import requests
from typing import Dict, Any, Optional, List
from config import (
    LIST_OUTBOUND_ENDPOINT,
    ERROR_MISSING_AUTH,
    API_KEY
)

def list_outbound_numbers(
    auth_token: str,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Retrieve a list of all outbound phone numbers in your account.
    
    Args:
        auth_token (str): Your API authentication token
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing:
            - status: Success/error status
            - numbers: List of outbound phone number objects with details
            
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
            LIST_OUTBOUND_ENDPOINT,
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
        result = list_outbound_numbers(
            auth_token=API_KEY
        )
        
        if result.get("status") == "success":
            print("Outbound numbers retrieved successfully!")
            numbers = result.get("numbers", [])
            
            if numbers:
                print("\nOutbound Numbers:")
                for number in numbers:
                    print(f"Phone Number: {number.get('phone_number')}")
                    print(f"Status: {number.get('status')}")
                    print(f"Created At: {number.get('created_at')}")
                    print(f"Last Used: {number.get('last_used')}")
                    print(f"Call Count: {number.get('call_count', 0)}")
                    print(f"Region: {number.get('region')}")
                    print(f"Country: {number.get('country')}")
                    print("-" * 40)
            else:
                print("No outbound numbers found.")
        else:
            print("Error:", result.get("message"))
            
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 