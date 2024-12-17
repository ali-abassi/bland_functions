# Configuration settings for Bland AI API
API_BASE_URL = "https://api.bland.ai"
API_VERSION = "v1"
API_KEY = "ADD API KEY HERE"
DEFAULT_PHONE = "ADD DEFAULT PHONE NUMBER HERE"
ORG_ID = "ADD ORG ID HERE"
PATHWAY_ID = "ADD PATHWAY ID HERE"
CALL_ID = "ADD CALL ID HERE"

# Endpoints
CALLS_ENDPOINT = f"{API_BASE_URL}/{API_VERSION}/calls"
ANALYZE_ENDPOINT = f"{CALLS_ENDPOINT}/{{call_id}}/analyze"
STOP_CALL_ENDPOINT = f"{CALLS_ENDPOINT}/{{call_id}}/stop"
STOP_ALL_CALLS_ENDPOINT = f"{CALLS_ENDPOINT}/active/stop"
CALL_DETAILS_ENDPOINT = f"{CALLS_ENDPOINT}/{{call_id}}"
EVENT_STREAM_ENDPOINT = f"{CALLS_ENDPOINT}/{{call_id}}/stream"
RECORDING_ENDPOINT = f"{CALLS_ENDPOINT}/{{call_id}}/recording"
TRANSCRIPTS_ENDPOINT = f"{CALLS_ENDPOINT}/{{call_id}}/transcripts"
PATHWAYS_ENDPOINT = f"{API_BASE_URL}/{API_VERSION}/pathways"
PATHWAY_DETAILS_ENDPOINT = f"{PATHWAYS_ENDPOINT}/{{pathway_id}}"
CREATE_PATHWAY_ENDPOINT = PATHWAYS_ENDPOINT
UPDATE_PATHWAY_ENDPOINT = f"{PATHWAYS_ENDPOINT}/{{pathway_id}}/update"
DELETE_PATHWAY_ENDPOINT = f"{PATHWAYS_ENDPOINT}/{{pathway_id}}/delete"
VECTOR_STORE_ENDPOINT = f"{API_BASE_URL}/{API_VERSION}/vector"
UPDATE_VECTOR_ENDPOINT = f"{VECTOR_STORE_ENDPOINT}/{{vector_id}}"
VECTOR_DETAILS_ENDPOINT = f"{VECTOR_STORE_ENDPOINT}/{{vector_id}}/details"
DELETE_VECTOR_ENDPOINT = f"{VECTOR_STORE_ENDPOINT}/{{vector_id}}/delete"
PATHWAY_CHAT_CREATE_ENDPOINT = f"{API_BASE_URL}/{API_VERSION}/pathway/chat/create"
PATHWAY_CHAT_ENDPOINT = f"{API_BASE_URL}/{API_VERSION}/pathway/chat/{{chat_id}}"
PATHWAY_VERSIONS_ENDPOINT = f"{PATHWAYS_ENDPOINT}/{{pathway_id}}/versions"
PATHWAY_VERSION_ENDPOINT = f"{PATHWAYS_ENDPOINT}/{{pathway_id}}/versions/{{version_id}}"
PROMOTE_PATHWAY_VERSION_ENDPOINT = f"{PATHWAYS_ENDPOINT}/{{pathway_id}}/versions/{{version_id}}/promote"
CREATE_PATHWAY_VERSION_ENDPOINT = f"{PATHWAYS_ENDPOINT}/{{pathway_id}}/versions/create"
DELETE_PATHWAY_VERSION_ENDPOINT = f"{PATHWAYS_ENDPOINT}/{{pathway_id}}/versions/{{version_id}}/delete"
FOLDERS_ENDPOINT = f"{API_BASE_URL}/{API_VERSION}/folders"
FOLDER_PATHWAYS_ENDPOINT = f"{FOLDERS_ENDPOINT}/{{folder_id}}/pathways"
CREATE_FOLDER_ENDPOINT = FOLDERS_ENDPOINT
DELETE_FOLDER_ENDPOINT = f"{FOLDERS_ENDPOINT}/{{folder_id}}/delete"
UPDATE_FOLDER_ENDPOINT = f"{FOLDERS_ENDPOINT}/{{folder_id}}/update"
MOVE_PATHWAY_ENDPOINT = f"{PATHWAYS_ENDPOINT}/{{pathway_id}}/move"
PURCHASE_PHONE_ENDPOINT = f"{API_BASE_URL}/{API_VERSION}/phone/purchase"
UPDATE_INBOUND_ENDPOINT = f"{API_BASE_URL}/{API_VERSION}/phone/inbound/update"
LIST_INBOUND_ENDPOINT = f"{API_BASE_URL}/{API_VERSION}/phone/inbound"
INBOUND_DETAILS_ENDPOINT = f"{API_BASE_URL}/{API_VERSION}/phone/inbound/{{phone_number}}"
LIST_OUTBOUND_ENDPOINT = f"{API_BASE_URL}/{API_VERSION}/phone/outbound"
LIST_VOICES_ENDPOINT = f"{API_BASE_URL}/{API_VERSION}/voices"
VOICE_DETAILS_ENDPOINT = f"{API_BASE_URL}/{API_VERSION}/voices/{{voice_id}}"
PUBLISH_VOICE_ENDPOINT = f"{API_BASE_URL}/{API_VERSION}/voices/publish"
GENERATE_AUDIO_ENDPOINT = f"{API_BASE_URL}/{API_VERSION}/voices/generate"

