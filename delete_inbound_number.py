import requests
from typing import Dict, Any, Optional
from config import (
    API_BASE_URL,
    API_VERSION,
    ERROR_MISSING_AUTH,
    ERROR_MISSING_PHONE,
    ERROR_INVALID_PHONE,
    API_KEY,
    DEFAULT_PHONE
)

# Define the endpoint
DELETE_INBOUND_NUMBER_ENDPOINT = f"{API_BASE_URL}/{API_VERSION}/phone/inbound/{{phone_number}}/delete"

def delete_inbound_number(
    auth_token: str,
    phone_number: str,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Delete an inbound phone number from your account.
    
    Args:
        auth_token (str): Your API authentication token
        phone_number (str): Phone number to delete (E.164 format)
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing:
            - status: Success/error status
            - message: Status message
            
    Raises:
        ValueError: If required parameters are missing or invalid
    """
    # Validate required parameters
    if not auth_token:
        raise ValueError(ERROR_MISSING_AUTH)
    if not phone_number:
        raise ValueError(ERROR_MISSING_PHONE)

    # Validate phone number format
    if not phone_number.startswith("+") or not phone_number[1:].isdigit():
        raise ValueError(ERROR_INVALID_PHONE)

    # Prepare headers
    headers = {
        "authorization": auth_token
    }

    if org_id:
        headers["encrypted_key"] = org_id

    try:
        # Make API request
        response = requests.delete(
            DELETE_INBOUND_NUMBER_ENDPOINT.format(phone_number=phone_number),
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
        # Get phone number from user or use default
        phone_number = input(f"Enter phone number to delete (default: {DEFAULT_PHONE}): ").strip()
        if not phone_number:
            phone_number = DEFAULT_PHONE
        
        # Confirm deletion
        confirm = input(f"Are you sure you want to delete phone number {phone_number}? (y/N): ")
        
        if confirm.lower() == 'y':
            # Double confirm for security
            confirm_again = input("This action cannot be undone. Type 'DELETE' to confirm: ")
            
            if confirm_again == "DELETE":
                result = delete_inbound_number(
                    auth_token=API_KEY,
                    phone_number=phone_number
                )
                
                if result.get("status") == "success":
                    print("Phone number deleted successfully!")
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