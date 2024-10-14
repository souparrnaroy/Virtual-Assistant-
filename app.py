import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '').strip()  # Remove "alexa" and strip whitespace
            print(command)
    except Exception as e:
        print(f"An error occurred: {e}")
    return command


def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who ' in command:
        person = command.replace('who the heck is', '').strip()
        try:
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        except wikipedia.exceptions.DisambiguationError:
            talk("Sorry, I couldn't find any information on that person.")
        except wikipedia.exceptions.PageError:
            talk("Sorry, I couldn't find any information on that person.")
    elif 'date' in command:
        date = datetime.datetime.now().strftime('%B %d, %Y')
        talk('Current date is ' + date)
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Sorry, I didn\'t understand that command. Please try again.')


while True:
    run_alexa()





# import speech_recognition as sr
# import pyttsx3
# import pywhatkit
# import datetime
# import wikipedia
# import pyjokes

# listener = sr.Recognizer()
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)


# def talk(text):
#     engine.say(text)
#     engine.runAndWait()


# def take_command():
#     try:
#         with sr.Microphone() as source:
#             print('listening...')
#             voice = listener.listen(source)
#             command = listener.recognize_google(voice)
#             command = command.lower()
#             if 'alexa' in command:
#                 command = command.replace('alexa', '')
#                 print(command)
#     except:
#         pass
#     return command


# def run_alexa():
#     command = take_command()
#     print(command)
#     if 'play' in command:
#         song = command.replace('play', '')
#         talk('playing ' + song)
#         pywhatkit.playonyt(song)
#     elif 'time' in command:
#         time = datetime.datetime.now().strftime('%I:%M %p')
#         talk('Current time is ' + time)
#     elif 'who the heck is' in command:
#         person = command.replace('who the heck is', '')
#         info = wikipedia.summary(person, 1)
#         print(info)
#         talk(info)
#     elif 'date' in command:
#         talk('sorry, I have a headache')
#     elif 'are you single' in command:
#         talk('I am in a relationship with wifi')
#     elif 'joke' in command:
#         talk(pyjokes.get_joke())
#     else:
#         talk('Please say the command again.')


# while True:
#     run_alexa()
















# import speech_recognition as sr
# import pyttsx3
# import pywhatkit
# import wikipedia
# import os
# import datetime

# listener = sr.Recognizer()
# machine = pyttsx3.init()

# def talk(text):
#     machine.say(text)
#     machine.runAndWait()

# def input_instruction():
#     try:
#         with sr.Microphone() as origin:
#             print('listening....')
#             speech = listener.listen(origin)
#             instruction = listener.recognize_google(speech)
#             instruction = instruction.lower()
#             if 'jarvis' in instruction:
#                 instruction = instruction.replace('jarvis', " ")
#                 print(instruction)
#             return instruction
#     except sr.UnknownValueError:
#         talk('Sorry, I didn\'t understand that')
#         return None

# def play_song(song):
#     talk('opening youtube....')
#     talk('playing ' + song)
#     pywhatkit.playonyt(song)

# def open_chrome():
#     talk('opening chrome')
#     os.system("start chrome.exe")

# def open_spotify():
#     talk('opening spotify')
#     os.system("start spotify.exe")

# def who_is(human):
#     info = wikipedia.summary(human, 1)
#     print(info)
#     talk(info)

# instruction_map = {
#     'play': play_song,
#     'open chrome': open_chrome,
#     'open spotify': open_spotify,
#     'who is': who_is,
#     # ...
# }

# def play_jarvis():
#     instruction = input_instruction()
#     if instruction:
#         for key in instruction_map:
#             if key in instruction:
#                 instruction_map[key](instruction.replace(key, ""))
#                 break
#         else:
#             talk('please repeat')

# play_jarvis()