from demogpt import DemoGPT
agent = DemoGPT(model_name="gpt-35-turbo", openai_api_key="111") # if OPENAI_API_KEY is not set in env variables, put it with openai_api_key argument
instruction = "Your instruction here"
title = "Your title here"
code = ""
for phase in agent(instruction=instruction, title=title):
    print(phase) # this will display the resulting json for each generation stage
    if phase["done"]:
        code = phase["code"] # final code
print(code)