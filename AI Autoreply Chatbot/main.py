import pyautogui 
import time
import pyperclip 
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key="<Your Key Here>")

def is_last_message_from_sender(chat_log, sender_name="Faizan"):
    """
    Check if the last message in the chat log is from the specified sender.
    """
    messages = chat_log.strip().split("/2024] ")[-1]
    return sender_name in messages

def click_chrome_icon():
    """
    Click on the Chrome icon at predefined coordinates.
    """
    pyautogui.click(1639, 1412)
    time.sleep(1)  # Wait to ensure the click is registered

def select_and_copy_chat():
    """
    Select and copy the chat text.
    """
    pyautogui.moveTo(972, 202)
    pyautogui.dragTo(2213, 1278, duration=2.0, button='left')
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)  # Wait to ensure the copy command is completed

def get_chat_history():
    """
    Retrieve the copied chat text from the clipboard.
    """
    chat_history = pyperclip.paste()
    print(chat_history)
    return chat_history

def generate_response(chat_history):
    """
    Generate a response using the OpenAI API.
    """
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a person named Oxygen who speaks Urdu as well as English. You are from Pakistan and you are a coder. You will the analyze chat history and deal people in a professional way. Output should be the next chat response (text message only)."},
            {"role": "system", "content": "Do not start like this [21:02, 12/6/2024] Faizan: "},
            {"role": "user", "content": chat_history}
        ]
    )
    return completion.choices[0].message.content

def paste_response(response):
    """
    Paste the generated response.
    """
    pyperclip.copy(response)
    pyautogui.click(1808, 1328)
    time.sleep(1)  # Wait to ensure the click is registered
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)  # Wait to ensure the paste command is completed
    pyautogui.press('enter')

def main():
    """
    Main function to run the automated process.
    """
    click_chrome_icon()
    while True:
        time.sleep(5)
        select_and_copy_chat()
        chat_history = get_chat_history()
        if is_last_message_from_sender(chat_history):
            response = generate_response(chat_history)
            paste_response(response)

if __name__ == "__main__":
    main()

