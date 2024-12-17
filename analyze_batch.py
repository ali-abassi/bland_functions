import requests
from typing import Dict, Any, Optional, List, Union
from config import (
    API_BASE_URL,
    API_VERSION,
    ERROR_MISSING_AUTH,
    ERROR_MISSING_GOAL,
    ERROR_MISSING_QUESTIONS,
    API_KEY
)

# Define the endpoint
ANALYZE_BATCH_ENDPOINT = f"{API_BASE_URL}/{API_VERSION}/calls/batch/{{batch_id}}/analyze"

def analyze_batch(
    auth_token: str,
    batch_id: str,
    goal: str,
    questions: List[str],
    filters: Optional[Dict[str, Any]] = None,
    custom_metrics: Optional[List[Dict[str, Any]]] = None,
    org_id: Optional[str] = None
) -> Dict[str, Any]:
    """
    Analyze a batch of calls using AI to extract insights and answer questions.
    
    Args:
        auth_token (str): Your API authentication token
        batch_id (str): ID of the batch to analyze
        goal (str): Analysis goal or objective
        questions (list): List of questions to answer about the calls
        filters (dict, optional): Filters to apply to the batch
        custom_metrics (list, optional): Custom metrics to calculate
        org_id (str, optional): Organization ID for enterprise customers
        
    Returns:
        dict: Response containing:
            - status: Success/error status
            - analysis_id: ID of the analysis task
            - insights: List of extracted insights
            - answers: Answers to provided questions
            - metrics: Calculated metrics
            - message: Status message
            
    Raises:
        ValueError: If required parameters are missing or invalid
    """
    # Validate required parameters
    if not auth_token:
        raise ValueError(ERROR_MISSING_AUTH)
    if not batch_id:
        raise ValueError("Missing required parameter: batch_id")
    if not goal:
        raise ValueError(ERROR_MISSING_GOAL)
    if not questions:
        raise ValueError(ERROR_MISSING_QUESTIONS)

    # Prepare headers
    headers = {
        "authorization": auth_token,
        "Content-Type": "application/json"
    }

    if org_id:
        headers["encrypted_key"] = org_id

    # Prepare request data
    data = {
        "goal": goal,
        "questions": questions
    }

    # Add optional parameters if provided
    if filters is not None:
        data["filters"] = filters
    if custom_metrics is not None:
        data["custom_metrics"] = custom_metrics

    try:
        # Make API request
        response = requests.post(
            ANALYZE_BATCH_ENDPOINT.format(batch_id=batch_id),
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
        # Get batch ID from user
        batch_id = input("Enter batch ID to analyze: ")
        
        # Example analysis configuration
        analysis_config = {
            "goal": "Evaluate call success rates and identify common patterns",
            "questions": [
                "What percentage of calls resulted in successful appointments?",
                "What are the most common reasons for call failure?",
                "What time of day had the highest success rate?",
                "What patterns emerged in successful calls?",
                "What were the most frequent customer objections?"
            ],
            "filters": {
                "duration_min": 60,  # Minimum call duration in seconds
                "status": ["completed", "failed"],
                "date_range": {
                    "start": "2024-01-01T00:00:00Z",
                    "end": "2024-01-31T23:59:59Z"
                }
            },
            "custom_metrics": [
                {
                    "name": "appointment_rate",
                    "description": "Percentage of calls that resulted in appointments",
                    "calculation": "appointments / total_calls * 100"
                },
                {
                    "name": "average_objections",
                    "description": "Average number of objections per call",
                    "calculation": "total_objections / total_calls"
                }
            ]
        }
        
        # Confirm analysis
        print("\nAnalysis Configuration:")
        print(f"Goal: {analysis_config['goal']}")
        print("\nQuestions to Answer:")
        for i, question in enumerate(analysis_config['questions'], 1):
            print(f"{i}. {question}")
        
        confirm = input("\nRun this analysis? (y/N): ")
        
        if confirm.lower() == 'y':
            result = analyze_batch(
                auth_token=API_KEY,
                batch_id=batch_id,
                **analysis_config
            )
            
            if result.get("status") == "success":
                print("\nAnalysis started successfully!")
                print(f"Analysis ID: {result.get('analysis_id')}")
                
                # Display initial insights if available
                insights = result.get('insights', [])
                if insights:
                    print("\nInitial Insights:")
                    for insight in insights:
                        print(f"- {insight}")
                
                # Display answers if available
                answers = result.get('answers', {})
                if answers:
                    print("\nAnswers to Questions:")
                    for question, answer in answers.items():
                        print(f"\nQ: {question}")
                        print(f"A: {answer}")
                
                # Display metrics if available
                metrics = result.get('metrics', {})
                if metrics:
                    print("\nCalculated Metrics:")
                    for name, value in metrics.items():
                        print(f"{name}: {value}")
            else:
                print("Error:", result.get("message"))
        else:
            print("Analysis cancelled")
            
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 