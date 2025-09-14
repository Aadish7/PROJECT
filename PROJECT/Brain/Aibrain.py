import openai

# Loading the API key
fileopen = open("D:\PROJECT\Data\Api.txt", "r")
API = fileopen.read().strip()  # Added .strip() to remove any newline or whitespace
fileopen.close()

# Setting up the API key
openai.api_key = API

def ReplyBrain(question, chat_log=None):
    # Reading the chat log from file
    with open("D:\PROJECT\Database\chat_log.txt", "r") as FileLog:
        chat_log_template = FileLog.read()
    
    # If no chat log is passed, use the existing one
    if chat_log is None:
        chat_log = chat_log_template
    
    # Formulating the prompt
    prompt = f'{chat_log} You : {question}\nZeus : '
    
    # Making the API call
    response = openai.Completion.create(
        model="gpt-4-turbo",  # Updated model name
        prompt=prompt,
        temperature=0.5,
        max_tokens=60,
        top_p=0.3,
        frequency_penalty=0.5,
        presence_penalty=0
    )
    
    # Extracting the response
    answer = response.choices[0].text.strip()
    
    # Updating the chat log
    chat_log_template_update = chat_log_template + f"\n You : {question} \nZeus : {answer}"
    with open("D:\PROJECT\Database\chat_log.txt", "w") as FileLog:
        FileLog.write(chat_log_template_update)
    
    return answer
