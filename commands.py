import subprocess
import os
import requests
from bs4 import BeautifulSoup
from get_answer import Fetcher

class Commander:
    def __init__(self):
        self.confirm = ["yes", "affirmative", "si", "sure", "do it", "yeah", "confirm"]
        self.cancel = ["no", "negative", "dont't", "wait", "cancel"]

    def discover(self, text):
        if "what" in text and "name" in text:
            if "my" in text:
                self.respond("You haven't told me your name yet")
            else:
                self.respond("My name is python commmander. How are you?")
        else:
            f = Fetcher("https://www.google.ie/search?q=" + text)
            answer = f.lookup()
            self.respond(answer)

    def respond(selfself, response):
        print(response)
        subprocess.call("echo '" + response, shell=True)