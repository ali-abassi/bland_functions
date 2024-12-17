import requests
from typing import Dict, Any, Optional
from config import (
    API_BASE_URL,
    API_VERSION,
    ERROR_MISSING_AUTH,
    API_KEY
)

# Define the endpoint
BATCH_ANALYSIS_ENDPOINT = f"{API_BASE_URL}/{API_VERSION}/calls/batch/{{batch_id}}/analysis/{{analysis_id}}"

def get_batch_analysis(
    auth_token: str,
    batch_id: str,
    analysis_id: str,
    include_call_details: Optional[bool] = False,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Retrieve AI analysis results for a batch of calls.
    
    Args:
        auth_token (str): Your API authentication token
        batch_id (str): ID of the batch
        analysis_id (str): ID of the analysis task
        include_call_details (bool, optional): Whether to include individual call analyses
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing:
            - status: Success/error status
            - analysis: Analysis object with results
            - insights: List of extracted insights
            - answers: Answers to analysis questions
            - metrics: Calculated metrics
            - call_analyses: Individual call analyses (if requested)
            - message: Status message
            
    Raises:
        ValueError: If required parameters are missing
    """
    # Validate required parameters
    if not auth_token:
        raise ValueError(ERROR_MISSING_AUTH)
    if not batch_id:
        raise ValueError("Missing required parameter: batch_id")
    if not analysis_id:
        raise ValueError("Missing required parameter: analysis_id")

    # Prepare headers
    headers = {
        "authorization": auth_token
    }

    if org_id:
        headers["encrypted_key"] = org_id

    # Prepare query parameters
    params = {}
    if include_call_details:
        params["include_call_details"] = "true"

    try:
        # Make API request
        response = requests.get(
            BATCH_ANALYSIS_ENDPOINT.format(
                batch_id=batch_id,
                analysis_id=analysis_id
            ),
            headers=headers,
            params=params
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
        # Get required IDs from user
        batch_id = input("Enter batch ID: ")
        analysis_id = input("Enter analysis ID: ")
        
        # Get optional parameters
        include_details = input("Include individual call analyses? (y/N): ").lower() == 'y'
        
        result = get_batch_analysis(
            auth_token=API_KEY,
            batch_id=batch_id,
            analysis_id=analysis_id,
            include_call_details=include_details
        )
        
        if result.get("status") == "success":
            analysis = result.get("analysis", {})
            
            print("\nAnalysis Results:")
            print(f"Status: {analysis.get('status')}")
            print(f"Completion: {analysis.get('completion_percentage')}%")
            print(f"Created At: {analysis.get('created_at')}")
            print(f"Completed At: {analysis.get('completed_at')}")
            
            # Display analysis goal and questions
            print(f"\nGoal: {analysis.get('goal')}")
            print("\nQuestions:")
            for question in analysis.get('questions', []):
                print(f"- {question}")
            
            # Display insights
            insights = result.get("insights", [])
            if insights:
                print("\nKey Insights:")
                for insight in insights:
                    print(f"- {insight}")
            
            # Display answers to questions
            answers = result.get("answers", {})
            if answers:
                print("\nAnswers:")
                for question, answer in answers.items():
                    print(f"\nQ: {question}")
                    print(f"A: {answer}")
            
            # Display metrics
            metrics = result.get("metrics", {})
            if metrics:
                print("\nMetrics:")
                for name, value in metrics.items():
                    print(f"{name}: {value}")
            
            # Display individual call analyses if included
            call_analyses = result.get("call_analyses", [])
            if call_analyses:
                print(f"\nIndividual Call Analyses ({len(call_analyses)}):")
                for call_analysis in call_analyses:
                    print(f"\n  Call ID: {call_analysis.get('call_id')}")
                    print(f"  Duration: {call_analysis.get('duration')} seconds")
                    print(f"  Success: {call_analysis.get('success', False)}")
                    
                    # Display call-specific insights
                    insights = call_analysis.get('insights', [])
                    if insights:
                        print("  Insights:")
                        for insight in insights:
                            print(f"  - {insight}")
                    
                    # Display call-specific metrics
                    metrics = call_analysis.get('metrics', {})
                    if metrics:
                        print("  Metrics:")
                        for name, value in metrics.items():
                            print(f"  {name}: {value}")
        else:
            print("Error:", result.get("message"))
            
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 