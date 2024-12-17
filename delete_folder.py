import requests
from typing import Dict, Any, Optional
from config import (
    DELETE_FOLDER_ENDPOINT,
    ERROR_MISSING_AUTH,
    API_KEY
)

def delete_folder(
    auth_token: str,
    folder_id: str,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Delete a folder and optionally all its contents.
    
    Args:
        auth_token (str): Your API authentication token
        folder_id (str): ID of the folder to delete
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
        response = requests.delete(
            DELETE_FOLDER_ENDPOINT.format(folder_id=folder_id),
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
        
        # Confirm deletion
        confirm = input(f"Are you sure you want to delete folder {folder_id}? This will also delete all pathways in the folder. (y/N): ")
        
        if confirm.lower() == 'y':
            result = delete_folder(
                auth_token=API_KEY,
                folder_id=folder_id
            )
            
            if result.get("status") == "success":
                print("Folder deleted successfully!")
                print(f"Message: {result.get('message')}")
            else:
                print("Error:", result.get("message"))
        else:
            print("Deletion cancelled")
            
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 