import requests
from typing import Dict, Union, List, Optional, Any
import re
from config import (
    CALLS_ENDPOINT,
    ERROR_MISSING_AUTH,
    ERROR_MISSING_PHONE,
    ERROR_MISSING_TASK,
    ERROR_INVALID_PHONE,
    ERROR_MISSING_ORG,
    ERROR_INVALID_MODEL,
    ERROR_INVALID_LANGUAGE,
    API_KEY,
    DEFAULT_PHONE,
    ORG_ID,
    DEFAULT_MODEL,
    DEFAULT_VOICE,
    DEFAULT_LANGUAGE,
    DEFAULT_MAX_DURATION,
    DEFAULT_TEMPERATURE,
    DEFAULT_INTERRUPTION_THRESHOLD,
    BACKGROUND_TRACKS
)

def send_call(
    auth_token: str,
    phone_number: str,
    task: str = None,
    pathway_id: str = None,
    start_node_id: str = None,
    voice: str = DEFAULT_VOICE,
    background_track: str = None,
    first_sentence: str = None,
    wait_for_greeting: bool = False,
    block_interruptions: bool = False,
    interruption_threshold: int = DEFAULT_INTERRUPTION_THRESHOLD,
    model: str = DEFAULT_MODEL,
    temperature: float = DEFAULT_TEMPERATURE,
    keywords: List[str] = None,
    pronunciation_guide: List[Dict] = None,
    transfer_phone_number: str = None,
    transfer_list: Dict[str, str] = None,
    language: str = DEFAULT_LANGUAGE,
    timezone: str = None,
    request_data: Dict = None,
    tools: List[Dict] = None,
    dynamic_data: List[Dict] = None,
    start_time: str = None,
    voicemail_message: str = None,
    voicemail_action: Dict = None,
    retry: Dict = None,
    max_duration: int = DEFAULT_MAX_DURATION,
    record: bool = False,
    from_number: str = None,
    webhook: str = None,
    webhook_events: List[str] = None,
    metadata: Dict = None,
    summary_prompt: str = None,
    analysis_prompt: str = None,
    analysis_schema: Dict = None,
    answered_by_enabled: bool = False,
    org_id: str = None
) -> Dict[str, Any]:
    """
    Send an AI phone call with comprehensive configuration options.
    
    Args:
        auth_token (str): Your API authentication token
        phone_number (str): The phone number to call (E.164 format preferred)
        task (str, optional): Instructions for the AI agent (required if pathway_id not provided)
        pathway_id (str, optional): The ID of the pathway to use (required if task not provided)
        start_node_id (str, optional): The starting node ID for pathway calls
        voice (str, optional): Voice ID or name to use
        background_track (str, optional): Background audio track
        first_sentence (str, optional): First thing the agent should say
        wait_for_greeting (bool, optional): Whether to wait for recipient to speak first
        block_interruptions (bool, optional): Whether to ignore user interruptions
        interruption_threshold (int, optional): Patience level for interruptions (50-200)
        model (str, optional): AI model to use (base, turbo, or enhanced)
        temperature (float, optional): Model temperature setting
        keywords (List[str], optional): Words to boost in transcription
        pronunciation_guide (List[Dict], optional): Guide for word pronunciation
        transfer_phone_number (str, optional): Number to transfer to
        transfer_list (Dict[str, str], optional): Multiple transfer options
        language (str, optional): Language code
        timezone (str, optional): Timezone for the call
        request_data (Dict, optional): Additional data for the call
        tools (List[Dict], optional): Custom tools for the agent
        dynamic_data (List[Dict], optional): Dynamic data configuration
        start_time (str, optional): When to start the call
        voicemail_message (str, optional): Message for voicemail
        voicemail_action (Dict, optional): Action when voicemail detected
        retry (Dict, optional): Retry configuration
        max_duration (int, optional): Maximum call duration in minutes
        record (bool, optional): Whether to record the call
        from_number (str, optional): Number to call from
        webhook (str, optional): Webhook URL for call events
        webhook_events (List[str], optional): Specific events to trigger webhook
        metadata (Dict, optional): Additional metadata
        summary_prompt (str, optional): Custom prompt for call summary
        analysis_prompt (str, optional): Custom prompt for call analysis
        analysis_schema (Dict, optional): Schema for call analysis
        answered_by_enabled (bool, optional): Enable answer detection
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing status and call_id if successful
        
    Raises:
        ValueError: If required parameters are missing or invalid
    """
    # Validate required parameters
    if not auth_token:
        raise ValueError(ERROR_MISSING_AUTH)
    if not phone_number:
        raise ValueError(ERROR_MISSING_PHONE)
    if not task and not pathway_id:
        raise ValueError("Either task or pathway_id must be provided")

    # Clean phone number
    phone_number = re.sub(r'[^\d+]', '', phone_number)
    
    # Validate phone number format
    if not re.match(r'^\+?\d{10,15}$', phone_number):
        raise ValueError(ERROR_INVALID_PHONE)

    # Validate model
    if model not in ["base", "turbo", "enhanced"]:
        raise ValueError(ERROR_INVALID_MODEL)

    # Validate background track
    if background_track and background_track not in BACKGROUND_TRACKS:
        raise ValueError(f"Invalid background track. Must be one of: {', '.join(BACKGROUND_TRACKS.keys())}")

    # Prepare headers
    headers = {
        "authorization": auth_token,
        "Content-Type": "application/json"
    }

    if org_id:
        headers["organization"] = org_id

    # Build payload with all optional parameters
    payload = {
        "phone_number": phone_number
    }

    # Add optional parameters if provided
    optional_params = {
        "task": task,
        "pathway_id": pathway_id,
        "start_node_id": start_node_id,
        "voice": voice,
        "background_track": background_track,
        "first_sentence": first_sentence,
        "wait_for_greeting": wait_for_greeting,
        "block_interruptions": block_interruptions,
        "interruption_threshold": interruption_threshold,
        "model": model,
        "temperature": temperature,
        "keywords": keywords,
        "pronunciation_guide": pronunciation_guide,
        "transfer_phone_number": transfer_phone_number,
        "transfer_list": transfer_list,
        "language": language,
        "timezone": timezone,
        "request_data": request_data,
        "tools": tools,
        "dynamic_data": dynamic_data,
        "start_time": start_time,
        "voicemail_message": voicemail_message,
        "voicemail_action": voicemail_action,
        "retry": retry,
        "max_duration": max_duration,
        "record": record,
        "from": from_number,
        "webhook": webhook,
        "webhook_events": webhook_events,
        "metadata": metadata,
        "summary_prompt": summary_prompt,
        "analysis_prompt": analysis_prompt,
        "analysis_schema": analysis_schema,
        "answered_by_enabled": answered_by_enabled
    }

    # Add non-None optional parameters to payload
    payload.update({k: v for k, v in optional_params.items() if v is not None})

    try:
        # Make API request
        response = requests.post(
            CALLS_ENDPOINT,
            headers=headers,
            json=payload
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
        # Example with minimal parameters
        result_simple = send_call(
            auth_token=API_KEY,
            phone_number=DEFAULT_PHONE,
            task="This is a test call with minimal parameters",
            org_id=ORG_ID
        )
        print("Simple API Response:", result_simple)

        # Example with more parameters
        result_complex = send_call(
            auth_token=API_KEY,
            phone_number=DEFAULT_PHONE,
            task="This is a test call with additional parameters",
            voice="maya",
            background_track="office",
            first_sentence="Hello! This is a test call.",
            wait_for_greeting=True,
            max_duration=5,
            record=True,
            metadata={"test_type": "comprehensive"},
            org_id=ORG_ID
        )
        print("\nComplex API Response:", result_complex)
        
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 