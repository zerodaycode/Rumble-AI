import logging
import subprocess
import sys
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

from .skills_registry import SkillsRegistry
from src.utils.rumble_logger import Logger


class RumbleAI:
    assistant_name = "Paco"

    def __init__(self):
        self.username = 'Alma'
        self.assistant_name = RumbleAI.assistant_name.lower()

        # Provisional -- TODO -- class Config?
        self.engine = pyttsx3.init()
        self.mic_input_device = None
        self.language = self.lang_setup()
        # self.listening_th = None
        self.id_language = 2

        # AI skills
        self.skills = SkillsRegistry( self.id_language )

    @staticmethod
    def lang_setup():
        return "es-ES"  # TODO Config file -- class

    def voice_setup(self):
        voices = self.engine.getProperty('voices')
        self.engine.setProperty("voice", voices[0].id)

    def mic_setup(self):
        for index, name in enumerate(speech_recognition.Microphone.list_microphone_names()):
            print(f'Dispositivo de audio: "{name}", identificado con el ID = {index}`.')

            while True:
                mic_id_request = input('\nPor favor, introduce uno de los números de alguno de los dispositivo\n')
                try:
                    mic_id_request = int(mic_id_request)
                    if 0 <= mic_id_request <= index:
                        self.mic_input_device = mic_id_request
                        break
                except ValueError:
                    print("Por favor, introduce un número válido")

    def talk(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    def listen(self):
        r = speech_recognition.Recognizer()

        query = ""

        with speech_recognition.Microphone(device_index = self.mic_input_device) as source:
            # if self.listening_th is None:
            #     self.listening_th = threading.Thread(target = self.print_listening)
            #     self.listening_th.setName('Listening Thread')
            #     self.listening_th.start()

            r.pause_threshold = 1
            try:
                query: str = r.recognize_google(r.listen(source), language = self.language)
            except speech_recognition.UnknownValueError as e:
                Logger.error(f'No ha sido posible reconocer el audio de entrada.\n{e}')

        return query

    @staticmethod
    def print_listening():
        counter = 1
        while True:
            if counter < 2:
                Logger.info(f'Escuchando... Programa activo desde hace {counter} s.')
                counter += 4
            else:
                Logger.info(f'Listening... Programa activo desde hace {counter} s.')
                counter += 5

            ti.sleep(5)

    def run(self):
        """ The event loop of the APP """
        self.skills.match_skill('saludar').play(
            self, **{ 'username': self.username }
        )  # Before anything else...

        # Permanent listening, and when we get a response, we can go to this one
        while True:
            # Getting input from the user
            try:
                query: str = self.listen( ).lower( )
                # query: str = "paco, qué hora es"
                Logger.info(
                    f'{self.assistant_name.title()} ha escuchado -> ' + query)

                extra_data = {
                    'username': self.username,
                    'query': query
                }

                if query.__contains__(self.assistant_name):
                    response = self.skills.match_skill( query )
                    response.play( self, **extra_data )

            except KeyboardInterrupt:
                # Program stopped by Ctrl + C or IDE's stop button
                Logger.warning(f'Program stopped by the user: { self.username }')
                sys.exit()
