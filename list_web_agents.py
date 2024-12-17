import requests
from typing import Dict, Any, Optional, List
from config import (
    API_BASE_URL,
    API_VERSION,
    ERROR_MISSING_AUTH,
    DEFAULT_LIMIT,
    API_KEY
)

# Define the endpoint
WEB_AGENTS_ENDPOINT = f"{API_BASE_URL}/{API_VERSION}/web-agents"

def list_web_agents(
    auth_token: str,
    limit: Optional[int] = DEFAULT_LIMIT,
    offset: Optional[int] = 0,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    List all web agents with pagination support.
    
    Args:
        auth_token (str): Your API authentication token
        limit (int, optional): Maximum number of agents to return (default: 1000)
        offset (int, optional): Number of agents to skip (default: 0)
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing:
            - status: Success/error status
            - agents: List of web agent objects
            - total: Total number of agents
            - message: Status message
            
    Raises:
        ValueError: If required parameters are missing or invalid
    """
    # Validate required parameters
    if not auth_token:
        raise ValueError(ERROR_MISSING_AUTH)
    
    # Validate pagination parameters
    if limit is not None and limit < 1:
        raise ValueError("Limit must be greater than 0")
    if offset is not None and offset < 0:
        raise ValueError("Offset must be greater than or equal to 0")

    # Prepare headers
    headers = {
        "authorization": auth_token
    }

    if org_id:
        headers["encrypted_key"] = org_id

    # Prepare query parameters
    params = {}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset

    try:
        # Make API request
        response = requests.get(
            WEB_AGENTS_ENDPOINT,
            headers=headers,
            params=params
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
        # Example: List first 10 web agents
        result = list_web_agents(
            auth_token=API_KEY,
            limit=10
        )
        
        if result.get("status") == "success":
            agents = result.get("agents", [])
            total = result.get("total", 0)
            
            print(f"Found {total} web agents:")
            for agent in agents:
                print(f"\nAgent ID: {agent.get('id')}")
                print(f"Name: {agent.get('name')}")
                print(f"Description: {agent.get('description')}")
                print(f"Website URL: {agent.get('website_url')}")
                print(f"Capabilities: {', '.join(agent.get('capabilities', []))}")
        else:
            print("Error:", result.get("message"))
            
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 