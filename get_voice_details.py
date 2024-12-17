import requests
from typing import Dict, Any, Optional
from config import (
    VOICE_DETAILS_ENDPOINT,
    ERROR_MISSING_AUTH,
    API_KEY
)

def get_voice_details(
    auth_token: str,
    voice_id: str,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Retrieve detailed information about a specific voice.
    
    Args:
        auth_token (str): Your API authentication token
        voice_id (str): ID of the voice to get details for
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing:
            - status: Success/error status
            - voice: Object containing voice details including:
                - id: Voice identifier
                - name: Display name of the voice
                - gender: Gender of the voice
                - language: Language code(s) supported
                - preview_url: URL to preview the voice
                - type: Type of voice (e.g., neural, standard)
                - description: Detailed description of the voice
                - capabilities: List of supported features
                - samples: List of sample audio clips
            
    Raises:
        ValueError: If required parameters are missing
    """
    # Validate required parameters
    if not auth_token:
        raise ValueError(ERROR_MISSING_AUTH)
    if not voice_id:
        raise ValueError("Missing required parameter: voice_id")

    # Prepare headers
    headers = {
        "authorization": auth_token
    }

    if org_id:
        headers["encrypted_key"] = org_id

    try:
        # Make API request
        response = requests.get(
            VOICE_DETAILS_ENDPOINT.format(voice_id=voice_id),
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
        # Example voice ID (you would get this from list_voices)
        voice_id = "example_voice_id"
        
        result = get_voice_details(
            auth_token=API_KEY,
            voice_id=voice_id
        )
        
        if result.get("status") == "success":
            print("Voice details retrieved successfully!")
            voice = result.get("voice", {})
            
            print("\nVoice Details:")
            print(f"ID: {voice.get('id')}")
            print(f"Name: {voice.get('name')}")
            print(f"Gender: {voice.get('gender')}")
            print(f"Language: {voice.get('language')}")
            print(f"Type: {voice.get('type')}")
            print(f"Description: {voice.get('description')}")
            
            if voice.get('capabilities'):
                print("\nCapabilities:")
                for capability in voice.get('capabilities', []):
                    print(f"- {capability}")
            
            if voice.get('preview_url'):
                print(f"\nPreview URL: {voice.get('preview_url')}")
            
            if voice.get('samples'):
                print("\nSample Audio Clips:")
                for sample in voice.get('samples', []):
                    print(f"- {sample.get('description')}: {sample.get('url')}")
        else:
            print("Error:", result.get("message"))
            
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 