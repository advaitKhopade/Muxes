import os
from groq import Groq

client = Groq(
    # This is the default and can be omitted
    api_key= "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",
)


def generate_riddle(userinput):
    riddle = "Generate a riddle for the word {} and just give the riddle as output and nothing else.".format(userinput)
    
    chat_completion = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "you are a helpful assistant who have a knowledge of riddles."},
        {
            "role": "user",
            "content": "Generate a riddle for the word {} and just give the riddle as output and nothing else.".format(userinput),
        },
    ],
    model="mixtral-8x7b-32768",
    )   
    return chat_completion.choices[0].message.content

print(generate_riddle("python"))