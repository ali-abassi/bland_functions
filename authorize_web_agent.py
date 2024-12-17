import requests
from typing import Dict, Any, Optional, List, Union
from config import (
    API_BASE_URL,
    API_VERSION,
    ERROR_MISSING_AUTH,
    API_KEY
)

# Define the endpoint
AUTHORIZE_WEB_AGENT_ENDPOINT = f"{API_BASE_URL}/{API_VERSION}/web-agents/{{agent_id}}/authorize"

def authorize_web_agent(
    auth_token: str,
    agent_id: str,
    call_id: str,
    action: str,
    target_url: str,
    parameters: Optional[Dict[str, Any]] = None,
    context: Optional[Dict[str, Any]] = None,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Authorize a web agent to perform a specific action during a call.
    
    Args:
        auth_token (str): Your API authentication token
        agent_id (str): ID of the web agent to authorize
        call_id (str): ID of the call requesting authorization
        action (str): Action to authorize (e.g., "click", "type", "navigate")
        target_url (str): URL where the action will be performed
        parameters (dict, optional): Additional parameters for the action
        context (dict, optional): Additional context about the request
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing:
            - status: Success/error status
            - authorized: Boolean indicating if the action is authorized
            - message: Status message
            
    Raises:
        ValueError: If required parameters are missing or invalid
    """
    # Validate required parameters
    if not auth_token:
        raise ValueError(ERROR_MISSING_AUTH)
    if not agent_id:
        raise ValueError("Missing required parameter: agent_id")
    if not call_id:
        raise ValueError("Missing required parameter: call_id")
    if not action:
        raise ValueError("Missing required parameter: action")
    if not target_url:
        raise ValueError("Missing required parameter: target_url")

    # Prepare headers
    headers = {
        "authorization": auth_token,
        "Content-Type": "application/json"
    }

    if org_id:
        headers["encrypted_key"] = org_id

    # Prepare request data
    data = {
        "call_id": call_id,
        "action": action,
        "target_url": target_url
    }

    # Add optional parameters if provided
    if parameters is not None:
        data["parameters"] = parameters
    if context is not None:
        data["context"] = context

    try:
        # Make API request
        response = requests.post(
            AUTHORIZE_WEB_AGENT_ENDPOINT.format(agent_id=agent_id),
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
        # Get required information
        agent_id = input("Enter agent ID: ")
        call_id = input("Enter call ID: ")
        
        # Example authorization request
        auth_request = {
            "action": "click",
            "target_url": "https://example.com/submit",
            "parameters": {
                "element_id": "submit-button",
                "element_type": "button",
                "verification_required": True
            },
            "context": {
                "previous_action": "form_fill",
                "session_duration": 300,
                "user_consent": True
            }
        }
        
        result = authorize_web_agent(
            auth_token=API_KEY,
            agent_id=agent_id,
            call_id=call_id,
            **auth_request
        )
        
        if result.get("status") == "success":
            authorized = result.get("authorized", False)
            print(f"Authorization {'granted' if authorized else 'denied'}")
            print(f"Message: {result.get('message')}")
        else:
            print("Error:", result.get("message"))
            
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 