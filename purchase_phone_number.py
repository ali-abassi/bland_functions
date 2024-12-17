import requests
from typing import Dict, Any, Optional, List
from config import (
    PURCHASE_PHONE_ENDPOINT,
    ERROR_MISSING_AUTH,
    API_KEY
)

def purchase_phone_number(
    auth_token: str,
    area_code: Optional[str] = None,
    country: Optional[str] = None,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Purchase a new phone number for your account.
    
    Args:
        auth_token (str): Your API authentication token
        area_code (str, optional): Desired area code for the phone number
        country (str, optional): Two-letter country code (default: US)
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing:
            - status: Success/error status
            - phone_number: The purchased phone number
            - message: Status message
            
    Raises:
        ValueError: If required parameters are missing
    """
    # Validate required parameters
    if not auth_token:
        raise ValueError(ERROR_MISSING_AUTH)

    # Prepare headers
    headers = {
        "authorization": auth_token,
        "Content-Type": "application/json"
    }

    if org_id:
        headers["encrypted_key"] = org_id

    # Prepare request data
    data = {}
    if area_code:
        data["area_code"] = area_code
    if country:
        data["country"] = country

    try:
        # Make API request
        response = requests.post(
            PURCHASE_PHONE_ENDPOINT,
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
        # Example purchase parameters
        desired_area_code = "415"  # San Francisco area code
        
        # Confirm purchase
        confirm = input(f"Purchase a new phone number{' with area code ' + desired_area_code if desired_area_code else ''}? (y/N): ")
        
        if confirm.lower() == 'y':
            result = purchase_phone_number(
                auth_token=API_KEY,
                area_code=desired_area_code
            )
            
            if result.get("status") == "success":
                print("Phone number purchased successfully!")
                print(f"Phone Number: {result.get('phone_number')}")
                print(f"Message: {result.get('message')}")
            else:
                print("Error:", result.get("message"))
        else:
            print("Purchase cancelled")
            
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 