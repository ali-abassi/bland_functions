import requests
from typing import Dict, Any, Optional, List
from config import (
    PATHWAY_VERSIONS_ENDPOINT,
    ERROR_MISSING_AUTH,
    ERROR_MISSING_PATHWAY,
    API_KEY,
    PATHWAY_ID
)

def get_pathway_versions(
    auth_token: str,
    pathway_id: str,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Retrieve all versions of a specific pathway, including version number, creation date, name, and latest status.
    
    Args:
        auth_token (str): Your API authentication token
        pathway_id (str): ID of the pathway to get versions for
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing:
            - status: Success/error status
            - versions: List of pathway versions with details
            
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
            PATHWAY_VERSIONS_ENDPOINT.format(pathway_id=pathway_id),
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
        result = get_pathway_versions(
            auth_token=API_KEY,
            pathway_id=PATHWAY_ID
        )
        
        if result.get("status") == "success":
            print("Pathway versions retrieved successfully!")
            versions = result.get("versions", [])
            
            if versions:
                print("\nVersions:")
                for version in versions:
                    print(f"Version: {version.get('version_number')}")
                    print(f"Created: {version.get('created_at')}")
                    print(f"Name: {version.get('name')}")
                    print(f"Status: {version.get('status')}")
                    print("-" * 40)
            else:
                print("No versions found for this pathway.")
        else:
            print("Error:", result.get("message"))
            
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 