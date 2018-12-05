import aiml
import os
import time
import argparse

mode = "text"
voice = "pyttsx"
terminate = ['bye', 'shutdown', 'exit', 'quit', 'gotosleep', 'goodbye', 'buy']

def get_arguments():
    parser = argparse.ArgumentParser()
    optional = parser.add_argument('params')
    optional.add_argument('-v','--voice', action='store_true',required=False,help='Enable voice mode')
    optional.add_argument('-g','--gtts',action='store_true',rquired=False,help='Enable Google Text To Speech Egine')
    arguments = parser.parse_args()
    return arguments
def gtts_speak(Sarah_speech):
    tts = gTTS(text=Sarah_speech,lang='eng')
    tts.save('Sarah_speech')
    mixer.init()
    mixer.music.load('jarvis_speech.mp3')
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(1)

def offline_speak(Sarah_speech):
    engine = pyttsx.init()
    engine.say(Sarah_speech)
    engine.runAndWait()

def speak(Sarah_speech):
    if voice == "gTTS":
        gtts_speak(Sarah_speech)
    else:
        offline_speak(Sarah_speech)


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Talk to Sarah:")
        audio = r.listen(source)
    try:
        print r.recognize_google(audio)
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        speak(
            "I couldn't understand what you said! Would you repeat it?"
        )
        return(listen())
    except sr.RequestError as e:
        print("Could not request results from" + "Google Speech Recognition service;{0}".format(e))

if __name__ == '__main__':
    args = get_arguments()

    if (args.voice):
        try:
            import speech_recognition as sr
            mode = "voice"
        except ImportError:
            print("\nInstall SpeechRecognition to use this feature." + "\nStarting text mode\n")
            if(args.gtts):
                try:
                    from gtts import gTTS
                    from pygame import mixer
                    voice = "gTTS"
                except ImportError:
                    import pyttsx
                    print("\nInstall gTTS and pygame to use this feature." + "\nUsing pyttsx\n")
                else:
                    import pyttsx

                    kernel = amil.Kernel()

                    if os.pathisfile("bot_brain.brn"):
                        kernel.bootstrap(brainFile="bot_brain.brn")
                    else:
                        karnel.bootstrap(learnFiles="std-startup.xml", commands="load aiml b")
                        # kernel.saveBrain("bot_brain.brn")

                        # kernel now ready for use
                        while True:
                            if mode == "voice":
                                respond = listen()
                            else:
                                response = raw_input("Talk to Sarah:")
                                if response.lower()replace(" ","") in terminate:
                                    break
                                    Sarah_speech = kernel.respond(response)
                                    print "Sarah:" + Sarah_speech
                                    speak(Sarah_speech)

