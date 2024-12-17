import requests
from typing import Dict, Any, Optional
from config import (
    API_BASE_URL,
    API_VERSION,
    ERROR_MISSING_AUTH,
    API_KEY
)

# Define the endpoint
BATCH_DETAILS_ENDPOINT = f"{API_BASE_URL}/{API_VERSION}/calls/batch/{{batch_id}}"

def get_batch_details(
    auth_token: str,
    batch_id: str,
    include_calls: Optional[bool] = False,
    call_status: Optional[str] = None,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Get detailed information about a specific batch of calls.
    
    Args:
        auth_token (str): Your API authentication token
        batch_id (str): ID of the batch to retrieve details for
        include_calls (bool, optional): Whether to include individual call details
        call_status (str, optional): Filter calls by status if including calls
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing:
            - status: Success/error status
            - batch: Batch object with detailed information
            - calls: List of call objects (if requested)
            - message: Status message
            
    Raises:
        ValueError: If required parameters are missing or invalid
    """
    # Validate required parameters
    if not auth_token:
        raise ValueError(ERROR_MISSING_AUTH)
    if not batch_id:
        raise ValueError("Missing required parameter: batch_id")

    # Validate call status if provided
    valid_statuses = ["queued", "in_progress", "completed", "failed", "cancelled"]
    if call_status and call_status not in valid_statuses:
        raise ValueError(f"Invalid call_status. Must be one of: {', '.join(valid_statuses)}")

    # Prepare headers
    headers = {
        "authorization": auth_token
    }

    if org_id:
        headers["encrypted_key"] = org_id

    # Prepare query parameters
    params = {}
    if include_calls:
        params["include_calls"] = "true"
        if call_status:
            params["call_status"] = call_status

    try:
        # Make API request
        response = requests.get(
            BATCH_DETAILS_ENDPOINT.format(batch_id=batch_id),
            headers=headers,
            params=params
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
        batch_id = input("Enter batch ID to get details for: ")
        
        # Get optional parameters
        include_calls = input("Include call details? (y/N): ").lower() == 'y'
        
        call_status = None
        if include_calls:
            print("\nAvailable call statuses:")
            print("1. queued")
            print("2. in_progress")
            print("3. completed")
            print("4. failed")
            print("5. cancelled")
            print("6. all (no filter)")
            
            status_choice = input("\nSelect call status filter (1-6): ").strip()
            if status_choice and status_choice != "6":
                status_map = {
                    "1": "queued",
                    "2": "in_progress",
                    "3": "completed",
                    "4": "failed",
                    "5": "cancelled"
                }
                call_status = status_map.get(status_choice)
        
        result = get_batch_details(
            auth_token=API_KEY,
            batch_id=batch_id,
            include_calls=include_calls,
            call_status=call_status
        )
        
        if result.get("status") == "success":
            batch = result.get("batch", {})
            
            print("\nBatch Details:")
            print(f"ID: {batch.get('id')}")
            print(f"Status: {batch.get('status')}")
            print(f"Created At: {batch.get('created_at')}")
            print(f"Total Calls: {batch.get('total_calls')}")
            print(f"Completed Calls: {batch.get('completed_calls')}")
            print(f"Failed Calls: {batch.get('failed_calls')}")
            
            # Display batch configuration
            config = batch.get('config', {})
            if config:
                print("\nConfiguration:")
                if config.get('task'):
                    print(f"Task: {config['task']}")
                if config.get('model'):
                    print(f"Model: {config['model']}")
                if config.get('voice'):
                    print(f"Voice: {config['voice']}")
                if config.get('max_duration'):
                    print(f"Max Duration: {config['max_duration']} minutes")
                if config.get('retry_config'):
                    retry = config['retry_config']
                    print("\nRetry Configuration:")
                    print(f"Max Attempts: {retry.get('max_attempts')}")
                    print(f"Retry Interval: {retry.get('retry_interval')} seconds")
            
            # Display call details if included
            calls = result.get("calls", [])
            if calls:
                print(f"\nCalls ({len(calls)}):")
                for call in calls:
                    print(f"\n  Call ID: {call.get('id')}")
                    print(f"  Phone Number: {call.get('phone_number')}")
                    print(f"  Status: {call.get('status')}")
                    print(f"  Duration: {call.get('duration')} seconds")
                    print(f"  Started At: {call.get('started_at')}")
                    print(f"  Completed At: {call.get('completed_at')}")
                    if call.get('error'):
                        print(f"  Error: {call['error']}")
        else:
            print("Error:", result.get("message"))
            
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 