"""Configuration for the LLM Council."""

import os
from dotenv import load_dotenv

load_dotenv()

# OpenRouter API key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Council members - list of OpenRouter model identifiers (Premium models)
COUNCIL_MODELS = [
    "anthropic/claude-sonnet-5",
    "openai/gpt-5.6-terra",
    "google/gemini-3.7-flash",
    "x-ai/grok-4.6",
]

# Chairman model - synthesizes final response
CHAIRMAN_MODEL = "anthropic/claude-opus-5"

# OpenRouter API endpoint
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Data directory for conversation storage
DATA_DIR = "data/conversations"
