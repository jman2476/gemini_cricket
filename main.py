import os
import argparse
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function

def main():
    # Argparse
    parser = argparse.ArgumentParser(description='Chatbot')
    parser.add_argument(
            'user_prompt', 
            type=str, 
            help='User prompt: Tell the agent what you want it to do.'
            )
    parser.add_argument(
            '--verbose', '-v',
            action='store_true',
            help='Enable verbose output'
            )
    args = parser.parse_args()
    # Load .env and api key
    load_dotenv() 
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key == None: raise RuntimeError('No API key found. Generate one via Google AI Studio, and add to .env file')
    else: print(f'API key: ...{api_key[-8:]}')
    if args.verbose:
        print('User prompt:')
        print(args.user_prompt)
    
    # Create Gemini client
    client = genai.Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    max_cycles = int(os.environ.get("MAX_CALLS"))
    for _ in range(max_cycles):
        cycle = generate_response(client, messages, args.verbose)
        if cycle == 'Done':
            break
        if _ == max_cycles - 1: sys.exit('Ran out of cycles')


def generate_response(client, messages, verbose):
    # Call Gemini API
    response = client.models.generate_content(
            model='gemini-2.5-flash', 
            contents=messages,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                tools=[available_functions]
                )
            )
    if response.usage_metadata == None: 
        raise RuntimeError(
                'No response recieved. Please check your internet, or that the model you are calling is active.'
                )
    
    if verbose:
        print('Prompt tokens:', response.usage_metadata.prompt_token_count)
        print('Response tokens:', response.usage_metadata.candidates_token_count)

    if response.candidates:
        for candidate in response.candidates:
            messages.append(candidate.content)

    if not response.function_calls:
        print('Gemini response:\n', response.text)
        return 'Done'
    
    function_results = []
    for function in response.function_calls:
        function_call_res = call_function(function, verbose)
        if (
            not function_call_res.parts
            or not function_call_res.parts[0].function_response
            or not function_call_res.parts[0].function_response.response):
            raise RuntimeError(f'Empty function call response for {function.name}')
        
        function_results.append(function_call_res.parts[0])
        if verbose:
            print(f'-> {function_call_res.parts[0].function_response.response}')

        messages.append(types.Content(role='user', parts=function_results))


if __name__ == '__main__':
    main()


    
