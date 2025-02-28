import time
import requests
import pyttsx3
import speech_recognition as sr
import datetime

# OpenWeather API Key (Replace with your actual API key)
API_KEY = "your_openweather_api_key"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize voice commands
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        speak("There was an error with the voice recognition service.")
        return ""

# Function to get weather info
def get_weather(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        result = f"The weather in {city} is {weather} with a temperature of {temp}°C."
        speak(result)
        return result
    else:
        speak("City not found. Please try again.")
        return "City not found."

# Function to set reminders
def set_reminder(reminder_text, seconds):
    speak(f"Reminder set for {seconds} seconds.")
    time.sleep(seconds)
    speak(f"Reminder: {reminder_text}")

# Main function
def virtual_assistant():
    speak("Hello! How can I assist you?")
    
    while True:
        command = listen()

        if "weather" in command:
            speak("Which city?")
            city = listen()
            if city:
                print(get_weather(city))
        
        elif "reminder" in command:
            speak("What should I remind you about?")
            reminder_text = listen()
            speak("In how many seconds?")
            try:
                seconds = int(listen())
                set_reminder(reminder_text, seconds)
            except ValueError:
                speak("Invalid time. Please try again.")

        elif "exit" in command or "quit" in command:
            speak("Goodbye! Have a great day.")
            break
        
        else:
            speak("I can only check the weather, set reminders, or exit. Try again!")

# Run the assistant
if __name__ == "__main__":
    virtual_assistant()
