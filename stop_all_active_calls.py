import requests
from typing import Dict, Any
from config import (
    STOP_ALL_CALLS_ENDPOINT,
    ERROR_MISSING_AUTH,
    API_KEY
)

def stop_all_active_calls(
    auth_token: str
) -> Dict[str, Any]:
    """
    End all active phone calls on your account.
    
    Args:
        auth_token (str): Your API authentication token
        
    Returns:
        dict: Response containing status, message and number of calls stopped
            Example success: {
                "status": "success",
                "message": "Stopping active calls. This may take some time...",
                "num_calls": 12
            }
        
    Raises:
        ValueError: If authorization token is missing
    """
    # Validate required parameters
    if not auth_token:
        raise ValueError(ERROR_MISSING_AUTH)

    # Prepare headers
    headers = {
        "authorization": auth_token
    }

    try:
        # Make API request
        response = requests.post(
            STOP_ALL_CALLS_ENDPOINT,
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
        result = stop_all_active_calls(
            auth_token=API_KEY
        )
        print("API Response:", result)
        
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 