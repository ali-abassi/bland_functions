import requests
from typing import Dict, Any
from config import (
    CALL_DETAILS_ENDPOINT,
    ERROR_MISSING_AUTH,
    ERROR_MISSING_CALL_ID,
    API_KEY,
    CALL_ID
)

def get_call_details(
    auth_token: str,
    call_id: str,
    org_id: str = None
) -> Dict[str, Any]:
    """
    Retrieve detailed information, metadata and transcripts for a specific call.
    
    Args:
        auth_token (str): Your API authentication token
        call_id (str): The unique identifier for the call
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing detailed call information including:
            - transcripts: Array of phrases spoken during the call
            - call_id: Unique identifier for the call
            - call_length: Length of call in minutes
            - transferred_to: Number call was transferred to (if applicable)
            - batch_id: Batch ID if part of a batch
            - to: Recipient phone number
            - from: Sender phone number
            - request_data: Original API request parameters
            - completed: Whether call is completed
            - inbound: Whether call was inbound
            - created_at: Call creation timestamp
            - started_at: Call start timestamp
            - end_at: Call end timestamp
            - queue_status: Current status of the call
            - endpoint_url: Deployment URL
            - max_duration: Maximum allowed duration
            - error_message: Any error messages
            - variables: System and generated variables
            - answered_by: Who answered (human/voicemail/etc)
            - record: Whether call was recorded
            - recording_url: URL of recording if available
            - metadata: Additional call metadata
            - summary: Call summary
            - price: Call cost in USD
            - call_ended_by: Who ended the call
            - pathway_logs: Detailed pathway information
            - analysis: Post-call analysis data
            - concatenated_transcript: Full call transcript
        
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

    if org_id:
        headers["encrypted_key"] = org_id

    try:
        # Make API request
        response = requests.get(
            CALL_DETAILS_ENDPOINT.format(call_id=call_id),
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
        result = get_call_details(
            auth_token=API_KEY,
            call_id=CALL_ID
        )
        print("Call Details Response:", result)
        
        # Print specific details of interest
        if result.get("status") != "error":
            print("\nKey Call Information:")
            print(f"Call Length: {result.get('call_length')} minutes")
            print(f"Status: {result.get('queue_status')}")
            print(f"Answered By: {result.get('answered_by')}")
            print(f"Cost: ${result.get('price')}")
            
            # Print first few transcript entries if available
            transcripts = result.get('transcripts', [])
            if transcripts:
                print("\nFirst 3 Transcript Entries:")
                for t in transcripts[:3]:
                    print(f"{t.get('user')}: {t.get('text')}")
        
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 