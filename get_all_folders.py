import requests
from typing import Dict, Any, Optional, List
from config import (
    FOLDERS_ENDPOINT,
    ERROR_MISSING_AUTH,
    API_KEY
)

def get_all_folders(
    auth_token: str,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Retrieve all folders in your account.
    
    Args:
        auth_token (str): Your API authentication token
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing:
            - status: Success/error status
            - folders: List of folder objects with details
            
    Raises:
        ValueError: If required parameters are missing
    """
    # Validate required parameters
    if not auth_token:
        raise ValueError(ERROR_MISSING_AUTH)

    # Prepare headers
    headers = {
        "authorization": auth_token
    }

    if org_id:
        headers["encrypted_key"] = org_id

    try:
        # Make API request
        response = requests.get(
            FOLDERS_ENDPOINT,
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
        result = get_all_folders(
            auth_token=API_KEY
        )
        
        if result.get("status") == "success":
            print("Folders retrieved successfully!")
            folders = result.get("folders", [])
            
            if folders:
                print("\nFolders:")
                for folder in folders:
                    print(f"ID: {folder.get('id')}")
                    print(f"Name: {folder.get('name')}")
                    print(f"Created: {folder.get('created_at')}")
                    print(f"Updated: {folder.get('updated_at')}")
                    print(f"Pathway Count: {folder.get('pathway_count', 0)}")
                    print("-" * 40)
            else:
                print("No folders found.")
        else:
            print("Error:", result.get("message"))
            
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 