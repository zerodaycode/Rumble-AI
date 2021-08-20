import logging
import subprocess
import threading

import pyttsx3
import speech_recognition

import time as ti
import webbrowser as we
from email.message import EmailMessage

import datetime
import os
import psutil
import pyautogui
import pyjokes
import pyttsx3
import pywhatkit
import requests
import smtplib

from src.utils.rumble_logger import Logger
from src.skills.queries_prueba import responses


class RumbleAI:
    assistant_name = "Rumble"

    def __init__(self):
        self.username = 'Álex'
        self.engine = pyttsx3.init()
        self.mic_input_device = None
        self.language = self.lang_setup()
        self.listening_th = None

    def lang_setup(self):
        return "es-ES"

    def voice_setup(self):
        voices = self.engine.getProperty('voices')
        self.engine.setProperty("voice", voices[0].id)

    def mic_setup(self):
        for index, name in enumerate(speech_recognition.Microphone.list_microphone_names()):
            print(f'Audio device with name "{name}" is the device ID = {index}`')

            while True:
                mic_id_request = input('\nPor favor, introduce uno de los números de alguno de los dispositivo\n')

                try:
                    mic_id_request = int(mic_id_request)

                    if 0 <= mic_id_request <= index:
                        self.mic_input_device = mic_id_request
                        break

                except ValueError:
                    print("Por favor, introduce un número válido")

    def rumble_talk(self, audio):
        # print(f'{RumbleAI.assistant_name} ha escuchado {audio}')
        self.engine.say(audio)
        self.engine.runAndWait()

    def rumble_listen(self):
        r = speech_recognition.Recognizer()

        query = ""

        with speech_recognition.Microphone(device_index = self.mic_input_device) as source:
            if self.listening_th is None:
                self.listening_th = threading.Thread(target = self.print_listening)
                self.listening_th.setName('Listening Thread')
                self.listening_th.start()

            r.pause_threshold = 1
            try:
                query: str = r.recognize_google(r.listen(source), language = self.language)
            except Exception as e:
                Logger.error(e)

        return query

    @staticmethod
    def print_listening():
        counter = 1
        while True:
            if counter < 2:
                Logger.info(f'Listening... Running for {counter}')
                counter += 4
            else:
                Logger.info(f'Listening... Running for {counter}')
                counter += 5

            ti.sleep(5)

    def greet(self):

        hour = datetime.datetime.now().hour

        if (hour >= 6) and (hour <= 13):
            self.rumble_talk(f"Buenos días, {self.username} como puedo ayudarte?")
        elif (hour >= 14) and (hour < 21):
            self.rumble_talk(f"Buenas tardes, {self.username} como puedo ayudarte?")
        elif (hour >= 21) and (hour <= 5):
            self.rumble_talk(f"Buenas moches, {self.username} como puedo ayudarte?")

    def run(self):
        """ The event loop of the APP """

        self.greet()  # Before anything else...

        # Permanent listening, and when we get a response, we can go to this one
        while True:

            # Getting input from the user
            query: str = self.rumble_listen().lower()
            print(f'{RumbleAI.assistant_name} ha escuchado -> ' + query)

            if query.__contains__("rumble"):
                responses(query, self)



