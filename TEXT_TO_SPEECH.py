import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty("voices")
voice = engine.setProperty("voice", voices[0].id)

text = input("Enter the text ")

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak(text)