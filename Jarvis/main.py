import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
from nltk.chat.util import Chat, reflections
from pyowm import OWM  # For weather updates
import pyttsx3


#Additional: We can also integrate Jarvis with the OpenAi

# Initialization
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet_user():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Jarvis, your personal assistant. How can I help you today?")

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print(f"Error: {e}")  # Print the exact error message
        print("Say that again please...")
        return "None"
    return query

def get_weather(city):
    owm = OWM('your_api_key')  # Use your OpenWeatherMap API key
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    weather = observation.weather
    temp = weather.temperature('celsius')['temp']
    description = weather.detailed_status
    speak(f"The current temperature in {city} is {temp}°C with {description}.")
    
def chat_with_jarvis(user_input):
    pairs = [
        (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
        (r'who are you', ['I am your personal assistant.']),
        (r'how are you?', ['I am fine, thank you! How can I help you today?']),
        (r'quit|exit', ['Goodbye!', 'See you later!'])
    ]
    chat = Chat(pairs, reflections)
    response = chat.respond(user_input)
    return response

def main():
    greet_user()
    while True:
        query = take_command().lower()
        
        if 'time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {str_time}")
        
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube")
        
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
            speak("Opening Google")
        
        elif 'weather' in query:
            city = query.split('in')[-1].strip()
            get_weather(city)
        
        elif 'jarvis' in query:
            user_input = query.replace('chat', '').strip()
            response = chat_with_jarvis(user_input)
            speak(response)
        
        elif 'exit' in query:
            speak("Goodbye!")
            break
        
        else:
            speak("I did not understand that command. Please try again.")

if __name__ == "__main__":
    main()

