import requests
from typing import Dict, Union
import re
from config import (
    CALLS_ENDPOINT,
    ERROR_MISSING_AUTH,
    ERROR_MISSING_PHONE,
    ERROR_INVALID_PHONE,
    ERROR_MISSING_ORG,
    API_KEY,
    DEFAULT_PHONE,
    ORG_ID,
    PATHWAY_ID
)

def send_call_pathway_simple(
    auth_token: str,
    phone_number: str,
    pathway_id: str,
    org_id: str = None
) -> Dict[str, Union[str, None]]:
    """
    Send an AI phone call using a predefined conversational pathway.
    
    Args:
        auth_token (str): Your API authentication token
        phone_number (str): The phone number to call (E.164 format preferred)
        pathway_id (str): The ID of the pathway to use for the conversation
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing status and call_id if successful
        
    Raises:
        ValueError: If required parameters are missing or invalid
    """
    # Validate required parameters
    if not auth_token:
        raise ValueError(ERROR_MISSING_AUTH)
    if not phone_number:
        raise ValueError(ERROR_MISSING_PHONE)
    if not pathway_id:
        raise ValueError("Missing required parameter: pathway_id")

    # Clean phone number
    phone_number = re.sub(r'[^\d+]', '', phone_number)
    
    # Validate phone number format
    if not re.match(r'^\+?\d{10,15}$', phone_number):
        raise ValueError(ERROR_INVALID_PHONE)

    # Prepare headers and payload
    headers = {
        "authorization": auth_token,
        "Content-Type": "application/json"
    }

    # Add organization ID if provided
    if org_id:
        headers["organization"] = org_id
    
    payload = {
        "phone_number": phone_number,
        "pathway_id": pathway_id
    }

    try:
        # Make API request
        response = requests.post(
            CALLS_ENDPOINT,
            headers=headers,
            json=payload
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
        result = send_call_pathway_simple(
            auth_token=API_KEY,
            phone_number=DEFAULT_PHONE,
            pathway_id=PATHWAY_ID,
            org_id=ORG_ID
        )
        print("API Response:", result)
        
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 