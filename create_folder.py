import requests
from typing import Dict, Any, Optional
from config import (
    CREATE_FOLDER_ENDPOINT,
    ERROR_MISSING_AUTH,
    API_KEY
)

def create_folder(
    auth_token: str,
    name: str,
    description: Optional[str] = None,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Create a new folder to organize pathways.
    
    Args:
        auth_token (str): Your API authentication token
        name (str): Name of the folder to create
        description (str, optional): Description of the folder
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing:
            - status: Success/error status
            - folder_id: ID of the created folder
            - message: Status message
            
    Raises:
        ValueError: If required parameters are missing
    """
    # Validate required parameters
    if not auth_token:
        raise ValueError(ERROR_MISSING_AUTH)
    if not name:
        raise ValueError("Missing required parameter: name")

    # Prepare headers
    headers = {
        "authorization": auth_token,
        "Content-Type": "application/json"
    }

    if org_id:
        headers["encrypted_key"] = org_id

    # Prepare request data
    data = {
        "name": name
    }
    
    if description:
        data["description"] = description

    try:
        # Make API request
        response = requests.post(
            CREATE_FOLDER_ENDPOINT,
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
        # Example folder data
        folder_name = "Test Folder"
        folder_description = "A test folder for organizing pathways"
        
        result = create_folder(
            auth_token=API_KEY,
            name=folder_name,
            description=folder_description
        )
        
        if result.get("status") == "success":
            print("Folder created successfully!")
            print(f"Folder ID: {result.get('folder_id')}")
            print(f"Message: {result.get('message')}")
        else:
            print("Error:", result.get("message"))
            
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 