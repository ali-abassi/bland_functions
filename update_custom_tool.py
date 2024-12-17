import requests
from typing import Dict, Any, Optional, List, Union
from config import (
    UPDATE_CUSTOM_TOOL_ENDPOINT,
    ERROR_MISSING_AUTH,
    API_KEY
)

def update_custom_tool(
    auth_token: str,
    tool_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    endpoint: Optional[str] = None,
    method: Optional[str] = None,
    parameters: Optional[List[Dict[str, Any]]] = None,
    headers: Optional[Dict[str, str]] = None,
    authentication: Optional[Dict[str, str]] = None,
    response_mapping: Optional[Dict[str, str]] = None,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Update an existing custom tool's configuration.
    
    Args:
        auth_token (str): Your API authentication token
        tool_id (str): ID of the tool to update
        name (str, optional): New name for the tool
        description (str, optional): New description of what the tool does
        endpoint (str, optional): New API endpoint URL
        method (str, optional): New HTTP method (GET, POST, PUT, DELETE)
        parameters (list, optional): New list of parameter objects
        headers (dict, optional): New custom headers for requests
        authentication (dict, optional): New authentication configuration
        response_mapping (dict, optional): New mapping of API response to tool output
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
    if not tool_id:
        raise ValueError("Missing required parameter: tool_id")

    # Validate method if provided
    if method:
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

    # Prepare request data (only include provided fields)
    data = {}
    if name is not None:
        data["name"] = name
    if description is not None:
        data["description"] = description
    if endpoint is not None:
        data["endpoint"] = endpoint
    if method is not None:
        data["method"] = method.upper()
    if parameters is not None:
        data["parameters"] = parameters
    if headers is not None:
        data["headers"] = headers
    if authentication is not None:
        data["authentication"] = authentication
    if response_mapping is not None:
        data["response_mapping"] = response_mapping

    try:
        # Make API request
        response = requests.post(
            UPDATE_CUSTOM_TOOL_ENDPOINT.format(tool_id=tool_id),
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
        # Example tool update configuration
        tool_id = input("Enter tool ID to update: ")
        update_config = {
            "name": "Updated Weather API Tool",
            "description": "Get detailed weather information for a location",
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
                },
                {
                    "name": "forecast_days",
                    "type": "integer",
                    "description": "Number of days to forecast",
                    "required": False,
                    "default": 1
                }
            ]
        }
        
        # Confirm update
        confirm = input(f"Update custom tool '{tool_id}'? (y/N): ")
        
        if confirm.lower() == 'y':
            result = update_custom_tool(
                auth_token=API_KEY,
                tool_id=tool_id,
                **update_config
            )
            
            if result.get("status") == "success":
                print("Custom tool updated successfully!")
                print(f"Message: {result.get('message')}")
            else:
                print("Error:", result.get("message"))
        else:
            print("Update cancelled")
            
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 