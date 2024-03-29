from flask import Flask

app = Flask(__name__)
DEBUG = True

def printLog(message):
    if DEBUG:
        print("DEBUG:",message)
