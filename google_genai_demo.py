import os
from dotenv import load_dotenv
# Import the library
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv(override=True)


# Your API key will be replaced here
API_KEY = os.environ.get("GEMINI_API_KEY")

# Set up authentication with API key
genai.configure(api_key=API_KEY)

# Choose the Gemini Flash model
model = genai.GenerativeModel('gemma-3-27b-it')

# Generate text with a prompt
response = model.generate_content("What kind of a tree can you carry in your hand?")

# Print the generated content
print(response.text)