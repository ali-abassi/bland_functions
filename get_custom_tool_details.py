import requests
from typing import Dict, Any, Optional
from config import (
    CUSTOM_TOOL_DETAILS_ENDPOINT,
    ERROR_MISSING_AUTH,
    API_KEY
)

def get_custom_tool_details(
    auth_token: str,
    tool_id: str,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Get detailed information about a specific custom tool.
    
    Args:
        auth_token (str): Your API authentication token
        tool_id (str): ID of the tool to retrieve details for
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing tool details including:
            - id: Tool ID
            - name: Tool name
            - description: Tool description
            - endpoint: API endpoint
            - method: HTTP method
            - parameters: List of parameter configurations
            - headers: Custom headers
            - authentication: Authentication settings
            - response_mapping: Response field mappings
            - created_at: Creation timestamp
            - updated_at: Last update timestamp
            
    Raises:
        ValueError: If required parameters are missing
    """
    # Validate required parameters
    if not auth_token:
        raise ValueError(ERROR_MISSING_AUTH)
    if not tool_id:
        raise ValueError("Missing required parameter: tool_id")

    # Prepare headers
    request_headers = {
        "authorization": auth_token,
        "Content-Type": "application/json"
    }

    if org_id:
        request_headers["encrypted_key"] = org_id

    try:
        # Make API request
        response = requests.get(
            CUSTOM_TOOL_DETAILS_ENDPOINT.format(tool_id=tool_id),
            headers=request_headers
        )
        response.raise_for_status()
        
        return response.json()
        
    except requests.exceptions.RequestException as e:
        return {
            "status": "error",
            "message": str(e)
        }

def format_parameter_info(param: Dict[str, Any]) -> str:
    """Helper function to format parameter information"""
    required = "Required" if param.get("required", False) else "Optional"
    default = f" (default: {param['default']})" if "default" in param else ""
    return (
        f"- {param['name']} ({param['type']}) - {required}{default}\n"
        f"  Description: {param.get('description', 'No description provided')}"
    )

def format_tool_details(tool: Dict[str, Any]) -> str:
    """Helper function to format complete tool details for display"""
    # Basic information
    details = [
        f"Tool ID: {tool.get('id')}",
        f"Name: {tool.get('name')}",
        f"Description: {tool.get('description')}",
        f"Endpoint: {tool.get('endpoint')}",
        f"Method: {tool.get('method')}",
        "",
        "Parameters:",
    ]
    
    # Parameters
    parameters = tool.get("parameters", [])
    if parameters:
        for param in parameters:
            details.append(format_parameter_info(param))
    else:
        details.append("  No parameters defined")
    
    # Headers
    details.append("")
    details.append("Headers:")
    header_items = [f"- {k}: {v}" for k, v in tool.get("headers", {}).items()]
    if header_items:
        details.extend(header_items)
    else:
        details.append("  No custom headers defined")
    
    # Authentication
    auth_config = tool.get("authentication", {})
    if auth_config:
        details.extend([
            "",
            "Authentication:",
            f"Type: {auth_config.get('type', 'Not specified')}",
            f"Location: {auth_config.get('location', 'Not specified')}"
        ])
    
    # Response mapping
    response_mapping = tool.get("response_mapping", {})
    if response_mapping:
        details.extend([
            "",
            "Response Mapping:",
            *(f"- {k} → {v}" for k, v in response_mapping.items())
        ])
    
    # Timestamps
    details.extend([
        "",
        f"Created: {tool.get('created_at')}",
        f"Last Updated: {tool.get('updated_at')}"
    ])
    
    return "\n".join(details)

if __name__ == "__main__":
    # Test the function using config values
    try:
        # Get tool ID
        tool_id = input("Enter tool ID to view details: ")
        
        result = get_custom_tool_details(
            auth_token=API_KEY,
            tool_id=tool_id
        )
        
        if result.get("status") != "error":
            print("\nTool Details")
            print("============")
            print(format_tool_details(result))
        else:
            print("Error:", result.get("message"))
            
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 