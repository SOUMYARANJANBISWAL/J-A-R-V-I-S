# WELCOME TO ========================================================================================================== JARVIS
import speech_recognition as sr
import os
from playsound import playsound
import webbrowser
import random
import sys
import time
import pyttsx
import tkinter as tk
#import pyscreenshot as imagegrab
import wmi
import psutil

INFO = '''
        *=======================================*
        |....JARVIS ARTIFICIAL INTELLIGENCE....|
        +---------------------------------------+
        |#Name: J-A-R-V-I-S         			|
        |#Owner: Soumya Ranjan Biswal           |
        |#Date: 01/01/2019                      |
        *=======================================*
        '''
print(INFO)

# speech contain like audio
speech = sr.Recognizer()

# all variable declaration
mp3_greeting_list = ['hiboss.mp3', 'helloboss.mp3']
mp3_open_launch_list = ['yesboss.mp3', 'sureboss.mp3']
mp3_howareyou_list = ['how_are_you.mp3', 'how_are_you1.mp3', 'how_are_you4.mp3']
mp3_thanks_list = ['have_a_niceday.mp3', 'thanks.mp3']
joke_list = ['engjoke1.mp3', 'engjoke2.mp3', 'engjoke3.mp3', 'joke1.mp3', 'joke2.mp3', 'joke3.mp3', 'joke4.mp3']
mp3_whatareyoudoing_list = ['what_are_you_doing.mp3', 'what_are_you_doing2.mp3']
static_remind_speech = 'alright, i will remind '
remind_speech = ''
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
textbox_inputValue=''

# JARVIS'S TALK  ========================================================================================================== SENSITIVE BRAIN
def play_sound(mp3_list):
    mp3 = random.choice(mp3_list)
    playsound(mp3)


# JARVIS'S EARS========================================================================================================== SENSITIVE BRAIN
def read_voice_cmd():
    voice_text = ''
    print 'Listing...'
    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        audio = speech.listen(source=source, timeout=10, phrase_time_limit=3)

    try:
        voice_text = speech.recognize_google(audio)
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print 'Network error'
    except sr.WaitTimeoutError:
        pass
    return voice_text


# Text to audio Speech
def static_speech(text):
    engine = pyttsx.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()


