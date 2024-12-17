import requests
from typing import Dict, Any, Optional
from config import (
    PATHWAYS_ENDPOINT,
    ERROR_MISSING_AUTH,
    ERROR_NO_PATHWAYS,
    API_KEY,
    DEFAULT_LIMIT
)

def get_all_pathways(
    auth_token: str,
    limit: int = DEFAULT_LIMIT,
    offset: int = 0,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Retrieve a list of all available pathways with optional pagination.
    
    Args:
        auth_token (str): Your API authentication token
        limit (int, optional): Maximum number of pathways to return (default: 1000)
        offset (int, optional): Number of pathways to skip (for pagination)
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing:
            - total_count: Total number of pathways
            - pathways: Array of pathway objects, each containing:
                - pathway_id: Unique identifier
                - name: Pathway name
                - description: Pathway description
                - created_at: Creation timestamp
                - updated_at: Last update timestamp
                - version: Current version
                - status: Active/inactive status
                - nodes: Array of pathway nodes
                - edges: Array of node connections
                - metadata: Additional pathway metadata
            
    Raises:
        ValueError: If required parameters are missing
    """
    # Validate required parameters
    if not auth_token:
        raise ValueError(ERROR_MISSING_AUTH)

    # Prepare headers
    headers = {
        "authorization": auth_token
    }

    if org_id:
        headers["encrypted_key"] = org_id

    # Prepare query parameters
    params = {
        'limit': limit,
        'offset': offset
    }

    try:
        # Make API request
        response = requests.get(
            PATHWAYS_ENDPOINT,
            headers=headers,
            params=params
        )
        response.raise_for_status()
        
        # Check if pathways exist
        data = response.json()
        if not data.get('pathways'):
            raise RuntimeError(ERROR_NO_PATHWAYS)
            
        return data
        
    except requests.exceptions.RequestException as e:
        return {
            "status": "error",
            "message": str(e)
        }

def format_pathway_info(pathway: Dict[str, Any]) -> str:
    """Helper function to format pathway information for display"""
    formatted = []
    formatted.append(f"Pathway: {pathway.get('name', 'N/A')}")
    formatted.append(f"ID: {pathway.get('pathway_id', 'N/A')}")
    formatted.append(f"Version: {pathway.get('version', 'N/A')}")
    formatted.append(f"Status: {pathway.get('status', 'N/A')}")
    formatted.append(f"Created: {pathway.get('created_at', 'N/A')}")
    formatted.append(f"Last Updated: {pathway.get('updated_at', 'N/A')}")
    
    if pathway.get('description'):
        formatted.append(f"\nDescription: {pathway['description']}")
    
    # Add node count
    nodes = pathway.get('nodes', [])
    formatted.append(f"\nNodes: {len(nodes)}")
    
    # Add edge count
    edges = pathway.get('edges', [])
    formatted.append(f"Connections: {len(edges)}")
    
    # Add metadata if available
    metadata = pathway.get('metadata', {})
    if metadata:
        formatted.append("\nMetadata:")
        for key, value in metadata.items():
            formatted.append(f"  {key}: {value}")
    
    return "\n".join(formatted)

if __name__ == "__main__":
    # Test the function using config values
    try:
        # Get first page of pathways
        result = get_all_pathways(
            auth_token=API_KEY,
            limit=5  # Get first 5 pathways for testing
        )
        
        if isinstance(result, dict) and result.get("status") != "error":
            pathways = result.get('pathways', [])
            print(f"Total Pathways: {result.get('total_count', 0)}")
            
            print("\nPathway Details:")
            for pathway in pathways:
                print("-" * 40)
                print(format_pathway_info(pathway))
            print("-" * 40)
        else:
            print("Error:", result.get("message"))
        
    except ValueError as e:
        print("Validation Error:", str(e))
    except RuntimeError as e:
        print("Runtime Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 