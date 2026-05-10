import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import pywhatkit
import os
import pyautogui
from speech_to_text import get_voice_input

# Text to Speech
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Voice Input
def execute_task(command):

    command = command.lower()

    # EXIT
    if any(word in command for word in ["exit", "stop", "bye", "goodbye"]):
        speak("Goodbye! Program is closing.")
        return False

    # OPEN CHROME
    if "chrome" in command:
        speak("Opening Chrome")
        webbrowser.open("https://www.google.com")

    # OPEN YOUTUBE
    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    # OPEN FACEBOOK
    elif "facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")

    # OPEN TIKTOK
    elif "tiktok" in command:
        speak("Opening Tiktok")
        webbrowser.open("https://www.tiktok.com")

    # OPEN WHATSAPP
    elif "whatsapp" in command:
        speak("Opening Whatsapp")
        webbrowser.open("https://web.whatsapp.com/")


    # OPEN NOTEPAD
    elif "notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")

    # OPEN VS CODE
    elif "code" in command or "vs code" in command:
        speak("Opening VS Code")
        os.system("code")   # Make sure VS Code is in PATH

    # TIME
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"Current time is {time}")

    # SEARCH GOOGLE
    elif "search" in command:
        query = command.replace("search", "")
        speak(f"Searching {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")

    # PLAY MUSIC
    elif "play" in command:
        song = command.replace("play", "").strip()
        speak(f"Playing {song}")
        pywhatkit.playonyt(song)

    # VOLUME CONTROL
    elif "volume up" in command:
        speak("Increasing volume")
        pyautogui.press("volumeup")

    elif "volume down" in command:
        speak("Decreasing volume")
        pyautogui.press("volumedown")

    elif "mute" in command:
        speak("Muting volume")
        pyautogui.press("volumemute")

    # SHUTDOWN
    elif "shutdown" in command:
        speak("Shutting down system")
        os.system("shutdown /s /t 5")

    # RESTART
    elif "restart" in command:
        speak("Restarting system")
        os.system("shutdown /r /t 5")

    # GREETING
    elif any(word in command for word in ["hello", "salam", "hi"]):
        speak("Hello! How can I help you?")

    else:
        speak("I don't understand this command")

    return True

# Main Loop
def main():
    speak("Voice assistant started")

    while True:
        command = get_voice_input()

        if command == "":
            continue

        if not execute_task(command):
            break

# Run
if __name__ == "__main__":
    main()