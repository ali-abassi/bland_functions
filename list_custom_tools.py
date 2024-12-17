import requests
from typing import Dict, Any, Optional, List
from config import (
    LIST_CUSTOM_TOOLS_ENDPOINT,
    ERROR_MISSING_AUTH,
    API_KEY
)

def list_custom_tools(
    auth_token: str,
    page: Optional[int] = 1,
    limit: Optional[int] = 10,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    List all custom tools with pagination support.
    
    Args:
        auth_token (str): Your API authentication token
        page (int, optional): Page number for pagination (default: 1)
        limit (int, optional): Number of tools per page (default: 10)
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing:
            - tools: List of custom tool objects
            - total: Total number of tools
            - page: Current page number
            - total_pages: Total number of pages
            
    Raises:
        ValueError: If required parameters are missing or invalid
    """
    # Validate required parameters
    if not auth_token:
        raise ValueError(ERROR_MISSING_AUTH)

    # Validate pagination parameters
    if page < 1:
        raise ValueError("Page number must be greater than 0")
    if limit < 1:
        raise ValueError("Limit must be greater than 0")

    # Prepare headers
    request_headers = {
        "authorization": auth_token,
        "Content-Type": "application/json"
    }

    if org_id:
        request_headers["encrypted_key"] = org_id

    # Prepare query parameters
    params = {
        "page": page,
        "limit": limit
    }

    try:
        # Make API request
        response = requests.get(
            LIST_CUSTOM_TOOLS_ENDPOINT,
            headers=request_headers,
            params=params
        )
        response.raise_for_status()
        
        return response.json()
        
    except requests.exceptions.RequestException as e:
        return {
            "status": "error",
            "message": str(e),
            "tools": [],
            "total": 0,
            "page": page,
            "total_pages": 0
        }

def format_tool_info(tool: Dict[str, Any]) -> str:
    """Helper function to format tool information for display"""
    return (
        f"Tool ID: {tool.get('id')}\n"
        f"Name: {tool.get('name')}\n"
        f"Description: {tool.get('description')}\n"
        f"Endpoint: {tool.get('endpoint')}\n"
        f"Method: {tool.get('method')}\n"
        f"Created: {tool.get('created_at')}\n"
        f"Last Updated: {tool.get('updated_at')}\n"
        "-------------------"
    )

if __name__ == "__main__":
    # Test the function using config values
    try:
        # Get pagination parameters
        page = int(input("Enter page number (default: 1): ") or "1")
        limit = int(input("Enter items per page (default: 10): ") or "10")
        
        result = list_custom_tools(
            auth_token=API_KEY,
            page=page,
            limit=limit
        )
        
        if result.get("status") != "error":
            tools = result.get("tools", [])
            total = result.get("total", 0)
            total_pages = result.get("total_pages", 0)
            
            print(f"\nShowing page {page} of {total_pages} ({total} total tools)")
            print("===================")
            
            for tool in tools:
                print(format_tool_info(tool))
        else:
            print("Error:", result.get("message"))
            
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 