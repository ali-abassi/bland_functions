import requests
from typing import Dict, Any, Optional, List, Union
from config import (
    CUSTOM_TOOLS_ENDPOINT,
    ERROR_MISSING_AUTH,
    API_KEY
)

def create_custom_tool(
    auth_token: str,
    name: str,
    description: str,
    endpoint: str,
    method: str,
    parameters: List[Dict[str, Any]],
    headers: Optional[Dict[str, str]] = None,
    authentication: Optional[Dict[str, str]] = None,
    response_mapping: Optional[Dict[str, str]] = None,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Create a custom tool for use in calls.
    
    Args:
        auth_token (str): Your API authentication token
        name (str): Name of the custom tool
        description (str): Description of what the tool does
        endpoint (str): API endpoint URL for the tool
        method (str): HTTP method (GET, POST, PUT, DELETE)
        parameters (list): List of parameter objects defining the tool's inputs
        headers (dict, optional): Custom headers for the tool's requests
        authentication (dict, optional): Authentication configuration
        response_mapping (dict, optional): Mapping of API response to tool output
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing:
            - status: Success/error status
            - tool_id: ID of the created tool
            - message: Status message
            
    Raises:
        ValueError: If required parameters are missing
    """
    # Validate required parameters
    if not auth_token:
        raise ValueError(ERROR_MISSING_AUTH)
    if not name:
        raise ValueError("Missing required parameter: name")
    if not description:
        raise ValueError("Missing required parameter: description")
    if not endpoint:
        raise ValueError("Missing required parameter: endpoint")
    if not method:
        raise ValueError("Missing required parameter: method")
    if not parameters:
        raise ValueError("Missing required parameter: parameters")

    # Validate method
    valid_methods = ["GET", "POST", "PUT", "DELETE"]
    if method.upper() not in valid_methods:
        raise ValueError(f"Invalid method. Must be one of: {', '.join(valid_methods)}")

    # Prepare headers
    request_headers = {
        "authorization": auth_token,
        "Content-Type": "application/json"
    }

    if org_id:
        request_headers["encrypted_key"] = org_id

    # Prepare request data
    data = {
        "name": name,
        "description": description,
        "endpoint": endpoint,
        "method": method.upper(),
        "parameters": parameters
    }
    
    if headers:
        data["headers"] = headers
    if authentication:
        data["authentication"] = authentication
    if response_mapping:
        data["response_mapping"] = response_mapping

    try:
        # Make API request
        response = requests.post(
            CUSTOM_TOOLS_ENDPOINT,
            headers=request_headers,
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
        # Example tool configuration
        tool_config = {
            "name": "Weather API Tool",
            "description": "Get current weather information for a location",
            "endpoint": "https://api.weather.example.com/v1/current",
            "method": "GET",
            "parameters": [
                {
                    "name": "location",
                    "type": "string",
                    "description": "City name or coordinates",
                    "required": True
                },
                {
                    "name": "units",
                    "type": "string",
                    "description": "Temperature units (celsius/fahrenheit)",
                    "required": False,
                    "default": "celsius"
                }
            ],
            "headers": {
                "Accept": "application/json"
            },
            "authentication": {
                "type": "api_key",
                "header_name": "X-API-Key"
            },
            "response_mapping": {
                "temperature": "current.temp",
                "conditions": "current.conditions"
            }
        }
        
        # Confirm creation
        confirm = input(f"Create custom tool '{tool_config['name']}'? (y/N): ")
        
        if confirm.lower() == 'y':
            result = create_custom_tool(
                auth_token=API_KEY,
                **tool_config
            )
            
            if result.get("status") == "success":
                print("Custom tool created successfully!")
                print(f"Tool ID: {result.get('tool_id')}")
                print(f"Message: {result.get('message')}")
            else:
                print("Error:", result.get("message"))
        else:
            print("Creation cancelled")
            
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 