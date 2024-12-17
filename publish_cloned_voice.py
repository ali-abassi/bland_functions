import requests
from typing import Dict, Any, Optional, List
from config import (
    PUBLISH_VOICE_ENDPOINT,
    ERROR_MISSING_AUTH,
    API_KEY
)

def publish_cloned_voice(
    auth_token: str,
    name: str,
    description: str,
    audio_files: List[str],
    language: Optional[str] = None,
    gender: Optional[str] = None,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Publish a cloned voice for use in calls.
    
    Args:
        auth_token (str): Your API authentication token
        name (str): Name for the cloned voice
        description (str): Description of the voice
        audio_files (list): List of audio file URLs or base64 encoded audio data
        language (str, optional): Language code for the voice (e.g., en-US)
        gender (str, optional): Gender of the voice (male/female)
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing:
            - status: Success/error status
            - voice_id: ID of the published voice
            - message: Status message
            
    Raises:
        ValueError: If required parameters are missing
    """
    # Validate required parameters
    if not auth_token:
        raise ValueError(ERROR_MISSING_AUTH)
    if not name:
        raise ValueError("Missing required parameter: name")
    if not description:
        raise ValueError("Missing required parameter: description")
    if not audio_files:
        raise ValueError("Missing required parameter: audio_files")

    # Prepare headers
    headers = {
        "authorization": auth_token,
        "Content-Type": "application/json"
    }

    if org_id:
        headers["encrypted_key"] = org_id

    # Prepare request data
    data = {
        "name": name,
        "description": description,
        "audio_files": audio_files
    }
    
    if language:
        data["language"] = language
    if gender:
        data["gender"] = gender

    try:
        # Make API request
        response = requests.post(
            PUBLISH_VOICE_ENDPOINT,
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
        # Example voice data
        voice_data = {
            "name": "Test Voice",
            "description": "A test cloned voice",
            "audio_files": [
                "https://example.com/audio1.wav",
                "https://example.com/audio2.wav"
            ],
            "language": "en-US",
            "gender": "female"
        }
        
        # Confirm publication
        confirm = input(f"Publish cloned voice '{voice_data['name']}'? (y/N): ")
        
        if confirm.lower() == 'y':
            result = publish_cloned_voice(
                auth_token=API_KEY,
                **voice_data
            )
            
            if result.get("status") == "success":
                print("Voice published successfully!")
                print(f"Voice ID: {result.get('voice_id')}")
                print(f"Message: {result.get('message')}")
            else:
                print("Error:", result.get("message"))
        else:
            print("Publication cancelled")
            
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 