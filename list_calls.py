import requests
from typing import Dict, Any, Optional
from config import (
    CALLS_ENDPOINT,
    ERROR_MISSING_AUTH,
    API_KEY,
    DEFAULT_LIMIT
)

def list_calls(
    auth_token: str,
    from_number: str = None,
    to_number: str = None,
    from_index: int = None,
    to_index: int = None,
    limit: int = DEFAULT_LIMIT,
    ascending: bool = False,
    start_date: str = None,
    end_date: str = None,
    created_at: str = None,
    completed: bool = None,
    batch_id: str = None,
    answered_by: str = None,
    inbound: bool = None,
    duration_gt: float = None,
    duration_lt: float = None,
    campaign_id: str = None,
    org_id: str = None
) -> Dict[str, Any]:
    """
    Retrieve a list of calls with optional filtering parameters.
    
    Args:
        auth_token (str): Your API authentication token
        from_number (str, optional): Filter calls by the number they were dispatched from
        to_number (str, optional): Filter calls by the number they were dispatched to
        from_index (int, optional): Starting index for pagination
        to_index (int, optional): Ending index for pagination
        limit (int, optional): Maximum number of calls to return (default: 1000)
        ascending (bool, optional): Sort calls by creation time ascending
        start_date (str, optional): Get calls including and after date (YYYY-MM-DD)
        end_date (str, optional): Get calls including and before date (YYYY-MM-DD)
        created_at (str, optional): Get calls for specific date (YYYY-MM-DD)
        completed (bool, optional): Filter by completion status
        batch_id (str, optional): Get calls from specific batch
        answered_by (str, optional): Filter by who answered (e.g., "human")
        inbound (bool, optional): Filter based on call direction
        duration_gt (float, optional): Duration greater than value in minutes
        duration_lt (float, optional): Duration less than value in minutes
        campaign_id (str, optional): Get calls for specific campaign
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing total count, returned count, and calls array
            Example: {
                "total_count": 784,
                "count": 100,
                "calls": [
                    {
                        "call_id": "c1234567-89ab-cdef-0123-456789abcdef",
                        "created_at": "2023-12-21T23:25:14.801193+00:00",
                        "call_length": 0.834,
                        "to": "5551234567",
                        "from": "+15551234567",
                        "completed": true,
                        "queue_status": "complete",
                        "error_message": null,
                        "answered_by": "human",
                        "batch_id": "b1234567-89ab-cdef-0123-gen-batch"
                    },
                    ...
                ]
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

    if org_id:
        headers["encrypted_key"] = org_id

    # Build query parameters
    params = {
        'limit': limit,
        'ascending': ascending
    }

    # Add optional query parameters
    optional_params = {
        'from_number': from_number,
        'to_number': to_number,
        'from': from_index,
        'to': to_index,
        'start_date': start_date,
        'end_date': end_date,
        'created_at': created_at,
        'completed': completed,
        'batch_id': batch_id,
        'answered_by': answered_by,
        'inbound': inbound,
        'duration_gt': duration_gt,
        'duration_lt': duration_lt,
        'campaign_id': campaign_id
    }

    # Add non-None optional parameters to query
    params.update({k: v for k, v in optional_params.items() if v is not None})

    try:
        # Make API request
        response = requests.get(
            CALLS_ENDPOINT,
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
        # Example 1: List recent calls with default parameters
        result_simple = list_calls(
            auth_token=API_KEY,
            limit=5  # Limit to 5 calls for testing
        )
        print("Simple List Response:", result_simple)

        # Example 2: List calls with filters
        result_filtered = list_calls(
            auth_token=API_KEY,
            limit=5,
            completed=True,
            answered_by="human",
            duration_gt=0.5,  # Calls longer than 30 seconds
            ascending=True
        )
        print("\nFiltered List Response:", result_filtered)
        
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 