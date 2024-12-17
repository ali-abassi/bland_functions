import requests
from typing import Dict, Any, Optional, List, Union
from config import (
    API_BASE_URL,
    API_VERSION,
    ERROR_MISSING_AUTH,
    ERROR_MISSING_PHONE,
    ERROR_INVALID_PHONE,
    API_KEY,
    DEFAULT_MODEL,
    DEFAULT_VOICE,
    DEFAULT_LANGUAGE,
    DEFAULT_TEMPERATURE,
    DEFAULT_MAX_DURATION
)

# Define the endpoint
BATCH_CALLS_ENDPOINT = f"{API_BASE_URL}/{API_VERSION}/calls/batch"

def send_batch_calls(
    auth_token: str,
    phone_numbers: List[str],
    pathway_id: Optional[str] = None,
    task: Optional[str] = None,
    model: Optional[str] = DEFAULT_MODEL,
    voice: Optional[str] = DEFAULT_VOICE,
    language: Optional[str] = DEFAULT_LANGUAGE,
    temperature: Optional[float] = DEFAULT_TEMPERATURE,
    max_duration: Optional[int] = DEFAULT_MAX_DURATION,
    schedule_time: Optional[str] = None,
    retry_config: Optional[Dict[str, Any]] = None,
    metadata: Optional[Dict[str, Any]] = None,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Send a batch of calls with shared configuration.
    
    Args:
        auth_token (str): Your API authentication token
        phone_numbers (list): List of phone numbers to call
        pathway_id (str, optional): ID of the pathway to use
        task (str, optional): Task description for non-pathway calls
        model (str, optional): AI model to use (base, turbo, enhanced)
        voice (str, optional): Voice ID to use
        language (str, optional): Language code (e.g., en-US)
        temperature (float, optional): Model temperature (0.0 to 1.0)
        max_duration (int, optional): Maximum call duration in minutes
        schedule_time (str, optional): ISO 8601 timestamp for scheduled calls
        retry_config (dict, optional): Retry configuration for failed calls
        metadata (dict, optional): Additional metadata for the batch
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing:
            - status: Success/error status
            - batch_id: ID of the created batch
            - queued: Number of calls queued
            - failed: List of numbers that failed validation
            - message: Status message
            
    Raises:
        ValueError: If required parameters are missing or invalid
    """
    # Validate required parameters
    if not auth_token:
        raise ValueError(ERROR_MISSING_AUTH)
    if not phone_numbers:
        raise ValueError(ERROR_MISSING_PHONE)
    if not pathway_id and not task:
        raise ValueError("Either pathway_id or task must be provided")

    # Validate phone numbers format
    for number in phone_numbers:
        if not number.startswith("+") or not number[1:].isdigit():
            raise ValueError(f"{ERROR_INVALID_PHONE}: {number}")

    # Validate model
    if model and model not in ["base", "turbo", "enhanced"]:
        raise ValueError("Invalid model. Must be one of: base, turbo, enhanced")

    # Validate temperature
    if temperature is not None and not (0.0 <= temperature <= 1.0):
        raise ValueError("Temperature must be between 0.0 and 1.0")

    # Prepare headers
    headers = {
        "authorization": auth_token,
        "Content-Type": "application/json"
    }

    if org_id:
        headers["encrypted_key"] = org_id

    # Prepare request data
    data = {
        "phone_numbers": phone_numbers
    }

    # Add optional parameters if provided
    if pathway_id is not None:
        data["pathway_id"] = pathway_id
    if task is not None:
        data["task"] = task
    if model is not None:
        data["model"] = model
    if voice is not None:
        data["voice"] = voice
    if language is not None:
        data["language"] = language
    if temperature is not None:
        data["temperature"] = temperature
    if max_duration is not None:
        data["max_duration"] = max_duration
    if schedule_time is not None:
        data["schedule_time"] = schedule_time
    if retry_config is not None:
        data["retry_config"] = retry_config
    if metadata is not None:
        data["metadata"] = metadata

    try:
        # Make API request
        response = requests.post(
            BATCH_CALLS_ENDPOINT,
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
        # Example batch configuration
        test_numbers = [
            "+12025550101",
            "+12025550102",
            "+12025550103"
        ]
        
        batch_config = {
            "task": "Schedule a follow-up appointment",
            "model": "enhanced",
            "voice": "mason",
            "language": "en-US",
            "temperature": 0.7,
            "max_duration": 30,
            "retry_config": {
                "max_attempts": 3,
                "retry_interval": 300,  # 5 minutes
                "retry_reasons": ["no_answer", "busy", "failed"]
            },
            "metadata": {
                "campaign": "follow_up_appointments",
                "department": "sales",
                "priority": "high"
            }
        }
        
        # Confirm batch creation
        print("Phone numbers in batch:")
        for number in test_numbers:
            print(f"  - {number}")
            
        print("\nBatch Configuration:")
        print(f"Task: {batch_config['task']}")
        print(f"Model: {batch_config['model']}")
        print(f"Voice: {batch_config['voice']}")
        print(f"Max Duration: {batch_config['max_duration']} minutes")
        print(f"Max Retry Attempts: {batch_config['retry_config']['max_attempts']}")
        
        confirm = input("\nSend this batch of calls? (y/N): ")
        
        if confirm.lower() == 'y':
            result = send_batch_calls(
                auth_token=API_KEY,
                phone_numbers=test_numbers,
                **batch_config
            )
            
            if result.get("status") == "success":
                print("\nBatch created successfully!")
                print(f"Batch ID: {result.get('batch_id')}")
                print(f"Calls Queued: {result.get('queued', 0)}")
                
                if result.get('failed'):
                    print("\nFailed numbers:")
                    for failure in result.get('failed', []):
                        print(f"  - {failure.get('number')}: {failure.get('reason')}")
            else:
                print("Error:", result.get("message"))
        else:
            print("Batch creation cancelled")
            
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 