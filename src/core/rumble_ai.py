import multiprocessing
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
from .core_exceptions.skills_exceptions import NoSkillFound


class RumbleAI:
    assistant_name = "Rumble"

    def __init__(self):
        self.username = 'Álex'
        self.assistant_name = RumbleAI.assistant_name.lower()

        # Provisional -- TODO -- class Config?
        self.engine = pyttsx3.init()
        self.mic_input_device = None
        self.language = self.lang_setup()
        self.id_language = 2
        # self.mic_setup()

        # AI skills
        self.skills = SkillsRegistry( self.id_language )

        self.word_filter = [
            self.assistant_name,  # ... TODO --- Complete it
            'a', 'para', 'cabe',
        ]
        self.extra_data = {
            'username': self.username,
            'keywords': []
        }

    @staticmethod
    def lang_setup():
        return "es-ES"  # TODO Config file -- class

    def voice_setup(self):
        voices = self.engine.getProperty( 'voices' )
        self.engine.setProperty( 'voice', voices[0].id )

    def mic_setup(self):
        availiable_options = 0
        for index, name in enumerate( speech_recognition.Microphone.list_microphone_names() ):
            print( f'Dispositivo de audio: "{ name }", identificado con el ID = { index }.' )
            availiable_options += 1

        while True:
            mic_id_request = input( '\nPor favor, introduce uno de los números de alguno de los dispositivo\n' )
            try:
                mic_id_request = int( mic_id_request )
                if 0 <= mic_id_request <= availiable_options:
                    self.mic_input_device = mic_id_request
                    break
            except ValueError:
                print( 'Por favor, introduce un número válido' )

    def talk(self, audio):
        self.engine.say( audio )
        self.engine.runAndWait()

    def listen(self):
        r = speech_recognition.Recognizer()

        query = ""

        with speech_recognition.Microphone( device_index = self.mic_input_device ) as source:
            # Just for printing a warning that the program it's listening for audui input
            # listening_th = multiprocessing.Process(target=self.print_listening)
            # listening_th.start()

            r.pause_threshold = 1
            try:
                query: str = r.recognize_google( r.listen( source ), language = self.language )
            except speech_recognition.UnknownValueError as error:
                Logger.error( f'No ha sido posible reconocer el audio de entrada.\n{ error }' )
            # listening_th.terminate()
        return query

    @staticmethod
    def print_listening():
        counter = 1
        while True:
            Logger.info( f'Escuchando hace { counter } s.' )
            counter += 1
            ti.sleep(1)

    def run(self):
        """ The event loop of the APP """
        self.skills.match_skill( ['saludar'] ).play(
            self, **{ 'username': self.username }
        )  # Before anything else...

        # Permanent listening, and when we get a response, we can go to this one
        while True:
            # Getting input from the user
            try:
                user_query: str = self.listen().lower()
                keywords = list(
                    filter(
                        lambda word: word not in self.word_filter,
                        user_query.split()
                    )
                )
                self.extra_data.update( { 'keywords': keywords } )

                if user_query != '':
                    Logger.info( f'{ self.assistant_name.title() } ha escuchado -> ' + user_query )

                if user_query.__contains__( self.assistant_name ):
                    response = self.skills.match_skill( keywords )
                    try:
                        if response is not None:
                            response.play( self, **self.extra_data )
                        else:
                            raise NoSkillFound( user_query )
                    except NoSkillFound as error:
                        Logger.warning( error, 2 )
                        self.talk( f'Lo siento { self.username }, '
                                   f'pero no he entendido lo que me has pedido' )

            except KeyboardInterrupt:
                # Program stopped by Ctrl + C or IDE's stop button
                print()
                Logger.warning( f'Program manually stopped by the user: { self.username }' )
                sys.exit()
