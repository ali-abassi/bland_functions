import requests
from typing import Dict, Any, Optional
from config import (
    API_BASE_URL,
    API_VERSION,
    ERROR_MISSING_AUTH,
    API_KEY
)

# Define the endpoint
DELETE_ENCRYPTED_KEY_ENDPOINT = f"{API_BASE_URL}/{API_VERSION}/encrypted-keys/{{key_id}}/delete"

def delete_encrypted_key(
    auth_token: str,
    key_id: str,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Delete an existing encrypted key.
    
    Args:
        auth_token (str): Your API authentication token
        key_id (str): ID of the encrypted key to delete
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
    if not key_id:
        raise ValueError("Missing required parameter: key_id")

    # Prepare headers
    headers = {
        "authorization": auth_token
    }

    if org_id:
        headers["encrypted_key"] = org_id

    try:
        # Make API request
        response = requests.delete(
            DELETE_ENCRYPTED_KEY_ENDPOINT.format(key_id=key_id),
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
        # Get key ID from user
        key_id = input("Enter encrypted key ID to delete: ")
        
        # Confirm deletion
        confirm = input(f"Are you sure you want to delete encrypted key {key_id}? (y/N): ")
        
        if confirm.lower() == 'y':
            # Double confirm for security
            confirm_again = input("This action cannot be undone. Type 'DELETE' to confirm: ")
            
            if confirm_again == "DELETE":
                result = delete_encrypted_key(
                    auth_token=API_KEY,
                    key_id=key_id
                )
                
                if result.get("status") == "success":
                    print("Encrypted key deleted successfully!")
                    print(f"Message: {result.get('message')}")
                else:
                    print("Error:", result.get("message"))
            else:
                print("Deletion cancelled: Confirmation text did not match")
        else:
            print("Deletion cancelled")
            
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 