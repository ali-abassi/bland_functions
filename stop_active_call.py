import requests
from typing import Dict, Any
from config import (
    STOP_CALL_ENDPOINT,
    ERROR_MISSING_AUTH,
    ERROR_MISSING_CALL_ID,
    API_KEY,
    CALL_ID
)

def stop_active_call(
    auth_token: str,
    call_id: str
) -> Dict[str, Any]:
    """
    End an active phone call by call_id.
    
    Args:
        auth_token (str): Your API authentication token
        call_id (str): The unique identifier for the call to stop
        
    Returns:
        dict: Response containing status and message
            Example success: {"status": "success", "message": "Call ended successfully."}
            Example error: {"status": "error", "message": "SID not found for the given c_id."}
        
    Raises:
        ValueError: If required parameters are missing
    """
    # Validate required parameters
    if not auth_token:
        raise ValueError(ERROR_MISSING_AUTH)
    if not call_id:
        raise ValueError(ERROR_MISSING_CALL_ID)

    # Prepare headers
    headers = {
        "authorization": auth_token
    }

    try:
        # Make API request
        response = requests.post(
            STOP_CALL_ENDPOINT.format(call_id=call_id),
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
        result = stop_active_call(
            auth_token=API_KEY,
            call_id=CALL_ID
        )
        print("API Response:", result)
        
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 