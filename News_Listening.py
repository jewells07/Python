import requests
import json
def speak(str):
    from win32com.client import Dispatch

    speak = Dispatch("SAPI.spVoice")

    speak.Speak(str)


if __name__ == '__main__':
    speak("Today's News ")
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=b90ad3248c7f4d9cbd8991c9131950b3"
    response_intext = requests.get(url).text        #It will convert into text form
    news_dict = json.loads(response_intext)         #It will convert into python object 
    arts = news_dict['articles']                    #It will fetch the keys(articles)
    i=1
    for article in arts:                            #It will iterate and print the all values in key(articles)
        print(f"{i} {article['source']['name']}")
        i+=1

    intt=int(input("Enter number Which News Paper you want listen\n"))
    
    i=1
    for article in arts:
        if i is intt:
            print(f" {intt} {article['title']}")
            speak(article['title'])
            print(f"For more information\n{article['url']}") 
        i+=1

    speak("Thanks for listening.....")


#-------If you want to listen all News papers-------
    # i=1
    # for article in arts:
    #     print(f"{i} {article['title']}")
    #     speak(article['title'])
    #     speak("Next news is coming")
    # speak("Thanks for listening.....")
