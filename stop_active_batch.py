import requests
from typing import Dict, Any, Optional
from config import (
    API_BASE_URL,
    API_VERSION,
    ERROR_MISSING_AUTH,
    API_KEY
)

# Define the endpoint
STOP_BATCH_ENDPOINT = f"{API_BASE_URL}/{API_VERSION}/calls/batch/{{batch_id}}/stop"

def stop_active_batch(
    auth_token: str,
    batch_id: str,
    stop_reason: Optional[str] = None,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Stop an active batch of calls.
    
    Args:
        auth_token (str): Your API authentication token
        batch_id (str): ID of the batch to stop
        stop_reason (str, optional): Reason for stopping the batch
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing:
            - status: Success/error status
            - stopped: Number of calls stopped
            - message: Status message
            
    Raises:
        ValueError: If required parameters are missing
    """
    # Validate required parameters
    if not auth_token:
        raise ValueError(ERROR_MISSING_AUTH)
    if not batch_id:
        raise ValueError("Missing required parameter: batch_id")

    # Prepare headers
    headers = {
        "authorization": auth_token,
        "Content-Type": "application/json"
    }

    if org_id:
        headers["encrypted_key"] = org_id

    # Prepare request data
    data = {}
    if stop_reason is not None:
        data["reason"] = stop_reason

    try:
        # Make API request
        response = requests.post(
            STOP_BATCH_ENDPOINT.format(batch_id=batch_id),
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
        # Get batch ID from user
        batch_id = input("Enter batch ID to stop: ")
        
        # Get optional stop reason
        stop_reason = input("Enter reason for stopping (optional): ").strip() or None
        
        # Confirm stop
        confirm = input(f"Are you sure you want to stop batch {batch_id}? (y/N): ")
        
        if confirm.lower() == 'y':
            result = stop_active_batch(
                auth_token=API_KEY,
                batch_id=batch_id,
                stop_reason=stop_reason
            )
            
            if result.get("status") == "success":
                print("\nBatch stopped successfully!")
                print(f"Calls Stopped: {result.get('stopped', 0)}")
                print(f"Message: {result.get('message')}")
            else:
                print("Error:", result.get("message"))
        else:
            print("Stop operation cancelled")
            
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 