import requests
from typing import Dict, Any, Optional
from config import (
    API_BASE_URL,
    API_VERSION,
    ERROR_MISSING_AUTH,
    API_KEY
)

# Define the endpoint
ENCRYPTED_KEYS_ENDPOINT = f"{API_BASE_URL}/{API_VERSION}/encrypted-keys"

def create_encrypted_key(
    auth_token: str,
    name: str,
    key_type: str,
    value: str,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Create a new encrypted key for secure storage of sensitive information.
    
    Args:
        auth_token (str): Your API authentication token
        name (str): Name of the encrypted key
        key_type (str): Type of key (e.g., "api_key", "password", "token")
        value (str): The sensitive value to encrypt
        description (str, optional): Description of what the key is used for
        metadata (dict, optional): Additional metadata about the key
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing:
            - status: Success/error status
            - key_id: ID of the created encrypted key
            - message: Status message
            
    Raises:
        ValueError: If required parameters are missing or invalid
    """
    # Validate required parameters
    if not auth_token:
        raise ValueError(ERROR_MISSING_AUTH)
    if not name:
        raise ValueError("Missing required parameter: name")
    if not key_type:
        raise ValueError("Missing required parameter: key_type")
    if not value:
        raise ValueError("Missing required parameter: value")

    # Validate key type
    valid_key_types = ["api_key", "password", "token", "secret"]
    if key_type not in valid_key_types:
        raise ValueError(f"Invalid key_type. Must be one of: {', '.join(valid_key_types)}")

    # Prepare headers
    headers = {
        "authorization": auth_token,
        "Content-Type": "application/json"
    }

    if org_id:
        headers["encrypted_key"] = org_id

    # Prepare request data
    data = {
        "name": name,
        "type": key_type,
        "value": value
    }

    # Add optional parameters if provided
    if description is not None:
        data["description"] = description
    if metadata is not None:
        data["metadata"] = metadata

    try:
        # Make API request
        response = requests.post(
            ENCRYPTED_KEYS_ENDPOINT,
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
        # Example key creation
        key_config = {
            "name": "Test API Key",
            "key_type": "api_key",
            "value": "test_api_key_12345",
            "description": "Test API key for development",
            "metadata": {
                "environment": "development",
                "service": "test_service",
                "created_by": "developer"
            }
        }
        
        # Confirm key creation
        confirm = input("Create new encrypted key? (y/N): ")
        
        if confirm.lower() == 'y':
            result = create_encrypted_key(
                auth_token=API_KEY,
                **key_config
            )
            
            if result.get("status") == "success":
                print("Encrypted key created successfully!")
                print(f"Key ID: {result.get('key_id')}")
                print(f"Message: {result.get('message')}")
            else:
                print("Error:", result.get("message"))
        else:
            print("Key creation cancelled")
            
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 