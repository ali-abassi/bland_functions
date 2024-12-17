import requests
from typing import Dict, Any, Optional, List, Union
from config import (
    API_BASE_URL,
    API_VERSION,
    ERROR_MISSING_AUTH,
    ERROR_MISSING_PHONE,
    ERROR_INVALID_PHONE,
    API_KEY
)

# Define the endpoint
UPLOAD_INBOUND_NUMBERS_ENDPOINT = f"{API_BASE_URL}/{API_VERSION}/phone/inbound/upload"

def upload_inbound_numbers(
    auth_token: str,
    phone_numbers: List[str],
    pathway_id: Optional[str] = None,
    task: Optional[str] = None,
    model: Optional[str] = None,
    voice: Optional[str] = None,
    language: Optional[str] = None,
    temperature: Optional[float] = None,
    max_duration: Optional[int] = None,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Upload a batch of inbound phone numbers with optional configuration.
    
    Args:
        auth_token (str): Your API authentication token
        phone_numbers (list): List of phone numbers to upload
        pathway_id (str, optional): ID of the pathway to use for these numbers
        task (str, optional): Task description for non-pathway calls
        model (str, optional): AI model to use (base, turbo, enhanced)
        voice (str, optional): Voice ID to use
        language (str, optional): Language code (e.g., en-US)
        temperature (float, optional): Model temperature (0.0 to 1.0)
        max_duration (int, optional): Maximum call duration in minutes
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing:
            - status: Success/error status
            - uploaded: List of successfully uploaded numbers
            - failed: List of numbers that failed to upload
            - message: Status message
            
    Raises:
        ValueError: If required parameters are missing or invalid
    """
    # Validate required parameters
    if not auth_token:
        raise ValueError(ERROR_MISSING_AUTH)
    if not phone_numbers:
        raise ValueError(ERROR_MISSING_PHONE)

    # Validate phone numbers format
    for number in phone_numbers:
        if not number.startswith("+") or not number[1:].isdigit():
            raise ValueError(f"{ERROR_INVALID_PHONE}: {number}")

    # Validate model if provided
    if model and model not in ["base", "turbo", "enhanced"]:
        raise ValueError("Invalid model. Must be one of: base, turbo, enhanced")

    # Validate temperature if provided
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

    try:
        # Make API request
        response = requests.post(
            UPLOAD_INBOUND_NUMBERS_ENDPOINT,
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
        # Example phone numbers and configuration
        test_numbers = [
            "+12025550101",
            "+12025550102",
            "+12025550103"
        ]
        
        upload_config = {
            "pathway_id": "example_pathway_id",
            "model": "enhanced",
            "voice": "mason",
            "language": "en-US",
            "temperature": 0.7,
            "max_duration": 30
        }
        
        # Confirm upload
        print("Phone numbers to upload:")
        for number in test_numbers:
            print(f"  - {number}")
        
        confirm = input("\nUpload these numbers? (y/N): ")
        
        if confirm.lower() == 'y':
            result = upload_inbound_numbers(
                auth_token=API_KEY,
                phone_numbers=test_numbers,
                **upload_config
            )
            
            if result.get("status") == "success":
                print("\nUpload Results:")
                print(f"Successfully uploaded: {len(result.get('uploaded', []))}")
                print(f"Failed to upload: {len(result.get('failed', []))}")
                
                if result.get('failed'):
                    print("\nFailed numbers:")
                    for failure in result.get('failed', []):
                        print(f"  - {failure.get('number')}: {failure.get('reason')}")
            else:
                print("Error:", result.get("message"))
        else:
            print("Upload cancelled")
            
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 