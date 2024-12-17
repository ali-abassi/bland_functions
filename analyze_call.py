import requests
from typing import Dict, Union, List, Any
from config import (
    ANALYZE_ENDPOINT,
    ERROR_MISSING_AUTH,
    ERROR_MISSING_CALL_ID,
    ERROR_MISSING_GOAL,
    ERROR_MISSING_QUESTIONS,
    API_KEY,
    CALL_ID
)

def analyze_call(
    auth_token: str,
    call_id: str,
    goal: str,
    questions: List[List[str]]
) -> Dict[str, Any]:
    """
    Analyze a call using AI based on specific questions and goals.
    
    Args:
        auth_token (str): Your API authentication token
        call_id (str): The unique identifier for the call to analyze
        goal (str): Overall purpose of the call analysis
        questions (List[List[str]]): List of questions, each containing question text and expected answer type
            Example: [
                ["Who answered the call?", "human or voicemail"],
                ["Positive feedback about the product: ", "string"],
                ["Customer confirmed they were satisfied", "boolean"]
            ]
    
    Returns:
        dict: Response containing analysis results including:
            - status: Success/error status
            - message: Status message
            - answers: Array of analyzed answers
            - credits_used: Token-based price for analysis
    
    Raises:
        ValueError: If required parameters are missing or invalid
    """
    # Validate required parameters
    if not auth_token:
        raise ValueError(ERROR_MISSING_AUTH)
    if not call_id:
        raise ValueError(ERROR_MISSING_CALL_ID)
    if not goal:
        raise ValueError(ERROR_MISSING_GOAL)
    if not questions or not isinstance(questions, list):
        raise ValueError(ERROR_MISSING_QUESTIONS)

    # Prepare headers and payload
    headers = {
        "authorization": auth_token,
        "Content-Type": "application/json"
    }
    
    payload = {
        "goal": goal,
        "questions": questions
    }

    try:
        # Make API request
        response = requests.post(
            ANALYZE_ENDPOINT.format(call_id=call_id),
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
    TEST_GOAL = "Evaluate customer satisfaction and identify key feedback points"
    TEST_QUESTIONS = [
        ["Who answered the call?", "human or voicemail"],
        ["Positive feedback about the product: ", "string"],
        ["Negative feedback about the product: ", "string"],
        ["Customer confirmed they were satisfied", "boolean"]
    ]
    
    try:
        result = analyze_call(
            auth_token=API_KEY,
            call_id=CALL_ID,
            goal=TEST_GOAL,
            questions=TEST_QUESTIONS
        )
        print("API Response:", result)
        
    except ValueError as e:
        print("Validation Error:", str(e))
    except Exception as e:
        print("Unexpected Error:", str(e)) 