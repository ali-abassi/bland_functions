import requests
from typing import Dict, Any, Optional, List
from config import (
    PATHWAY_CHAT_ENDPOINT,
    ERROR_MISSING_AUTH,
    API_KEY,
    PATHWAY_ID
)

def send_pathway_chat_message(
    auth_token: str,
    chat_id: str,
    message: Optional[str] = None,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Send a message to a pathway chat instance and receive a response.
    
    Args:
        auth_token (str): Your API authentication token
        chat_id (str): The chat ID created from the create_pathway_chat endpoint
        message (str, optional): The message to send to the pathway
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing:
            - status: Success/error status
            - chat_id: The ID of the chat instance
            - assistant_response: The response from the Assistant
            - current_node_id: The ID of the current node
            - current_node_name: The name of the current node
            - chat_history: Array of message objects
            - pathway_id: The ID of the pathway
            
    Raises:
        ValueError: If required parameters are missing
    """
    # Validate required parameters
    if not auth_token:
        raise ValueError(ERROR_MISSING_AUTH)
    if not chat_id:
        raise ValueError("Missing required parameter: chat_id")

    # Prepare headers
    headers = {
        "authorization": auth_token,
        "Content-Type": "application/json"
    }

    if org_id:
        headers["encrypted_key"] = org_id

    # Prepare request data
    data = {}
    if message:
        data["message"] = message

    try:
        # Make API request
        response = requests.post(
            PATHWAY_CHAT_ENDPOINT.format(chat_id=chat_id),
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

def get_pathway_chat_history(
    auth_token: str,
    chat_id: str,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Get conversation history for a pathway chat.
    
    Args:
        auth_token (str): Your API authentication token
        chat_id (str): The chat ID created from the create_pathway_chat endpoint
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing:
            - errors: List of errors or null
            - data: Array of message objects for the conversation history
            
    Raises:
        ValueError: If required parameters are missing
    """
    # Validate required parameters
    if not auth_token:
        raise ValueError(ERROR_MISSING_AUTH)
    if not chat_id:
        raise ValueError("Missing required parameter: chat_id")

    # Prepare headers
    headers = {
        "authorization": auth_token
    }

    if org_id:
        headers["encrypted_key"] = org_id

    try:
        # Make API request
        response = requests.get(
            PATHWAY_CHAT_ENDPOINT.format(chat_id=chat_id),
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
    # Test the send message function
    try:
        # Example chat ID (you would get this from create_pathway_chat)
        chat_id = "example_chat_id"
        
        # Send a message
        result = send_pathway_chat_message(
            auth_token=API_KEY,
            chat_id=chat_id,
            message="Hello!"
        )
        
        if result.get("status") == "success":
            print("Message sent successfully!")
            print(f"Assistant Response: {result.get('assistant_response')}")
            print(f"Current Node: {result.get('current_node_name')}")
        else:
            print("Error:", result.get("message"))
            
        # Get chat history
        history = get_pathway_chat_history(
            auth_token=API_KEY,
            chat_id=chat_id
        )
        
        if not history.get("errors"):
            print("\nChat History:")
            for message in history.get("data", []):
                print(f"{message['role']}: {message['content']}")
        else:
            print("Error retrieving chat history:", history.get("errors"))
            
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 