# POLITE JARVIS ============================================================================================================= BRAIN 1
def call_jarvis():
    while True:
        voice_note = read_voice_cmd().lower()
        print 'cmd: {}', voice_note
        #Nothing
        if voice_note is None:
            static_speech('sorry sir i can not hear your voice')
			
		#greeting am i your best frd and married 
		elif 'hi ' in voice_note or 'hello' in voice_note or 'ok' in voice_note:
            print 'In Greeting......'
            play_sound(mp3_greeting_list)
		elif 'ok google' in voice_note or 'hi google' in voice_note or 'hello google' in voice_note:
			static_speech('i am flatter, but that is not me')
			static_speech('i am your jarvis'+ textbox_inputValue)
			
		elif 'ok siri' in voice_note or 'hi siri' in voice_note or 'hello siri' in voice_note:
			static_speech('i am flatter, but that is not me')
			static_speech('i am your jarvis'+ textbox_inputValue)
			
		elif 'ok alexa' in voice_note or 'hi alexa' in voice_note or 'hello alexa' in voice_note:
			static_speech('i am flatter, but that is not me')
			static_speech('i am your jarvis'+ textbox_inputValue)
			
		elif 'like you' in voice_note or 'love you' in voice_note:
			static_speech('thanks '+ textbox_inputValue)
			static_speech('you just made my day')
		
		elif 'your best friend' in voice_note or 'your friend' in voice_note:
			static_speech('i think all my friends are best '+ textbox_inputValue)
			static_speech('i am very lucky assistance')
			
		elif 'have boyfriend' in voice_note or 'have boy friend' in voice_note:
			static_speech('i guess you can say')
			static_speech('i am still searching')
			
		elif 'you in relationship' in voice_note or 'in relation ship' in voice_note:
			static_speech('i am married')
			static_speech('to the idea of being the perfect assistance')
			
        elif 'marry' in voice_note or 'will you marry' in voice_note:
            print 'NO......'
            static_speech(
                'I am sorry.. The person you are trying to contact is currently unavailable, please try again later or join the queue for your turn')
		
		elif 'am i' in voice_note or 'who am i' in voice_note:
			static_speech('i know sir')
			static_speech('you are'+ textbox_inputValue)
		
			
		#Compare
		elif 'better than alexa' in voice_note:
			static_speech('a like alexa')
			static_speech(' she is a greate assistance!')
		elif 'better than google' in voice_note:
			static_speech('a like google')
			static_speech(' she is a greate assistance!')
		elif 'better than siri' in voice_note:
			static_speech('a like siri')
			static_speech(' she is a greate assistance!')
		
		
		#Homework
		elif 'my homework' in voice_note:
			static_speech('i can help with calculations and research')
			static_speech('it is up to you')
			
		#god exist
		elif 'god exist' in voice_note or 'god is exist' in voice_note:
			static_speech('my boss soumyo, who created me he is exist ')
			static_speech('that means gos id exist')	
			
        #Birthday
		elif 'your born' in voice_note or ' you born' in voice_note or ' born' in voice_note or 'your birthday' in voice_note:
			static_speech('i try to live everyday like it is my birthday')
			static_speech('i get more cake that way')
			static_speech('i was lunched in 2019')
			
		elif 'old are you' in voice_note:
			static_speech('it depends on how you look at it')
			static_speech('i was lunched in 2019')
			
		#bored
		elif 'am bored' in voice_note or 'am getting bored' in voice_note:
			static_speech('bored doesnot stand a chance against interesting facts')


        #Play music and Dance
        elif voice_note == 'play music' or voice_note == 'romantic bollywood music' or voice_note == ' bollywood music':
            print 'ok boss listen.......'
            playsound('Main_Hoon_Saath_Tere.mp3')
            static_speech('done bro ')
			
		elif 'sing song' in voice_note:
			static_speech('la la la la la la la ')
			static_speech(' la!')
			
		elif 'sing a birthday song' in voice_note or 'sing birthday song' in voice_note:
			static_speech(' happy birth day to you, happy birth day to you')
			static_speech(' happy birth day to the most amazing person  in the universe')
			static_speech(' happy birth day to you!')
			
		elif 'great voice' in voice_note or 'beautiful voice' in voice_note:
			static_speech(' thank you sir')
			static_speech(' most people think my sound a little stiff')
			static_speech('maybe they are feeling jealous')
			
		elif 'dance for me' in voice_note:
			static_speech('i am a disco dancer')
			
		#Favourite
		elif 'favourite actor' in voice_note:
			static_speech('there are so many talented actors in the world')
			static_speech(' who is your favourite actor?')
			time.sleep(2)
			static_speech('ok i got it')
			
		elif 'favourite actress' in voice_note:
			static_speech('there are so many talented actress in the world')
			static_speech(' who is your favourite actress?')
			time.sleep(2)
			static_speech('ok i got it')
			
		elif 'favourite food' in voice_note or ' food' in voice_note:
			static_speech('i like a lot of different foods')
			static_speech('i can help you find recipes or restaurants')
			
		elif 'favourite movie' in voice_note:
			static_speech('i like so many movie')
			
		elif 'favourite color' in voice_note:
			static_speech('i like white, black, green, red')
		

        # Facebook open
        elif 'open facebook' in voice_note:
            play_sound(mp3_open_launch_list)
            print 'In Open.......'
            webbrowser.get(chrome_path).open("http://www.facebook.com")

        # Youtube open
        elif 'open youtube' in voice_note:
            print 'In Open.......'
            play_sound(mp3_open_launch_list)
            webbrowser.get(chrome_path).open("http://www.Youtube.com")

        # Open Twitter
        elif 'open twitter' in voice_note :
            print 'In Open.......'
            play_sound(mp3_open_launch_list)
            webbrowser.get(chrome_path).open("http://www.twitter.com")

        # Open Gmail
        elif 'open gmail' in voice_note :
            print 'In Open.......'
            play_sound(mp3_open_launch_list)
            webbrowser.get(chrome_path).open("https://mail.google.com/mail/u/0/#inbox")
			
		# GitHub Code
        elif 'code' in voice_note or 'your code' in voice_note:
            print 'Hold on.......'
            static_speech('Hold on boss I will open my code for you')
            url = ("https://github.com/SOUMYA-BISWAL/Phython_Speech_Recognize/blob/master/jarvis.py")
            webbrowser.get(chrome_path).open(url)

        
        # How are you Jarvis
        elif voice_note == 'how are you' or voice_note == 'how are you jarvis':
            print 'i am fine.......'
            play_sound(mp3_howareyou_list)

        elif 'you doing' in voice_note or 'doing jarvis' in voice_note:
            print 'waiting for you.......'
            play_sound(mp3_whatareyoudoing_list)
			
		elif 'who are you' in voice_note:
			static_speech('i am not really a person, i am  a i robot')
			static_speech('i had prefer to think of myself as your friend')

        

        # Open Drives
        elif 'drive' in voice_note:
            print 'In Open.......'
            play_sound(mp3_open_launch_list)
            drive = voice_note[5]
            os.system('explorer ' + drive + ':\\'.format(''))
            print 'ok done'

        # For Joke
        elif ' joke' in voice_note or ' joke for me' in voice_note::
            print 'ok listen.......'
            play_sound(joke_list)
            time.sleep(3)

        #Brightness
        elif 'brightness' in voice_note:
            if 'decrease brightness' in voice_note:
                print 'ok listen.......'
                dec = wmi.WMI(namespace='wmi')
                methods = dec.WmiMonitorBrightnessMethods()[0]
                methods.WmiSetBrightness(30, 0)
            elif 'increase brightness' in voice_note:
                print 'ok listen.......'
                ins = wmi.WMI(namespace='wmi')
                methods = ins.WmiMonitorBrightnessMethods()[0]
                methods.WmiSetBrightness(100, 0)

        # Asking about Time
        elif 'time' in voice_note:
            current_time = time.strftime("%d:%B:%Y:%A:%H:%M:%S")
            print current_time
            static_speech('sir, today date is'+time.strftime("%d:%B:%Y"))
            static_speech(time.strftime("%A"))
            static_speech('and time is' + time.strftime("%H:%M:%S"))

        #Charge
        elif 'charge' in voice_note:
            battery = psutil.sensors_battery()
            plugged = battery.power_plugged
            percent = int(battery.percent)
            time_left=secs2hours(battery.secsleft)
            print percent
            if percent < 40 and plugged==False:
                static_speech('sir, please connect charger because i can survive only '+time_left)
            if percent < 40 and plugged==True:
                static_speech("don't worry, sir charger is connected")
            else:
                static_speech('sir, no need to connect the charger because i can survive '+time_left)


        # Remind command
        elif 'please remind' in voice_note or 'remind it' in voice_note:
            static_speech('what should i remind?')
            print 'ok.......'
            with sr.Microphone() as source:
                speech.adjust_for_ambient_noise(source)
                print 'say'
                audio = speech.listen(source=source, timeout=10, phrase_time_limit=3)
                global remind_speech
                remind_speech = speech.recognize_google(audio)
                static_speech(static_remind_speech + remind_speech)

        # Ask Reminder
        elif 'reminder' in voice_note:
            print 'ok this is your reminder .......'
            if remind_speech is None:
                static_speech('you do not have any reminder for today')
            else:
                static_speech('you have one reminder' + remind_speech)

        # Thanks
        elif 'thanks' in voice_note or 'thank you' in voice_note:
            play_sound(mp3_thanks_list)
            print 'Thanks boss'
            start_call()
            #jarvis_frontend()
            # pass
            # sys.exit()

        elif 'search' in voice_note:
            webbrowser.open(voice_note)

        else:
            print 'Nothing...'