# Custom Tools Endpoints
CUSTOM_TOOLS_ENDPOINT = f"{API_BASE_URL}/{API_VERSION}/tools"
CUSTOM_TOOL_DETAILS_ENDPOINT = f"{CUSTOM_TOOLS_ENDPOINT}/{{tool_id}}"
UPDATE_CUSTOM_TOOL_ENDPOINT = f"{CUSTOM_TOOLS_ENDPOINT}/{{tool_id}}/update"
DELETE_CUSTOM_TOOL_ENDPOINT = f"{CUSTOM_TOOLS_ENDPOINT}/{{tool_id}}/delete"
LIST_CUSTOM_TOOLS_ENDPOINT = f"{CUSTOM_TOOLS_ENDPOINT}/list"

# Default Values
DEFAULT_MODEL = "enhanced"
DEFAULT_VOICE = "mason"
DEFAULT_LANGUAGE = "en-US"
DEFAULT_MAX_DURATION = 30
DEFAULT_TEMPERATURE = 0.7
DEFAULT_INTERRUPTION_THRESHOLD = 100
DEFAULT_LIMIT = 1000  # Added for list calls pagination

# Background Track Options
BACKGROUND_TRACKS = {
    "none": "none",
    "office": "office",
    "cafe": "cafe",
    "restaurant": "restaurant"
}

# Error Messages
ERROR_MISSING_AUTH = "Missing authorization header"
ERROR_MISSING_PHONE = "Missing required parameter: phone_number"
ERROR_MISSING_TASK = "Missing required parameter: task"
ERROR_MISSING_PATHWAY = "Missing required parameter: pathway_id"
ERROR_INVALID_PHONE = "Invalid phone number format"
ERROR_MISSING_ORG = "Missing organization ID"
ERROR_INVALID_MODEL = "Invalid model. Must be one of: base, turbo, enhanced"
ERROR_INVALID_LANGUAGE = "Invalid language code"
ERROR_MISSING_CALL_ID = "Missing required parameter: call_id"
ERROR_MISSING_GOAL = "Missing required parameter: goal"
ERROR_MISSING_QUESTIONS = "Missing required parameter: questions"
ERROR_NO_RECORDING = "No recording available for this call"
ERROR_NO_TRANSCRIPTS = "No transcripts available for this call"
ERROR_NO_PATHWAYS = "No pathways found"
ERROR_MISSING_VECTOR_NAME = "Missing required parameter: name"
ERROR_MISSING_VECTOR_DATA = "Missing required parameter: data"
ERROR_MISSING_VECTOR_ID = "Missing required parameter: vector_id"
ERROR_MISSING_PATHWAY_NAME = "Missing required parameter: name"
ERROR_MISSING_NODES = "Missing required parameter: nodes"
ERROR_MISSING_EDGES = "Missing required parameter: edges"

# Response Status
STATUS_SUCCESS = "success"
STATUS_ERROR = "error" 