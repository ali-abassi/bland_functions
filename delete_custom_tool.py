import requests
from typing import Dict, Any, Optional
from config import (
    DELETE_CUSTOM_TOOL_ENDPOINT,
    ERROR_MISSING_AUTH,
    API_KEY
)

def delete_custom_tool(
    auth_token: str,
    tool_id: str,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Delete an existing custom tool.
    
    Args:
        auth_token (str): Your API authentication token
        tool_id (str): ID of the tool to delete
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
    if not tool_id:
        raise ValueError("Missing required parameter: tool_id")

    # Prepare headers
    headers = {
        "authorization": auth_token
    }

    if org_id:
        headers["encrypted_key"] = org_id

    try:
        # Make API request
        response = requests.delete(
            DELETE_CUSTOM_TOOL_ENDPOINT.format(tool_id=tool_id),
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
        # Get tool ID from user
        tool_id = input("Enter tool ID to delete: ")
        
        # Confirm deletion
        confirm = input(f"Are you sure you want to delete tool {tool_id}? (y/N): ")
        
        if confirm.lower() == 'y':
            result = delete_custom_tool(
                auth_token=API_KEY,
                tool_id=tool_id
            )
            
            if result.get("status") == "success":
                print("Custom tool deleted successfully!")
                print(f"Message: {result.get('message')}")
            else:
                print("Error:", result.get("message"))
        else:
            print("Deletion cancelled")
            
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 