import requests
from typing import Dict, Any, Optional
from config import (
    PATHWAY_CHAT_CREATE_ENDPOINT,
    ERROR_MISSING_AUTH,
    ERROR_MISSING_PATHWAY,
    API_KEY,
    PATHWAY_ID
)

def create_pathway_chat(
    auth_token: str,
    pathway_id: str,
    start_node_id: Optional[str] = None,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Create an instance of a pathway chat, which can be used to send and receive messages to the pathway.
    
    Args:
        auth_token (str): Your API authentication token
        pathway_id (str): Pathway ID of the pathway to create a chat instance for
        start_node_id (str, optional): The start node ID of the pathway
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing:
            - status: Success/error status
            - chat_id: The ID of the chat instance created
            - message: Status message
            
    Raises:
        ValueError: If required parameters are missing
    """
    # Validate required parameters
    if not auth_token:
        raise ValueError(ERROR_MISSING_AUTH)
    if not pathway_id:
        raise ValueError(ERROR_MISSING_PATHWAY)

    # Prepare headers
    headers = {
        "authorization": auth_token,
        "Content-Type": "application/json"
    }

    if org_id:
        headers["encrypted_key"] = org_id

    # Prepare request data
    data = {
        "pathway_id": pathway_id
    }
    
    if start_node_id:
        data["start_node_id"] = start_node_id

    try:
        # Make API request
        response = requests.post(
            PATHWAY_CHAT_CREATE_ENDPOINT,
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
        result = create_pathway_chat(
            auth_token=API_KEY,
            pathway_id=PATHWAY_ID
        )
        
        if result.get("status") == "success":
            print("Chat instance created successfully!")
            print(f"Chat ID: {result.get('chat_id')}")
            print(f"Message: {result.get('message')}")
        else:
            print("Error:", result.get("message"))
            
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 