# Example: reuse your existing OpenAI setup
from openai import OpenAI 



def chatbot(message):
    # Point to the local server
    client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

    completion = client.chat.completions.create(
    model="local-model", # this field is currently unused
    messages=[
        {"role": "system", "content": message}
    ],
    temperature=0.7,
    )
    
    return(completion.choices[0].message.content)



"""
This is the new one
def chatbot(message):
    # Point to the local server
    client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

    completion = client.chat.completions.create(
        model="local-model",  # this field is currently unused
        messages=[
            {"role": "system", "content": message}
        ],
        temperature=0.7,
    )

    print(completion.choices[0].message.content)"""

"""
def chatbot(user_input):
    # Set up OpenAI client
    client = OpenAI.ChatCompletion.create(
        base_url="http://localhost:1234/v1",
        api_key="not-needed"
    )

    # Define the initial system message
    talk = [
        {"role": "system", "content": "You are ChatGPT"},
    ]

    while True:
        prompt = input("\n> ")

        # Add user message to the conversation
        talk.append({"role": "user", "content": prompt})

        # Send conversation to OpenAI API
        response = client.create(
            model="local-model",  # Replace with the actual model name
            messages=talk
        )

        # Get the AI's response
        ai_response = response.choices[0].message['content']

        # Print the AI's response
        print(ai_response)

        # Add AI response to the conversation
        talk.append({"role": "assistant", "content": ai_response})

if __name__ == "__main__":
    chatbot()"""

