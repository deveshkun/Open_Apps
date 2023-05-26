import webbrowser
from AppOpener import open

def openfb():
    webbrowser.open('https://facebook.com')

def openinsta():
    webbrowser.open('https://instagram.com')

def open_youtube():
    webbrowser.open('https://youtube.com')

def openwhasap():
    open("whatsapp",match_closest=True)

def syssetting():
    open("settings",match_closest=True)

def chrome():
    open("google chrome")

def explorer():
    open("explorer",match_closest=True)

def thispc():
    open("this pc",match_closest=True)

def openstore():
    open("microsoft store")

def camera():
    open("camera")
