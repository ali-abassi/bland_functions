import requests
from typing import Dict, Any, Optional
from config import (
    DELETE_PATHWAY_VERSION_ENDPOINT,
    ERROR_MISSING_AUTH,
    ERROR_MISSING_PATHWAY,
    API_KEY,
    PATHWAY_ID
)

def delete_pathway_version(
    auth_token: str,
    pathway_id: str,
    version_id: str,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Delete a specific version of a pathway.
    
    Args:
        auth_token (str): Your API authentication token
        pathway_id (str): ID of the pathway
        version_id (str): ID of the version to delete
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing:
            - status: Success/error status
            - message: Status message
            
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
        response = requests.delete(
            DELETE_PATHWAY_VERSION_ENDPOINT.format(
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
        
        # Confirm deletion
        confirm = input(f"Are you sure you want to delete version {version_id}? (y/N): ")
        
        if confirm.lower() == 'y':
            result = delete_pathway_version(
                auth_token=API_KEY,
                pathway_id=PATHWAY_ID,
                version_id=version_id
            )
            
            if result.get("status") == "success":
                print("Pathway version deleted successfully!")
                print(f"Message: {result.get('message')}")
            else:
                print("Error:", result.get("message"))
        else:
            print("Deletion cancelled")
            
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 