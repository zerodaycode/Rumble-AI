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
# import pywhatkit
import requests
import smtplib

from .skills_registry import SkillsRegistry
from src.utils.rumble_logger import Logger
from .core_exceptions.skills_exceptions import NoSkillFound


class RumbleAI:
    """ The Rumble AI core """
    def __init__(self, config):
        # Rumble set-up
        self.config = config
        # The text to speech engine
        self.engine = config.tts_engine()
        # AI skills
        self.skills = SkillsRegistry( self.config.id_language )
        # Flag to contorl when Rumble it's listening
        self.listening = False
        self.counter = 0  # Controls when the listening message it's printed 

        # Data that it's passed to the "now playing" skill
        self.extra_data = {
            'username': self.config.username,
            'keywords': [],  # SHOULD NOT BE NECESSARY. Pass the query again it's better, and any plugin can
            # parse it again according to it's needs
            'query': ''
        }

    def talk(self, audio):
        """ The Rumble ability to talk. Send audio based on text """
        self.engine.say( audio )
        self.engine.runAndWait()

    def listen(self):
        """ The Rumble capacity to listen. It parses the audio input to perform an AI based action """
        r = speech_recognition.Recognizer()
        query = ""

        with speech_recognition.Microphone( device_index = self.config.mic_input_device ) as source:
            # Just for printing a warning that the program it's listening forinput
            # listening_th = multiprocessing.Process(target=self.print_listening)
            self.listening = True
            listening_th = threading.Thread( target=self.print_listening )
            listening_th.start()
            
            # TODO move the configuration of the SR to the config class
            r.pause_threshold = 0.5
            r.adjust_for_ambient_noise( source )
            r.energy_threshold = 2000
            try:
                print('Listening...')
                init_time = int(round(ti.time() * 1000))
                query: str = r.recognize_google( r.listen( source ), language = self.config.language )
                end_time = int(round(ti.time() * 1000))
                Logger.info( f'It tooks { (end_time - init_time) }ms listening until we got an audio')
            except speech_recognition.UnknownValueError as error:
                Logger.error( f'It has been imposible to understand the input audio.\n{ error }' )
            
            self.listening = False
            listening_th.join()
            print('\nThe print listening thread has successfully joined the main one!')

        return query

    def run(self):
        """ The event loop of the APP """
        # self.skills.match_skill( ['saludar'] ).play(
        #     self, **{ 'username': self.username }
        # )  # Before anything else...

        # Permanent listening, and when we get a response, we can go to this one
        while True:
            # Getting input from the user
            try:
                user_query: str = self.listen().lower()
                keywords = list(
                    filter(
                        lambda word: word not in self.config.word_filter,
                        user_query.split()
                    )
                )
                self.extra_data.update( { 'keywords': keywords } )
                self.extra_data.update( { 'query': user_query } )

                if user_query != '':
                    Logger.info( f'{ self.config.assistant_name.title() } has listened -> ' + user_query )

                if user_query.__contains__( self.config.assistant_name.lower() ):
                    response = self.skills.match_skill( keywords )
                    try:
                        if response is not None:
                            response.play( self, **self.extra_data )
                        else:
                            raise NoSkillFound( user_query )
                    except NoSkillFound as error:
                        Logger.warning( error, 2 )
                        self.talk( f'Lo siento { self.config.username }, '
                                   f'pero no he entendido lo que me has pedido' )

            except KeyboardInterrupt:
                # Program stopped by Ctrl + C or IDE's stop button
                print()
                self.listening = False
                Logger.warning( f'Program manually stopped by the user: { self.config.username }' )
                sys.exit()

    def print_listening(self):
        while self.listening:
            if self.counter > 9000000:  # This value changes from machine to machine
                print('Listening...')
                self.counter = 0
            else:
                self.counter += 1