import requests
from typing import Dict, Any, Optional, List
from config import (
    API_BASE_URL,
    API_VERSION,
    ERROR_MISSING_AUTH,
    DEFAULT_LIMIT,
    API_KEY
)

# Define the endpoint
BATCHES_ENDPOINT = f"{API_BASE_URL}/{API_VERSION}/calls/batch"

def list_batches(
    auth_token: str,
    limit: Optional[int] = DEFAULT_LIMIT,
    offset: Optional[int] = 0,
    status: Optional[List[str]] = None,
    date_range: Optional[Dict[str, str]] = None,
    sort_by: Optional[str] = None,
    sort_order: Optional[str] = "desc",
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    List batches of calls with filtering and pagination support.
    
    Args:
        auth_token (str): Your API authentication token
        limit (int, optional): Maximum number of batches to return (default: 1000)
        offset (int, optional): Number of batches to skip (default: 0)
        status (list, optional): Filter by batch status (e.g., ["active", "completed", "failed"])
        date_range (dict, optional): Filter by date range (e.g., {"start": "2024-01-01", "end": "2024-01-31"})
        sort_by (str, optional): Field to sort by (e.g., "created_at", "total_calls")
        sort_order (str, optional): Sort order ("asc" or "desc", default: "desc")
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing:
            - status: Success/error status
            - batches: List of batch objects
            - total: Total number of batches
            - message: Status message
            
    Raises:
        ValueError: If required parameters are missing or invalid
    """
    # Validate required parameters
    if not auth_token:
        raise ValueError(ERROR_MISSING_AUTH)
    
    # Validate pagination parameters
    if limit is not None and limit < 1:
        raise ValueError("Limit must be greater than 0")
    if offset is not None and offset < 0:
        raise ValueError("Offset must be greater than or equal to 0")

    # Validate sort order
    if sort_order and sort_order not in ["asc", "desc"]:
        raise ValueError("Sort order must be either 'asc' or 'desc'")

    # Prepare headers
    headers = {
        "authorization": auth_token
    }

    if org_id:
        headers["encrypted_key"] = org_id

    # Prepare query parameters
    params = {}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    if status:
        params["status"] = status
    if date_range:
        params["date_range"] = date_range
    if sort_by:
        params["sort_by"] = sort_by
        params["sort_order"] = sort_order

    try:
        # Make API request
        response = requests.get(
            BATCHES_ENDPOINT,
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
        # Example: List recent batches with filters
        list_config = {
            "limit": 10,
            "status": ["active", "completed"],
            "date_range": {
                "start": "2024-01-01",
                "end": "2024-01-31"
            },
            "sort_by": "created_at",
            "sort_order": "desc"
        }
        
        result = list_batches(
            auth_token=API_KEY,
            **list_config
        )
        
        if result.get("status") == "success":
            batches = result.get("batches", [])
            total = result.get("total", 0)
            
            print(f"Found {total} batches:")
            for batch in batches:
                print(f"\nBatch ID: {batch.get('id')}")
                print(f"Status: {batch.get('status')}")
                print(f"Total Calls: {batch.get('total_calls')}")
                print(f"Completed Calls: {batch.get('completed_calls')}")
                print(f"Failed Calls: {batch.get('failed_calls')}")
                print(f"Created At: {batch.get('created_at')}")
                
                # Display batch configuration if available
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
        else:
            print("Error:", result.get("message"))
            
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 