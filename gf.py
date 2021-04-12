import datetime
import json
import logging
import os
import requests
import sys


class Form:
    def __init__(self):
        self.url = "https://docs.google.com/forms/u/2/d/e/1FAIpQLSdtsYuS1F7k5EyC6LAtPPRLMBkB_0lm8pded7rwQb61kU6XOg/formResponse"
        self.firstName = "Solomea"
        self.lastName = "Morozova"
        self.signedPerson = "Igor Morozov"
        self.school = "Oxford Elementary"
        self.submission = {'entry.1835589034': self.firstName,
                           'entry.549753788': self.lastName,
                           'entry.709320111': self.school,
                           'entry.1651259847': "No",
                           'entry.1058890283': "No",
                           'entry.366340186': "No",
                           'entry.1374099639': "No",
                           'entry.664754152': "No",
                           'entry.836067891': "No",
                           'entry.428027701': "No",
                           'entry.695115332': "No",
                           'entry.125897830': "No",
                           'entry.107425672': "No",
                           'entry.1539999785': "No",
                           'entry.2054034220' : self.signedPerson}

        self.response_code = None

    def submit(self):
        response = requests.post(self.url, self.submission)
        self.response_code = response.status_code
        print(self.response_code)


def main():
    form = Form()
    form.submit()
    
if __name__ == "__main__":
    main()
