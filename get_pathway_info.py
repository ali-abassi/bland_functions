import requests
from typing import Dict, Any, Optional
from config import (
    PATHWAY_DETAILS_ENDPOINT,
    ERROR_MISSING_AUTH,
    ERROR_MISSING_PATHWAY,
    API_KEY,
    PATHWAY_ID
)

def get_pathway_info(
    auth_token: str,
    pathway_id: str,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Retrieve detailed information about a specific pathway.
    
    Args:
        auth_token (str): Your API authentication token
        pathway_id (str): The unique identifier of the pathway
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing:
            - pathway_id: Unique identifier
            - name: Pathway name
            - description: Pathway description
            - created_at: Creation timestamp
            - updated_at: Last update timestamp
            - version: Current version
            - status: Active/inactive status
            - nodes: Array of pathway nodes, each containing:
                - id: Node identifier
                - type: Node type (default, webhook, etc.)
                - data: Node configuration data
                - position: Visual position data
            - edges: Array of node connections, each containing:
                - id: Edge identifier
                - source: Source node ID
                - target: Target node ID
                - label: Connection label/condition
            - metadata: Additional pathway metadata
            
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
        "authorization": auth_token
    }

    if org_id:
        headers["encrypted_key"] = org_id

    try:
        # Make API request
        response = requests.get(
            PATHWAY_DETAILS_ENDPOINT.format(pathway_id=pathway_id),
            headers=headers
        )
        response.raise_for_status()
        
        return response.json()
        
    except requests.exceptions.RequestException as e:
        return {
            "status": "error",
            "message": str(e)
        }

def format_node_info(node: Dict[str, Any]) -> str:
    """Helper function to format node information"""
    formatted = []
    formatted.append(f"Node: {node.get('id', 'N/A')}")
    formatted.append(f"Type: {node.get('type', 'default')}")
    
    # Add node data if available
    data = node.get('data', {})
    if data:
        formatted.append("Data:")
        if data.get('prompt'):
            formatted.append(f"  Prompt: {data['prompt'][:100]}...")
        if data.get('webhook_url'):
            formatted.append(f"  Webhook: {data['webhook_url']}")
        if data.get('condition'):
            formatted.append(f"  Condition: {data['condition']}")
    
    return "\n  ".join(formatted)

def format_edge_info(edge: Dict[str, Any]) -> str:
    """Helper function to format edge information"""
    return (f"Connection: {edge.get('source', 'N/A')} -> {edge.get('target', 'N/A')}\n"
            f"  Label: {edge.get('label', 'N/A')}")

if __name__ == "__main__":
    # Test the function using config values
    try:
        result = get_pathway_info(
            auth_token=API_KEY,
            pathway_id=PATHWAY_ID
        )
        
        if isinstance(result, dict) and result.get("status") != "error":
            print("Pathway Information:")
            print("-" * 40)
            print(f"Name: {result.get('name', 'N/A')}")
            print(f"ID: {result.get('pathway_id', 'N/A')}")
            print(f"Version: {result.get('version', 'N/A')}")
            print(f"Status: {result.get('status', 'N/A')}")
            print(f"Created: {result.get('created_at', 'N/A')}")
            print(f"Last Updated: {result.get('updated_at', 'N/A')}")
            
            if result.get('description'):
                print(f"\nDescription: {result['description']}")
            
            # Print nodes
            nodes = result.get('nodes', [])
            if nodes:
                print("\nNodes:")
                for node in nodes:
                    print(format_node_info(node))
            
            # Print edges
            edges = result.get('edges', [])
            if edges:
                print("\nConnections:")
                for edge in edges:
                    print(format_edge_info(edge))
            
            # Print metadata
            metadata = result.get('metadata', {})
            if metadata:
                print("\nMetadata:")
                for key, value in metadata.items():
                    print(f"  {key}: {value}")
            
            print("-" * 40)
        else:
            print("Error:", result.get("message"))
        
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 