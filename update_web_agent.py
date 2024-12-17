import requests
from typing import Dict, Any, Optional, List, Union
from config import (
    API_BASE_URL,
    API_VERSION,
    ERROR_MISSING_AUTH,
    API_KEY
)

# Define the endpoint
UPDATE_WEB_AGENT_ENDPOINT = f"{API_BASE_URL}/{API_VERSION}/web-agents/{{agent_id}}/update"

def update_web_agent(
    auth_token: str,
    agent_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    website_url: Optional[str] = None,
    allowed_domains: Optional[List[str]] = None,
    capabilities: Optional[List[str]] = None,
    authentication: Optional[Dict[str, Any]] = None,
    custom_headers: Optional[Dict[str, str]] = None,
    rate_limit: Optional[int] = None,
    max_pages: Optional[int] = None,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Update an existing web agent's configuration.
    
    Args:
        auth_token (str): Your API authentication token
        agent_id (str): ID of the web agent to update
        name (str, optional): New name for the web agent
        description (str, optional): New description of what the web agent does
        website_url (str, optional): New base URL of the website to interact with
        allowed_domains (list, optional): New list of domains the agent is allowed to access
        capabilities (list, optional): New list of agent capabilities
        authentication (dict, optional): New website authentication configuration
        custom_headers (dict, optional): New custom HTTP headers for requests
        rate_limit (int, optional): New maximum requests per minute
        max_pages (int, optional): New maximum number of pages to visit per session
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing:
            - status: Success/error status
            - message: Status message
            
    Raises:
        ValueError: If required parameters are missing or invalid
    """
    # Validate required parameters
    if not auth_token:
        raise ValueError(ERROR_MISSING_AUTH)
    if not agent_id:
        raise ValueError("Missing required parameter: agent_id")

    # Prepare headers
    headers = {
        "authorization": auth_token,
        "Content-Type": "application/json"
    }

    if org_id:
        headers["encrypted_key"] = org_id

    # Prepare request data (only include provided fields)
    data = {}
    if name is not None:
        data["name"] = name
    if description is not None:
        data["description"] = description
    if website_url is not None:
        data["website_url"] = website_url
    if allowed_domains is not None:
        data["allowed_domains"] = allowed_domains
    if capabilities is not None:
        data["capabilities"] = capabilities
    if authentication is not None:
        data["authentication"] = authentication
    if custom_headers is not None:
        data["custom_headers"] = custom_headers
    if rate_limit is not None:
        data["rate_limit"] = rate_limit
    if max_pages is not None:
        data["max_pages"] = max_pages

    try:
        # Make API request
        response = requests.post(
            UPDATE_WEB_AGENT_ENDPOINT.format(agent_id=agent_id),
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
        # Get agent ID from user
        agent_id = input("Enter agent ID to update: ")
        
        # Example update configuration
        update_config = {
            "name": "Updated Web Agent",
            "description": "Updated web agent for automated interactions",
            "capabilities": ["click", "type", "scroll", "extract", "navigate"],
            "rate_limit": 120,
            "max_pages": 200,
            "custom_headers": {
                "User-Agent": "BlandAI Web Agent/2.0"
            }
        }
        
        # Confirm update
        confirm = input(f"Update web agent '{agent_id}'? (y/N): ")
        
        if confirm.lower() == 'y':
            result = update_web_agent(
                auth_token=API_KEY,
                agent_id=agent_id,
                **update_config
            )
            
            if result.get("status") == "success":
                print("Web agent updated successfully!")
                print(f"Message: {result.get('message')}")
            else:
                print("Error:", result.get("message"))
        else:
            print("Update cancelled")
            
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 