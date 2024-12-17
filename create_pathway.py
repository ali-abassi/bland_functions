import requests
from typing import Dict, Any, List, Optional
from config import (
    CREATE_PATHWAY_ENDPOINT,
    ERROR_MISSING_AUTH,
    ERROR_MISSING_PATHWAY_NAME,
    ERROR_MISSING_NODES,
    ERROR_MISSING_EDGES,
    API_KEY
)

def create_pathway(
    auth_token: str,
    name: str,
    nodes: List[Dict[str, Any]],
    edges: List[Dict[str, Any]],
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Create a new conversation pathway.
    
    Args:
        auth_token (str): Your API authentication token
        name (str): Name of the pathway
        nodes (List[Dict]): Array of node objects, each containing:
            - id: Node identifier
            - type: Node type (default, webhook, etc.)
            - data: Node configuration data
            - position: Visual position data
        edges (List[Dict]): Array of edge objects, each containing:
            - id: Edge identifier
            - source: Source node ID
            - target: Target node ID
            - label: Connection label/condition
        description (str, optional): Description of the pathway
        metadata (dict, optional): Additional metadata for the pathway
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing:
            - status: Success/error status
            - pathway_id: ID of the created pathway
            - message: Status message
            
    Raises:
        ValueError: If required parameters are missing or invalid
    """
    # Validate required parameters
    if not auth_token:
        raise ValueError(ERROR_MISSING_AUTH)
    if not name:
        raise ValueError(ERROR_MISSING_PATHWAY_NAME)
    if not nodes:
        raise ValueError(ERROR_MISSING_NODES)
    if not edges:
        raise ValueError(ERROR_MISSING_EDGES)

    # Prepare headers
    headers = {
        "authorization": auth_token,
        "Content-Type": "application/json"
    }

    if org_id:
        headers["encrypted_key"] = org_id

    # Prepare payload
    payload = {
        "name": name,
        "nodes": nodes,
        "edges": edges
    }

    # Add optional parameters
    if description:
        payload["description"] = description
    if metadata:
        payload["metadata"] = metadata

    try:
        # Make API request
        response = requests.post(
            CREATE_PATHWAY_ENDPOINT,
            headers=headers,
            json=payload
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
        # Example pathway with two nodes and one edge
        test_nodes = [
            {
                "id": "start",
                "type": "default",
                "data": {
                    "prompt": "Hello! This is a test pathway. How can I help you today?"
                },
                "position": {"x": 0, "y": 0}
            },
            {
                "id": "end",
                "type": "default",
                "data": {
                    "prompt": "Thank you for testing the pathway. Goodbye!"
                },
                "position": {"x": 200, "y": 0}
            }
        ]
        
        test_edges = [
            {
                "id": "edge1",
                "source": "start",
                "target": "end",
                "label": "default"
            }
        ]
        
        result = create_pathway(
            auth_token=API_KEY,
            name="Test Pathway",
            nodes=test_nodes,
            edges=test_edges,
            description="A simple test pathway",
            metadata={"version": "1.0", "type": "test"}
        )
        
        if result.get("status") == "success":
            print("Pathway created successfully!")
            print(f"Pathway ID: {result.get('pathway_id')}")
            print(f"Message: {result.get('message')}")
        else:
            print("Error:", result.get("message"))
        
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 