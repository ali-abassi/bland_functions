import requests
from typing import Dict, Any, Optional, Union
from config import (
    GENERATE_AUDIO_ENDPOINT,
    ERROR_MISSING_AUTH,
    API_KEY,
    DEFAULT_VOICE
)

def generate_audio_sample(
    auth_token: str,
    text: str,
    voice_id: Optional[str] = None,
    language: Optional[str] = None,
    speed: Optional[float] = None,
    pitch: Optional[float] = None,
    format: Optional[str] = None,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Generate an audio sample using a specified voice.
    
    Args:
        auth_token (str): Your API authentication token
        text (str): The text to convert to speech
        voice_id (str, optional): ID of the voice to use (default: system default)
        language (str, optional): Language code for the voice (e.g., en-US)
        speed (float, optional): Speech rate (0.5 to 2.0, default: 1.0)
        pitch (float, optional): Voice pitch (-20 to 20, default: 0)
        format (str, optional): Audio format (wav/mp3, default: mp3)
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing:
            - status: Success/error status
            - audio_url: URL to download the generated audio
            - duration: Duration of the audio in seconds
            - message: Status message
            
    Raises:
        ValueError: If required parameters are missing or invalid
    """
    # Validate required parameters
    if not auth_token:
        raise ValueError(ERROR_MISSING_AUTH)
    if not text:
        raise ValueError("Missing required parameter: text")
    if speed is not None and not (0.5 <= speed <= 2.0):
        raise ValueError("Speed must be between 0.5 and 2.0")
    if pitch is not None and not (-20 <= pitch <= 20):
        raise ValueError("Pitch must be between -20 and 20")

    # Prepare headers
    headers = {
        "authorization": auth_token,
        "Content-Type": "application/json"
    }

    if org_id:
        headers["encrypted_key"] = org_id

    # Prepare request data
    data = {
        "text": text
    }
    
    if voice_id:
        data["voice_id"] = voice_id
    if language:
        data["language"] = language
    if speed is not None:
        data["speed"] = speed
    if pitch is not None:
        data["pitch"] = pitch
    if format:
        data["format"] = format

    try:
        # Make API request
        response = requests.post(
            GENERATE_AUDIO_ENDPOINT,
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
        # Example generation parameters
        sample_text = "Hello! This is a test of the audio generation system."
        
        # Confirm generation
        confirm = input(f"Generate audio sample with text: '{sample_text}'? (y/N): ")
        
        if confirm.lower() == 'y':
            result = generate_audio_sample(
                auth_token=API_KEY,
                text=sample_text,
                voice_id=DEFAULT_VOICE,
                speed=1.0,
                pitch=0,
                format="mp3"
            )
            
            if result.get("status") == "success":
                print("Audio sample generated successfully!")
                print(f"Audio URL: {result.get('audio_url')}")
                print(f"Duration: {result.get('duration')} seconds")
                print(f"Message: {result.get('message')}")
            else:
                print("Error:", result.get("message"))
        else:
            print("Generation cancelled")
            
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 