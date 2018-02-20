#import webbrowser
#webbrowser.open('http://inventwithpython.com/')
import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)
