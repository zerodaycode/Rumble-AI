import pyttsx3

from src.persistence import database


class RumbleConfiguration:
    """ Stores the basic configuration properties """
    def __init__(self, **configuration):
        # Rumble data
        self.assistant_name = configuration['assistant_name']
        # User data
        self.username = configuration['username']
        # Voice input
        self.mic_input_device = configuration['mic_device']
        # Language related config
        self.id_language = configuration['id_language']
        self.language = self.speech_recognition_lang()
        # Stores the words that should be filtered to parse the user voice input
        self.word_filter = configuration['word_filter']

    def to_database(self):
        return {
            'assistant_name': self.assistant_name,
            'username': self.username,
            'mic_device': self.mic_input_device,
            'id_language': self.id_language,
            'word_filter': self.word_filter
        }

    # TODO Change behaviour of non instance dependent methods to @staticmethods

    def tts_engine(self):
        """ Creates a new tts engine, and sets it's initial configuration"""
        tts_engine = pyttsx3.init()

        voices = tts_engine.getProperty( 'voices' )
        tts_engine.setProperty( 'voice', voices[0].id )

        return tts_engine

    def speech_recognition_lang(self):
        """ Returns the language code for the speech recognition API """
        sr_lang = {
            1: "en-EN",
            2: "es-ES"
        }
        return sr_lang.get( self.id_language, 1 )

    def mic_setup(self):
        """ Sets the correct primary audio input device """
        # TODO Traducción de los outputs
        availiable_options = 0
        for index, name in enumerate( speech_recognition.Microphone.list_microphone_names() ):
            print( f'Dispositivo de audio: "{ name }", identificado con el ID = { index }.' )
            availiable_options += 1

            while True:
                mic_id_request = input('\nPor favor, introduce uno de los números de alguno de los dispositivo\n')
                try:
                    mic_id_request = int(mic_id_request)
                    if 0 <= mic_id_request <= availiable_options:
                        self.mic_input_device = mic_id_request
                        break
                except ValueError:
                    print('Por favor, introduce un número válido')

    @staticmethod
    def print_listening():
        """ Helper that prints a message while the speech recognition it's trying to parse an audio input"""
        counter = 1
        while True:
            Logger.info(f'Escuchando hace {counter} s.')
            counter += 1
            ti.sleep(1)
