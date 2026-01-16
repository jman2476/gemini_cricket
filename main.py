import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Argparse
parser = argparse.ArgumentParser(description='Chatbot')
parser.add_argument(
        'user_prompt', 
        type=str, 
        help='User prompt: Tell the agent what you want it to do.'
        )
parser.add_argument(
        '--verbose',
        action='store_true',
        help='Enable verbose output'
        )
args = parser.parse_args()
# Load .env and api key
load_dotenv() 
api_key = os.environ.get("GEMINI_API_KEY")
if api_key == None: raise RuntimeError('No API key found. Generate one via Google AI Studio, and add to .env file')
else: print(f'API key: ...{api_key[-8:]}')

# Create Gemini client
client = genai.Client(api_key=api_key)
messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

# Call Gemini API
response = client.models.generate_content(
        model='gemini-2.5-flash', 
        contents=messages
        )
if response.usage_metadata == None: 
    raise RuntimeError(
            'No response recieved. Please check your internet, or that the model you are calling is active.'
            )
else:
    if args.verbose:
        print(
            'User prompt:', args, 
            '\nPrompt tokens:', response.usage_metadata.prompt_token_count,
            '\nResponse tokens:', response.usage_metadata.candidates_token_count
            )
print('Gemini response:', response.text)
