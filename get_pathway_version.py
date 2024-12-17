import requests
from typing import Dict, Any, Optional
from config import (
    PATHWAY_VERSION_ENDPOINT,
    ERROR_MISSING_AUTH,
    ERROR_MISSING_PATHWAY,
    API_KEY,
    PATHWAY_ID
)

def get_pathway_version(
    auth_token: str,
    pathway_id: str,
    version_id: str,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Retrieve details of a specific version of a pathway.
    
    Args:
        auth_token (str): Your API authentication token
        pathway_id (str): ID of the pathway
        version_id (str): ID of the specific version to retrieve
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing:
            - status: Success/error status
            - version: Details of the specific pathway version
            - nodes: Array of node configurations
            - edges: Array of edge configurations
            
    Raises:
        ValueError: If required parameters are missing
    """
    # Validate required parameters
    if not auth_token:
        raise ValueError(ERROR_MISSING_AUTH)
    if not pathway_id:
        raise ValueError(ERROR_MISSING_PATHWAY)
    if not version_id:
        raise ValueError("Missing required parameter: version_id")

    # Prepare headers
    headers = {
        "authorization": auth_token
    }

    if org_id:
        headers["encrypted_key"] = org_id

    try:
        # Make API request
        response = requests.get(
            PATHWAY_VERSION_ENDPOINT.format(
                pathway_id=pathway_id,
                version_id=version_id
            ),
            headers=headers
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
        # Example version ID (you would get this from get_pathway_versions)
        version_id = "example_version_id"
        
        result = get_pathway_version(
            auth_token=API_KEY,
            pathway_id=PATHWAY_ID,
            version_id=version_id
        )
        
        if result.get("status") == "success":
            print("Pathway version details retrieved successfully!")
            version = result.get("version", {})
            
            print(f"\nVersion Details:")
            print(f"Version Number: {version.get('version_number')}")
            print(f"Created At: {version.get('created_at')}")
            print(f"Name: {version.get('name')}")
            print(f"Status: {version.get('status')}")
            
            # Print nodes information
            nodes = result.get("nodes", [])
            if nodes:
                print("\nNodes:")
                for node in nodes:
                    print(f"Node ID: {node.get('id')}")
                    print(f"Name: {node.get('name')}")
                    print(f"Type: {node.get('type')}")
                    print("-" * 40)
            
            # Print edges information
            edges = result.get("edges", [])
            if edges:
                print("\nEdges:")
                for edge in edges:
                    print(f"Source: {edge.get('source')}")
                    print(f"Target: {edge.get('target')}")
                    print(f"Label: {edge.get('label')}")
                    print("-" * 40)
        else:
            print("Error:", result.get("message"))
            
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 