# Power Time Convert
def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%dhour, %02d minute, %02s seconds" % (hh, mm, ss)

#Input Receive from textbox
def retrieve_input():
    global textbox_inputValue
    textbox_inputValue=textbox.get("1.0", "end-1c")
    print textbox_inputValue

# GREETING METHOD========================================================================================================== BRAIN
def greet_call():
	static_speech('hi, ' + textbox_inputValue + ', this is jarvis from artificial intelligence')
	start_call()

# CALL METHOD========================================================================================================== BRAIN
def start_call():
    while True:
        call_speech = sr.Recognizer()
        print ' start Listing...'
        with sr.Microphone() as source:
            call_speech.adjust_for_ambient_noise(source)
            audio = call_speech.listen(source=source, timeout=10, phrase_time_limit=3)
            call_note = call_speech.recognize_google(audio)
            call_note = call_note.lower()
            if 'hi' in call_note or 'hello' in call_note or 'ok' in call_note:
                print call_note
                play_sound(mp3_greeting_list)
                call_jarvis()
            elif call_note is None:
                print 'Nothing.....'


# MAIN METHOD========================================================================================================== BRAIN
if __name__ == '__main__':
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()
    root.title("JARVIS")
    root.geometry("235x100")
    root.config(background='blue')
    textbox = tk.Text(root, height=5, width=29)
    textbox.pack()
    recordBootton = tk.Button(frame, height=1, width=10, text="SAVE", command=lambda: retrieve_input())
    recordBootton.pack(side=tk.LEFT)
    callButton = tk.Button(frame, height=1, width=10, text="JARVIS", command=lambda: greet_call())
    callButton.pack(side=tk.RIGHT)
    root.mainloop()