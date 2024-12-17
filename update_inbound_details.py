import requests
from typing import Dict, Any, Optional, Union
from config import (
    UPDATE_INBOUND_ENDPOINT,
    ERROR_MISSING_AUTH,
    ERROR_MISSING_PHONE,
    API_KEY,
    DEFAULT_PHONE
)

def update_inbound_details(
    auth_token: str,
    phone_number: str,
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
    Update the settings for an inbound phone number.
    
    Args:
        auth_token (str): Your API authentication token
        phone_number (str): The phone number to update settings for
        pathway_id (str, optional): ID of the pathway to use for inbound calls
        task (str, optional): Task description for the AI agent
        model (str, optional): AI model to use (base, turbo, enhanced)
        voice (str, optional): Voice to use for the AI agent
        language (str, optional): Language code for the AI agent
        temperature (float, optional): Temperature setting for AI responses
        max_duration (int, optional): Maximum call duration in minutes
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing:
            - status: Success/error status
            - message: Status message
            
    Raises:
        ValueError: If required parameters are missing
    """
    # Validate required parameters
    if not auth_token:
        raise ValueError(ERROR_MISSING_AUTH)
    if not phone_number:
        raise ValueError(ERROR_MISSING_PHONE)

    # Prepare headers
    headers = {
        "authorization": auth_token,
        "Content-Type": "application/json"
    }

    if org_id:
        headers["encrypted_key"] = org_id

    # Prepare request data
    data = {
        "phone_number": phone_number
    }
    
    # Add optional parameters if provided
    if pathway_id:
        data["pathway_id"] = pathway_id
    if task:
        data["task"] = task
    if model:
        data["model"] = model
    if voice:
        data["voice"] = voice
    if language:
        data["language"] = language
    if temperature is not None:
        data["temperature"] = temperature
    if max_duration:
        data["max_duration"] = max_duration

    try:
        # Make API request
        response = requests.post(
            UPDATE_INBOUND_ENDPOINT,
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
        # Example update parameters
        update_params = {
            "pathway_id": "example_pathway_id",
            "task": "Handle customer support calls",
            "model": "enhanced",
            "voice": "mason",
            "language": "en-US",
            "temperature": 0.7,
            "max_duration": 30
        }
        
        # Confirm update
        confirm = input(f"Update settings for phone number {DEFAULT_PHONE}? (y/N): ")
        
        if confirm.lower() == 'y':
            result = update_inbound_details(
                auth_token=API_KEY,
                phone_number=DEFAULT_PHONE,
                **update_params
            )
            
            if result.get("status") == "success":
                print("Inbound settings updated successfully!")
                print(f"Message: {result.get('message')}")
            else:
                print("Error:", result.get("message"))
        else:
            print("Update cancelled")
            
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 