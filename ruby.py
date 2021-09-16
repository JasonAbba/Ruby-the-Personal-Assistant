import speech_recognition as sr
import pyttsx3
import json
import random
import os
import subprocess
import pywhatkit as pwk # whatsapp, youtube, google search
import time
import wolframalpha
from boltiot import Bolt

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# initialising variables
current_app = ''
apps = {
    'spotify' : 'Spotify.exe',
    'firefox' : 'firefox.exe',
    'code' : 'Code.exe',
    'sublime' : 'sublime_text.exe',
    'cmd' : 'wt.exe',
    'terminal' : 'wt.exe',
    'discord' : 'Update.exe',
    'steam' : 'steam.exe',
    'calculator' : 'calc.exe',
    'whatsapp' : 'WhatsApp.exe'
}

def text2speech(audio):
    engine.setProperty('rate', 180) # Sets speed percent can be more than 100
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        # # led right indication that ruby is listening {---
        # response=mybolt.isOnline()
        # data=json.loads(response)
        # if data["value"]=="online":
        #     mybolt.digitalWrite('0','HIGH')#0 is the gpio pin
        # else:
        #     print("Your device is offline")
        # # ---}

        r.adjust_for_ambient_noise(source)
        print('Listening...')
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        # # led right indication that ruby is listening {---
        # res=mybolt.isOnline()
        # data=json.loads(res)
        # if data["value"]=="online":
        #     mybolt.digitalWrite('0','LOW')
        # else:
        #     print("Your device is offline")
        # # ---}

        print('Recognizing...')
        query = r.recognize_google(audio, language = 'en-in')
        print('You: ', query)
    except Exception as e:
        print(e)
        print('Unable to recognize your voice.')
        return 'None'
    return query

def rubysays(key): # key is the tag or key element in the data.json which contains the responses
    length = len(data[key])
    # print(length)
    say_this = data[key][random.randint(0, length - 1)]
    return say_this

