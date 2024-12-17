import requests
from typing import Dict, Any, Optional, List, Union
from config import (
    API_BASE_URL,
    API_VERSION,
    ERROR_MISSING_AUTH,
    API_KEY
)

# Define the endpoint
WEB_AGENTS_ENDPOINT = f"{API_BASE_URL}/{API_VERSION}/web-agents"

def create_web_agent(
    auth_token: str,
    name: str,
    description: str,
    website_url: str,
    allowed_domains: List[str],
    capabilities: Optional[List[str]] = None,
    authentication: Optional[Dict[str, Any]] = None,
    custom_headers: Optional[Dict[str, str]] = None,
    rate_limit: Optional[int] = None,
    max_pages: Optional[int] = None,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Create a new web agent for automated web interactions.
    
    Args:
        auth_token (str): Your API authentication token
        name (str): Name of the web agent
        description (str): Description of what the web agent does
        website_url (str): Base URL of the website to interact with
        allowed_domains (list): List of domains the agent is allowed to access
        capabilities (list, optional): List of agent capabilities (e.g., ["click", "type", "scroll"])
        authentication (dict, optional): Website authentication configuration
        custom_headers (dict, optional): Custom HTTP headers for requests
        rate_limit (int, optional): Maximum requests per minute
        max_pages (int, optional): Maximum number of pages to visit per session
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing:
            - status: Success/error status
            - agent_id: ID of the created web agent
            - message: Status message
            
    Raises:
        ValueError: If required parameters are missing or invalid
    """
    # Validate required parameters
    if not auth_token:
        raise ValueError(ERROR_MISSING_AUTH)
    if not name:
        raise ValueError("Missing required parameter: name")
    if not description:
        raise ValueError("Missing required parameter: description")
    if not website_url:
        raise ValueError("Missing required parameter: website_url")
    if not allowed_domains:
        raise ValueError("Missing required parameter: allowed_domains")

    # Prepare headers
    headers = {
        "authorization": auth_token,
        "Content-Type": "application/json"
    }

    if org_id:
        headers["encrypted_key"] = org_id

    # Prepare request data
    data = {
        "name": name,
        "description": description,
        "website_url": website_url,
        "allowed_domains": allowed_domains
    }

    # Add optional parameters if provided
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
            WEB_AGENTS_ENDPOINT,
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
        # Example web agent configuration
        agent_config = {
            "name": "Test Web Agent",
            "description": "A test web agent for automated web interactions",
            "website_url": "https://example.com",
            "allowed_domains": ["example.com", "api.example.com"],
            "capabilities": ["click", "type", "scroll", "extract"],
            "rate_limit": 60,
            "max_pages": 100,
            "custom_headers": {
                "User-Agent": "BlandAI Web Agent/1.0"
            }
        }
        
        result = create_web_agent(
            auth_token=API_KEY,
            **agent_config
        )
        
        if result.get("status") == "success":
            print("Web agent created successfully!")
            print(f"Agent ID: {result.get('agent_id')}")
            print(f"Message: {result.get('message')}")
        else:
            print("Error:", result.get("message"))
            
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 