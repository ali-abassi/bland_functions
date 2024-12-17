import requests
from typing import Dict, Any, Optional
from config import (
    UPDATE_FOLDER_ENDPOINT,
    ERROR_MISSING_AUTH,
    API_KEY
)

def update_folder(
    auth_token: str,
    folder_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Update a folder's details.
    
    Args:
        auth_token (str): Your API authentication token
        folder_id (str): ID of the folder to update
        name (str, optional): New name for the folder
        description (str, optional): New description for the folder
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing:
            - status: Success/error status
            - message: Status message
            
    Raises:
        ValueError: If required parameters are missing or no updates provided
    """
    # Validate required parameters
    if not auth_token:
        raise ValueError(ERROR_MISSING_AUTH)
    if not folder_id:
        raise ValueError("Missing required parameter: folder_id")
    if not name and not description:
        raise ValueError("At least one update field (name or description) must be provided")

    # Prepare headers
    headers = {
        "authorization": auth_token,
        "Content-Type": "application/json"
    }

    if org_id:
        headers["encrypted_key"] = org_id

    # Prepare request data
    data = {}
    if name:
        data["name"] = name
    if description:
        data["description"] = description

    try:
        # Make API request
        response = requests.patch(
            UPDATE_FOLDER_ENDPOINT.format(folder_id=folder_id),
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
        folder_id = "example_folder_id"
        
        # Example update data
        new_name = "Updated Test Folder"
        new_description = "An updated test folder for organizing pathways"
        
        result = update_folder(
            auth_token=API_KEY,
            folder_id=folder_id,
            name=new_name,
            description=new_description
        )
        
        if result.get("status") == "success":
            print("Folder updated successfully!")
            print(f"Message: {result.get('message')}")
        else:
            print("Error:", result.get("message"))
            
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 