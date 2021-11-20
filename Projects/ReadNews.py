from win32com.client.makepy import main


def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == "__main__":
    import requests
    import json

    url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=b4ed483ab94c42e1847b9c7a20b9716a'

    response = requests.get(url).text
    news = json.loads(response)
    speak(news)

