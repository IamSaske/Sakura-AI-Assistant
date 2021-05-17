import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import os
import random
import requests,json
def speak(audio):  #for champa to speak
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon")
    elif hour >= 18 and hour <= 24:
        speak("Good Evening")
def takecommand():#Iy will take command interms of voice from you
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1#it will wait for a sec if speaker takes gap for sec
        audio=r.listen(source)
    try:
        print("Recogninizing...")#try recognizing
        query=r.recognize_google(audio,language='en.-in')#we are using google recognizer
        #You will need internet for this

        print(f"User said {query}\n")
    except Exception as e:
        print(e)

        print("Say that again please..")
        return "None"
    return query

if __name__ == '__main__':
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    print(voices[1].id)
    engine.setProperty('voice', voices[1].id)
    newVoiceRate = 150  # voice speed
    engine.setProperty('rate', newVoiceRate)

    speak("Hi, i am Sakura , How i can help you?")
    wishme()

    # logic to run program
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia.....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)  # how many sentence sakura will read
            speak('According to wikipedia...')
            print(results)
            speak(results)
        elif 'open youtube' in query:  # browser opening
            webbrowser.open("youtube.com")

        elif 'open amazon' in query:
            webbrowser.open("amazon.com")

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open twitter' in query:
            webbrowser.open("twitter.com")

        elif 'find me girlfriend' in query:
            webbrowser.open("tinder.com")

        elif 'find me new job' in query:
            webbrowser.open("linkedin.com")
        elif 'play music' in query:
            music_dir = "D:\music"
            songs = os.listdir(music_dir)
            j = random.choice(songs)
            print(j)

            os.startfile(os.path.join(music_dir, j))
        elif 'tell me about weather' in query:

            # Enter your API key here

            api_key = "xxxx"

            # base_url variable to store url

            base_url = "http://api.openweathermap.org/data/2.5/weather?"

            # Give city name
            speak("Type your city name ")
            city_name = input("enter city name:")

            # complete_url variable to store
            # complete url address

            complete_url = base_url + "appid=" + api_key + "&q=" + city_name

            # get method of requests module
            # return response object

            response = requests.get(complete_url)

            # json method of response object
            # convert json format data into
            # python format data

            x = response.json()

            # Now x contains list of nested dictionaries
            # Check the value of "cod" key is equal to
            # "404", means city is found otherwise,
            # city is not found

            if x["cod"] != "404":

                # store the value of "main"

                # key in variable y

                y = x["main"]

                # store the value corresponding

                # to the "temp" key of y

                current_temperature = y["temp"]

                # store the value corresponding

                # to the "pressure" key of y

                current_pressure = y["pressure"]

                # store the value corresponding

                # to the "humidity" key of y

                current_humidiy = y["humidity"]

                # store the value of "weather"

                # key in variable z

                z = x["weather"]

                # store the value corresponding

                # to the "description" key at

                # the 0th index of z

                weather_description = z[0]["description"]

                # print following values

                results = (" Temperature (in kelvin unit) = " +

                           str(current_temperature) +

                           "\n atmospheric pressure (in hPa unit) = " +

                           str(current_pressure) +

                           "\n humidity (in percentage) = " +

                           str(current_humidiy) +

                           "\n description = " +

                           str(weather_description))
                speak(results)
                print(results)
            else:
                speak("city not found")

            pass
        elif 'what is time' in query:
            strtime = datetime.datetime.now().strftime("%H%M%S")
            speak(f"Sir,the time is {strtime}")
        elif 'tell me a joke' in query:
            list = [" Where should a 500 pound alien go?... On a diet",
                    "What did one toilet say to the other? .. You look a bit flushed",
                    " Why did the picture go to jail?.. Because it was framed",
                    "What did one wall say to the other wall?.. I'll meet you at the corner",
                    "What did the paper say to the pencil?.. Write on",
                    "Why do bicycles fall over?.. Because they are two-tired!",
                    " Why do dragons sleep during the day?.. So they can fight knights!",
                    " What part of the car is the laziest?.. The wheels, because they are always tired!"]
            i = random.choice(list)
            speak(i)
        elif 'good job' in query:
            speak("thanks")
        elif 'how are you' in query:
            speak(" i am fine")


