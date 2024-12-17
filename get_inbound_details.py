import requests
from typing import Dict, Any, Optional
from config import (
    INBOUND_DETAILS_ENDPOINT,
    ERROR_MISSING_AUTH,
    ERROR_MISSING_PHONE,
    API_KEY,
    DEFAULT_PHONE
)

def get_inbound_details(
    auth_token: str,
    phone_number: str,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Retrieve details of a specific inbound phone number.
    
    Args:
        auth_token (str): Your API authentication token
        phone_number (str): The phone number to get details for
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing:
            - status: Success/error status
            - number: Object containing phone number details
            
    Raises:
        ValueError: If required parameters are missing
    """
    # Validate required parameters
    if not auth_token:
        raise ValueError(ERROR_MISSING_AUTH)
    if not phone_number:
        raise ValueError(ERROR_MISSING_PHONE)

    # Prepare headers
    headers = {
        "authorization": auth_token
    }

    if org_id:
        headers["encrypted_key"] = org_id

    try:
        # Make API request
        response = requests.get(
            INBOUND_DETAILS_ENDPOINT.format(phone_number=phone_number),
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
        result = get_inbound_details(
            auth_token=API_KEY,
            phone_number=DEFAULT_PHONE
        )
        
        if result.get("status") == "success":
            print("Inbound number details retrieved successfully!")
            number = result.get("number", {})
            
            print("\nNumber Details:")
            print(f"Phone Number: {number.get('phone_number')}")
            print(f"Status: {number.get('status')}")
            print(f"Pathway ID: {number.get('pathway_id')}")
            print(f"Task: {number.get('task')}")
            print(f"Model: {number.get('model')}")
            print(f"Voice: {number.get('voice')}")
            print(f"Language: {number.get('language')}")
            print(f"Temperature: {number.get('temperature')}")
            print(f"Max Duration: {number.get('max_duration')} minutes")
            
            # Additional details that might be specific to a single number
            print(f"Created At: {number.get('created_at')}")
            print(f"Updated At: {number.get('updated_at')}")
            print(f"Last Used: {number.get('last_used')}")
        else:
            print("Error:", result.get("message"))
            
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 