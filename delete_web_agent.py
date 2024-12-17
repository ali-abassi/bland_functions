import requests
from typing import Dict, Any, Optional
from config import (
    API_BASE_URL,
    API_VERSION,
    ERROR_MISSING_AUTH,
    API_KEY
)

# Define the endpoint
DELETE_WEB_AGENT_ENDPOINT = f"{API_BASE_URL}/{API_VERSION}/web-agents/{{agent_id}}/delete"

def delete_web_agent(
    auth_token: str,
    agent_id: str,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Delete an existing web agent.
    
    Args:
        auth_token (str): Your API authentication token
        agent_id (str): ID of the web agent to delete
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
    if not agent_id:
        raise ValueError("Missing required parameter: agent_id")

    # Prepare headers
    headers = {
        "authorization": auth_token
    }

    if org_id:
        headers["encrypted_key"] = org_id

    try:
        # Make API request
        response = requests.delete(
            DELETE_WEB_AGENT_ENDPOINT.format(agent_id=agent_id),
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
        # Get agent ID from user
        agent_id = input("Enter agent ID to delete: ")
        
        # Confirm deletion
        confirm = input(f"Are you sure you want to delete web agent {agent_id}? (y/N): ")
        
        if confirm.lower() == 'y':
            result = delete_web_agent(
                auth_token=API_KEY,
                agent_id=agent_id
            )
            
            if result.get("status") == "success":
                print("Web agent deleted successfully!")
                print(f"Message: {result.get('message')}")
            else:
                print("Error:", result.get("message"))
        else:
            print("Deletion cancelled")
            
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 