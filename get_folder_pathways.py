import requests
from typing import Dict, Any, Optional, List
from config import (
    FOLDER_PATHWAYS_ENDPOINT,
    ERROR_MISSING_AUTH,
    API_KEY
)

def get_folder_pathways(
    auth_token: str,
    folder_id: str,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Retrieve all pathways in a specific folder.
    
    Args:
        auth_token (str): Your API authentication token
        folder_id (str): ID of the folder to get pathways from
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing:
            - status: Success/error status
            - pathways: List of pathway objects with details
            
    Raises:
        ValueError: If required parameters are missing
    """
    # Validate required parameters
    if not auth_token:
        raise ValueError(ERROR_MISSING_AUTH)
    if not folder_id:
        raise ValueError("Missing required parameter: folder_id")

    # Prepare headers
    headers = {
        "authorization": auth_token
    }

    if org_id:
        headers["encrypted_key"] = org_id

    try:
        # Make API request
        response = requests.get(
            FOLDER_PATHWAYS_ENDPOINT.format(folder_id=folder_id),
            headers=headers
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
        folder_id = "example_folder_id"
        
        result = get_folder_pathways(
            auth_token=API_KEY,
            folder_id=folder_id
        )
        
        if result.get("status") == "success":
            print(f"Pathways in folder {folder_id} retrieved successfully!")
            pathways = result.get("pathways", [])
            
            if pathways:
                print("\nPathways:")
                for pathway in pathways:
                    print(f"ID: {pathway.get('id')}")
                    print(f"Name: {pathway.get('name')}")
                    print(f"Description: {pathway.get('description')}")
                    print(f"Created: {pathway.get('created_at')}")
                    print(f"Updated: {pathway.get('updated_at')}")
                    print(f"Status: {pathway.get('status')}")
                    print("-" * 40)
            else:
                print("No pathways found in this folder.")
        else:
            print("Error:", result.get("message"))
            
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 