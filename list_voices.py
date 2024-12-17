import requests
from typing import Dict, Any, Optional, List
from config import (
    LIST_VOICES_ENDPOINT,
    ERROR_MISSING_AUTH,
    API_KEY
)

def list_voices(
    auth_token: str,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Retrieve a list of all available voices for use in calls.
    
    Args:
        auth_token (str): Your API authentication token
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing:
            - status: Success/error status
            - voices: List of voice objects with details including:
                - id: Voice identifier
                - name: Display name of the voice
                - gender: Gender of the voice
                - language: Language code(s) supported
                - preview_url: URL to preview the voice
                - type: Type of voice (e.g., neural, standard)
            
    Raises:
        ValueError: If required parameters are missing
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

    try:
        # Make API request
        response = requests.get(
            LIST_VOICES_ENDPOINT,
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
        result = list_voices(
            auth_token=API_KEY
        )
        
        if result.get("status") == "success":
            print("Voices retrieved successfully!")
            voices = result.get("voices", [])
            
            if voices:
                print("\nAvailable Voices:")
                for voice in voices:
                    print(f"ID: {voice.get('id')}")
                    print(f"Name: {voice.get('name')}")
                    print(f"Gender: {voice.get('gender')}")
                    print(f"Language: {voice.get('language')}")
                    print(f"Type: {voice.get('type')}")
                    if voice.get('preview_url'):
                        print(f"Preview: {voice.get('preview_url')}")
                    print("-" * 40)
            else:
                print("No voices found.")
        else:
            print("Error:", result.get("message"))
            
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 