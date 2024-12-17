import requests
from typing import Dict, Any, List, Optional
from config import (
    UPDATE_PATHWAY_ENDPOINT,
    ERROR_MISSING_AUTH,
    ERROR_MISSING_PATHWAY,
    API_KEY,
    PATHWAY_ID
)

def update_pathway(
    auth_token: str,
    pathway_id: str,
    name: Optional[str] = None,
    nodes: Optional[List[Dict[str, Any]]] = None,
    edges: Optional[List[Dict[str, Any]]] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Update an existing conversation pathway.
    
    Args:
        auth_token (str): Your API authentication token
        pathway_id (str): ID of the pathway to update
        name (str, optional): New name for the pathway
        nodes (List[Dict], optional): Updated array of node objects
        edges (List[Dict], optional): Updated array of edge objects
        description (str, optional): New description for the pathway
        metadata (dict, optional): Updated metadata for the pathway
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing:
            - status: Success/error status
            - pathway_id: ID of the updated pathway
            - message: Status message
            
    Raises:
        ValueError: If required parameters are missing or no updates provided
    """
    # Validate required parameters
    if not auth_token:
        raise ValueError(ERROR_MISSING_AUTH)
    if not pathway_id:
        raise ValueError(ERROR_MISSING_PATHWAY)
    
    # Ensure at least one update parameter is provided
    if not any([name, nodes, edges, description, metadata]):
        raise ValueError("At least one update parameter must be provided")

    # Prepare headers
    headers = {
        "authorization": auth_token,
        "Content-Type": "application/json"
    }

    if org_id:
        headers["encrypted_key"] = org_id

    # Prepare payload with only provided updates
    payload = {}
    if name:
        payload["name"] = name
    if nodes:
        payload["nodes"] = nodes
    if edges:
        payload["edges"] = edges
    if description:
        payload["description"] = description
    if metadata:
        payload["metadata"] = metadata

    try:
        # Make API request
        response = requests.post(
            UPDATE_PATHWAY_ENDPOINT.format(pathway_id=pathway_id),
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
        # Example 1: Update pathway name and description
        result_simple = update_pathway(
            auth_token=API_KEY,
            pathway_id=PATHWAY_ID,
            name="Updated Test Pathway",
            description="Updated pathway description"
        )
        print("Simple Update Response:", result_simple)

        # Example 2: Update pathway with new nodes and edges
        test_nodes = [
            {
                "id": "start",
                "type": "default",
                "data": {
                    "prompt": "Updated greeting message. How can I assist you?"
                },
                "position": {"x": 0, "y": 0}
            },
            {
                "id": "middle",
                "type": "default",
                "data": {
                    "prompt": "Processing your request..."
                },
                "position": {"x": 100, "y": 0}
            },
            {
                "id": "end",
                "type": "default",
                "data": {
                    "prompt": "Thank you for your time. Have a great day!"
                },
                "position": {"x": 200, "y": 0}
            }
        ]
        
        test_edges = [
            {
                "id": "edge1",
                "source": "start",
                "target": "middle",
                "label": "default"
            },
            {
                "id": "edge2",
                "source": "middle",
                "target": "end",
                "label": "default"
            }
        ]
        
        result_complex = update_pathway(
            auth_token=API_KEY,
            pathway_id=PATHWAY_ID,
            nodes=test_nodes,
            edges=test_edges,
            metadata={"version": "2.0", "updated": True}
        )
        print("\nComplex Update Response:", result_complex)
        
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 