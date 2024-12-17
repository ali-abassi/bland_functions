import requests
from typing import Dict, Any, Optional
from config import (
    MOVE_PATHWAY_ENDPOINT,
    ERROR_MISSING_AUTH,
    ERROR_MISSING_PATHWAY,
    API_KEY,
    PATHWAY_ID
)

def move_pathway(
    auth_token: str,
    pathway_id: str,
    folder_id: Optional[str] = None,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Move a pathway to a different folder or to root if no folder_id is provided.
    
    Args:
        auth_token (str): Your API authentication token
        pathway_id (str): ID of the pathway to move
        folder_id (str, optional): ID of the destination folder (None for root)
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing:
            - status: Success/error status
            - message: Status message
            
    Raises:
        ValueError: If required parameters are missing
    """
    # Validate required parameters
    if not auth_token:
        raise ValueError(ERROR_MISSING_AUTH)
    if not pathway_id:
        raise ValueError(ERROR_MISSING_PATHWAY)

    # Prepare headers
    headers = {
        "authorization": auth_token,
        "Content-Type": "application/json"
    }

    if org_id:
        headers["encrypted_key"] = org_id

    # Prepare request data
    data = {}
    if folder_id:
        data["folder_id"] = folder_id

    try:
        # Make API request
        response = requests.post(
            MOVE_PATHWAY_ENDPOINT.format(pathway_id=pathway_id),
            headers=headers,
            json=data
        )
        response.raise_for_status()
        
        return response.json()
        
    except requests.exceptions.RequestException as e:
        return {
            "status": "error",
            "message": str(e)
        }

if __name__ == "__main__":
    # Test the function using config values
    try:
        # Example folder ID (you would get this from get_all_folders)
        destination_folder_id = "example_folder_id"
        
        # Confirm move
        if destination_folder_id:
            confirm = input(f"Move pathway {PATHWAY_ID} to folder {destination_folder_id}? (y/N): ")
        else:
            confirm = input(f"Move pathway {PATHWAY_ID} to root? (y/N): ")
        
        if confirm.lower() == 'y':
            result = move_pathway(
                auth_token=API_KEY,
                pathway_id=PATHWAY_ID,
                folder_id=destination_folder_id
            )
            
            if result.get("status") == "success":
                print("Pathway moved successfully!")
                print(f"Message: {result.get('message')}")
            else:
                print("Error:", result.get("message"))
        else:
            print("Move cancelled")
            
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 