import pyttsx3 
import speech_recognition as sr 
import webbrowser 
import datetime 
import wikipedia
from subprocess import call
import wolframalpha
from playsound import playsound
import time
import sys
from threading import Thread
import subprocess
from pynput.keyboard import Listener
import os
import beautifulsouptest

# this method is for taking the commands 
# and recognizing the command from the 
# speech_Recognition module we will use 
# the recongizer method for recognizing
def takeCommand(): 

        r = sr.Recognizer() 

        # from the speech_Recognition module 
        # we will use the Microphone module 
        # for listening the command 
        with sr.Microphone() as source: 
                print('Listening') 
                
                # seconds of non-speaking audio before 
                # a phrase is considered complete 
                r.pause_threshold = 0.7
                audio = r.listen(source) 
                
                # Now we will be using the try and catch 
                # method so that if sound is recognized 
                # it is good else we will have exception 
                # handling 
                try: 
                        print("Recognizing")                        
                        # for Listening the command in indian 
                        # english we can also use 'hi-In' 
                        # for hindi recognizing 
                        Query = r.recognize_google(audio, language='en-in') 
                        print(Query) 
                        
                except Exception as e: 
                        print(e) 
                        print("Say that again")
                        return "None"
                
                return Query 

def speak(audio): 
        
        engine = pyttsx3.init() 
        # getter method(gets the current value 
        # of engine property) 
        voices = engine.getProperty('voices') 
        
        # setter method .[0]=male voice and 
        # [1]=female voice in set Property. 
        engine.setProperty('voice', voices[1].id) 
        
        # Method for the speaking of the the assistant 
        engine.say(audio) 
        
        # Blocks while processing all the currently 
        # queued commands 
        engine.runAndWait() 

def tellDay(): 
        
        # This function is for telling the 
        # day of the week 
        day = datetime.datetime.today().weekday() + 1
        
        #this line tells us about the number 
        # that will help us in telling the day 
        Day_dict = {1: 'Monday', 2: 'Tuesday', 
                                3: 'Wednesday', 4: 'Thursday', 
                                5: 'Friday', 6: 'Saturday', 
                                7: 'Sunday'} 
        
        if day in Day_dict.keys(): 
                day_of_the_week = Day_dict[day] 
                print(day_of_the_week) 
                speak("Today is " + day_of_the_week) 


def tellTime(): 
        
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"the time is {strTime}")   

def Hello(): 
        
        # This function is for when the assistant 
        # is called it will say hello and then 
        # take query 
        speak("Hello. How may I assist you?")
        
def waitforCancel():
        if "cancel" in takeCommand().lower():
                takeCommand()
        else:
                return()
def minimize():
        
        if "resume" in takeCommand().lower():
                Take_query()
        else:
                minimize()
        
def Take_query():
        # calling the Hello function for 
        # making it more interactive 
        Hello() 
        
        # This loop is infinite as it will take 
        # our queries continuously until and unless 
        # we do not say something to exit or terminate 
        # the program 
        while(True): 
                
                # taking the query and making it into 
                # lower case so that most of the times 
                # query matches and we get the correct 
                # output 
                query = takeCommand().lower()
                if "web" in query:
                        SeArCh = query.replace("open", "")
                        SeArCh = SeArCh.replace(" ", "")
                        speak("Opening")
                        speak(SeArCh)
                        webbrowser.open("https://www." + SeArCh)
                            
                elif "which day is it" in query: 
                        tellDay() 
                        continue
                
                elif "tell me the time" in query: 
                        tellTime() 
                        continue

                elif "what is the time" in query: 
                        tellTime() 
                        continue
                
                # this will exit and terminate the program 
                elif "bye" in query: 
                        speak("Good Bye.")
                        sys.exit()
                        
                elif "test" in query: 
                        speak("The quick brown fox jumped over the lazy dog.")
                        continue
                
                elif "exit" in query: 
                        speak("exiting")
                        sys.exit()
                        
                        # if any one wants to have information 
                        # from wikipedia
                
                elif "from wikipedia" in query:
                        try:
                                speak("Checking the wikipedia ") 
                                query = query.replace("wikipedia", "")          
                                # it will give the summary from Wikipedia 
                                result = wikipedia.summary(query, sentences=2) 
                                speak("According to wikipedia")
                                speak(result)
                        except:
                                print("An ERROR occurred")
                        else:
                                continue

                elif "wiki" in query:
                        try:
                                speak("Checking the wikipedia ")
                                #READ LIMITED TO FIRST PARAGRAPH
                                name = query.replace("wiki", "")          
                                # it will give the summary from Wikipedia 
                                result = beautifulsouptest.wikipedia(name) 
                                speak("According to wikipedia")
                                speak(result)
                        except:
                                print("An ERROR occurred")
                        else:
                                continue
                        
                elif "update" in query: 
                        speak("I am sorry, this capability isn't available yet. Please check back later.")
                        continue

                elif "version" in query: 
                        speak("I am running version 1.433 LS. Say about to get more information")
                        continue

                elif "about" in query:
                        speak("Currently I am running version 1.4 revision 3 feature update 3 Limited Support beta version.")

                elif "play me a song" in query: 
                        speak("Running song chooser program.")
                        subprocess.call("musicplayer.py", shell=True)
                        
                elif "search" in query:
                        SearchQuery = query.replace("search", "")
                        speak("Searching")
                        speak(SearchQuery)
                        webbrowser.open("https://duckduckgo.com/?q=" + SearchQuery)
                        continue

                elif "minimize" in query:
                        speak("Minimizing")
                        minimize()

                elif "open" in query:
                        program = query.replace("open", "")
                        speak("Opening" + program)
                        openprogram.open(program)
                        #Call minimize to minimize the program so you don't get interupted
                        minimize()
                        continue

                elif "text" in query:
                        program = input("Enter program to open: ")
                        print(program + ".exe")
                        os.system(program + ".exe")
                        speak("Running text mode")

                else:
                        continue
if __name__ == '__main__': 
        # main method for executing 
        # the functions 
        Take_query()
