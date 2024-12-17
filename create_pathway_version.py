import requests
from typing import Dict, Any, Optional, List
from config import (
    CREATE_PATHWAY_VERSION_ENDPOINT,
    ERROR_MISSING_AUTH,
    ERROR_MISSING_PATHWAY,
    API_KEY,
    PATHWAY_ID
)

def create_pathway_version(
    auth_token: str,
    pathway_id: str,
    name: str,
    description: Optional[str] = None,
    nodes: Optional[List[Dict[str, Any]]] = None,
    edges: Optional[List[Dict[str, Any]]] = None,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Create a new version of a pathway.
    
    Args:
        auth_token (str): Your API authentication token
        pathway_id (str): ID of the pathway to create a version for
        name (str): Name of the new version
        description (str, optional): Description of the new version
        nodes (list, optional): Array of node configurations
        edges (list, optional): Array of edge configurations
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing:
            - status: Success/error status
            - version_id: ID of the created version
            - message: Status message
            
    Raises:
        ValueError: If required parameters are missing
    """
    # Validate required parameters
    if not auth_token:
        raise ValueError(ERROR_MISSING_AUTH)
    if not pathway_id:
        raise ValueError(ERROR_MISSING_PATHWAY)
    if not name:
        raise ValueError("Missing required parameter: name")

    # Prepare headers
    headers = {
        "authorization": auth_token,
        "Content-Type": "application/json"
    }

    if org_id:
        headers["encrypted_key"] = org_id

    # Prepare request data
    data = {
        "name": name
    }
    
    if description:
        data["description"] = description
    if nodes:
        data["nodes"] = nodes
    if edges:
        data["edges"] = edges

    try:
        # Make API request
        response = requests.post(
            CREATE_PATHWAY_VERSION_ENDPOINT.format(pathway_id=pathway_id),
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
        # Example version data
        version_name = "Test Version"
        version_description = "A test version of the pathway"
        
        # Example nodes and edges (these would typically come from your pathway configuration)
        example_nodes = [
            {
                "id": "node1",
                "type": "Default",
                "data": {
                    "name": "Start Node",
                    "text": "Hello, how can I help you?",
                    "isStart": True
                }
            }
        ]
        
        example_edges = [
            {
                "id": "edge1",
                "source": "node1",
                "target": "node2",
                "data": {
                    "label": "Default Path"
                }
            }
        ]
        
        result = create_pathway_version(
            auth_token=API_KEY,
            pathway_id=PATHWAY_ID,
            name=version_name,
            description=version_description,
            nodes=example_nodes,
            edges=example_edges
        )
        
        if result.get("status") == "success":
            print("Pathway version created successfully!")
            print(f"Version ID: {result.get('version_id')}")
            print(f"Message: {result.get('message')}")
        else:
            print("Error:", result.get("message"))
            
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 