def startruby():
    global current_app

    query = takeCommand().lower()

    if query in ['bye', 'goodbye']:
        say_this = rubysays('bye')
        print(say_this)
        text2speech(say_this)
        exit()

    elif query in ['who am i', 'what is my name', 'my name']:
        say_this = rubysays('my_name')
        print(say_this)
        text2speech(say_this)
    
    elif 'my birthday' in query:
        say_this = rubysays('my_birthday')
        print(say_this)
        text2speech(say_this)
    
    elif 'my dob' in query or 'my date of birth' in query:
        say_this = rubysays('my_dob')
        print(say_this)
        text2speech(say_this)
    
    elif 'my blood group' in query:
        say_this = rubysays('my_blood_group')
        print(say_this)
        text2speech(say_this)
    
    elif 'my phone number' in query or 'my mobile number' in query:
        say_this = rubysays('my_phone_num')
        print(say_this)
        text2speech(say_this)
    
    elif 'my address' in query or 'house address' in query:
        say_this = rubysays('my_address')
        print(say_this)
        text2speech(say_this)
    
    elif 'pan card number' in query or 'pan number' in query:
        say_this = rubysays('pan_number')
        print(say_this)
        text2speech(say_this)

    elif 'aadhar card number' in query or 'aadhar number' in query or 'adhar card number' in query or 'adhar number' in query:
        say_this = rubysays('aadhar_number')
        print(say_this)
        text2speech(say_this)
    
    elif 'passport number' in query or 'past port' in query:
        say_this = rubysays('passport_number')
        print(say_this)
        text2speech(say_this)
    
    elif query in ['open spotify', 'pen spotify', 'spotify']:
        say_this = rubysays('spotify')
        print(say_this)
        text2speech(say_this)
        current_app = 'spotify'
        # os.startfile(r'C:\Users\JasonPC\AppData\Local\Microsoft\WindowsApps\Spotify.exe')
        # os.system(r'C:\Users\JasonPC\AppData\Local\Microsoft\WindowsApps\Spotify.exe')
        subprocess.Popen(r'C:\Users\JasonPC\AppData\Local\Microsoft\WindowsApps\Spotify.exe')

    elif query in ['open firefox', 'pen firefox', 'firefox', 'fire fox']: # opens Visual Studio Code
        say_this = 'Opening Firefox Browser'
        print(say_this)
        text2speech(say_this)
        current_app = 'firefox'
        # os.startfile(r'C:\Program Files\Mozilla Firefox\firefox.exe')
        # os.system(r'C:\Program Files\Mozilla Firefox\firefox.exe')
        subprocess.Popen(r'C:\Program Files\Mozilla Firefox\firefox.exe')
    
    elif query in ['open code', 'pen code']: # opens Visual Studio Code
        say_this = 'Opening Visual Studio Code'
        print(say_this)
        text2speech(say_this)
        current_app = 'code'
        # os.startfile(r'C:\Program Files\Microsoft VS Code\Code.exe')
        # os.system(r'C:\Program Files\Microsoft VS Code\Code.exe')
        subprocess.Popen(r'C:\Program Files\Microsoft VS Code\Code.exe')
    
    elif query in ['open sublime', 'pen sublime', 'open sub lime', 'pen sub lime']: # opens Sublime Text
        say_this = 'Opening Sublime Text'
        print(say_this)
        text2speech(say_this)
        current_app = 'sublime'
        # os.startfile(r'C:\Program Files\Sublime Text 3\sublime_text.exe')
        # os.system(r'C:\Program Files\Sublime Text 3\sublime_text.exe')
        subprocess.Popen(r'C:\Program Files\Sublime Text 3\sublime_text.exe')

    elif query in ['open cmd', 'c m d']: # opens command prompt
        say_this = 'Opening Windows Terminal'
        print(say_this)
        text2speech(say_this)
        current_app = 'cmd'
        # os.startfile(r'C:\Users\JasonPC\AppData\Local\Microsoft\WindowsApps\wt.exe')
        # os.system(r'C:\Users\JasonPC\AppData\Local\Microsoft\WindowsApps\wt.exe')
        subprocess.Popen(r'C:\Users\JasonPC\AppData\Local\Microsoft\WindowsApps\wt.exe')

    elif query in ['open discord', 'discord']: # opens Discord
        say_this = 'Opening Discord'
        print(say_this)
        text2speech(say_this)
        current_app = 'discordd'
        # os.startfile(r'C:\Users\JasonPC\AppData\Local\Discord\Update.exe')
        # os.system(r'C:\Users\JasonPC\AppData\Local\Discord\Update.exe')
        subprocess.Popen(r'C:\Users\JasonPC\AppData\Local\Discord\Update.exe')
    
    elif query in ['open steam', 'steam']: # opens Steam
        say_this = 'Opening Steam'
        print(say_this)
        text2speech(say_this)
        current_app = 'steam'
        # os.startfile(r'C:\Program Files (x86)\Steam\steam.exe')
        # os.system(r'C:\Program Files (x86)\Steam\steam.exe')
        subprocess.Popen(r'C:\Program Files (x86)\Steam\steam.exe')

    elif query in ['open calculator', 'calculator']: # opens Calculator
        say_this = 'Opening Calculator'
        print(say_this)
        text2speech(say_this)
        current_app = 'calculator'
        # os.startfile(r'C:\Windows\System32\calc.exe')
        # os.system(r'C:\Windows\System32\calc.exe')
        subprocess.Popen(r'C:\Windows\System32\calc.exe')
    
    elif query in ['open camera']: # opens Camera
        say_this = 'Opening Camera'
        print(say_this)
        text2speech(say_this)
        os.system('start microsoft.windows.camera:')
    
    elif query in ['whatsapp', 'whats app', 'whats up', "what's app", "what's up"]: # opens WhatsApp
        say_this = 'Opening WhatsApp'
        print(say_this)
        text2speech(say_this)
        current_app = 'whatsapp'
        # os.startfile(r'C:\Users\JasonPC\AppData\Local\WhatsApp\WhatsApp.exe')
        # os.system(r'C:\Users\JasonPC\AppData\Local\WhatsApp\WhatsApp.exe')
        subprocess.Popen(r'C:\Users\JasonPC\AppData\Local\WhatsApp\WhatsApp.exe')
    
    elif 'search' in query:
        say_this = rubysays('search')
        print(say_this)
        text2speech(say_this)

        # perform a google search
        to_be_searched = query.replace('search', '').lstrip()
        pwk.search(to_be_searched)
    
    elif 'play' in query:
        say_this = rubysays('youtube')
        print(say_this)
        text2speech(say_this)

        # plays a youtube video
        video_to_play = query.replace('play', '').lstrip()
        pwk.playonyt(video_to_play)
    
    elif 'information' in query: 
        # say_this = rubysays('information')
        # print(say_this)
        # text2speech(say_this)

        try:
            info = query.replace('information', '').lstrip()
            description = str(pwk.info(info))
            print(description)
            text2speech(description)

        except Exception as e:
            say_this = "Couldn't find anything on it."
            print(say_this)
            text2speech(say_this)
    
    elif 'ask' in query:
        try:
            question = query.replace('ask', '').lstrip()
            # print('You:', question)
            result = client.query(question) # returns the question's answer
            answer = next(result.results).text
            answer = str(answer)
            say_this(answer)
            print(say_this)
            text2speech(say_this)

        except Exception as e:
            say_this = "Couldn't find anything on it."
            print(say_this)
            text2speech(say_this)

    elif 'close application' in query:
        if current_app != '':
            say_this = 'Closing {}'.format(current_app)
            print(say_this)
            text2speech(say_this)
            app_to_close = apps[current_app]
            os.system("TASKKILL /F /IM {0}".format(app_to_close))
        else:
            say_this = 'No application to close.'
            print(say_this)
            text2speech(say_this)
    elif 'who is neha' in query:
        say_this = 'Neha is gandu'
        print(say_this)
        text2speech(say_this)

if __name__ == '__main__':
    # loading data.json
    f = open('data.json')  
    data = json.load(f)

    # boltiot device info {---
    API_key = "073efd14-fca5-4e97-b723-ad0db338dd87"
    Device_ID = "BOLT14000750"
    mybolt = Bolt(API_key,Device_ID)

    mybolt.digitalWrite('0','LOW')
    # ---}

    # wolframalpha {---
    app_id = 'GTPA8U-9KXWPURTE6'
    # Instance of wolf ram alpha 
    # client class
    client = wolframalpha.Client(app_id)
    # ---}

    text2speech('Hey this is Ruby!')

    while True:
        query = takeCommand().lower()

        if 'ruby' in query or 'rubi' in query:
            say_this = rubysays('greeting')
            print('You:', say_this)
            text2speech(say_this)
            startruby()
        
        if 'bye' in query or 'goodbye' in query:
            say_this = rubysays('bye')
            print(say_this)
            text2speech(say_this)
            exit()