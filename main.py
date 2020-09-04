import TextToSpeech
import GetTopHeadlinesFromNewsAPI

def main(n):
    lst = GetTopHeadlinesFromNewsAPI.getTopNHeadlines(n)
    for item in lst:
        TextToSpeech.speak(f"{item[0]} News: {item[1]}")

if __name__=='__main__':
    main(5)