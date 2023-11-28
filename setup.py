''' This little module just takes care about autoconfigure this project before it starts to run '''

import subprocess
import sys
import os

print("Syncing Python's PIP dependencies")

def sync_dependencies():
    ''' Handles the dependencies install '''
    dependencies = [
        "SpeechRecognition",  # For Voice commands
        "clipboard",  # For working with the clipboard
        "newsapi",  # For working with clipboard
        "newsapi-python",  # For Getting news
        "pyjokes",  # For fun
        "psutil",  # For getting compute info
        "pyaudio",  # For working with audio
        "pyautogui",  # For performing some GUI operation
        "pyttsx3",  # For Voice Interaction
        'pywhatkit',  # For WhatsApp interaction
        # 'pymongo',  # Mongo DB Python's impl
        # 'pocketsphinx'  # Voice to text audio engine
    ]

    '''
        Install the packages listed on dependencies but not pyaudio. 
        Pyaudio for Python > 3.6 it has to be manually builded, or installed vía the precompiled .whl file. 
        
        We've included both for 3.10 and 3.11 versions on the ./.whl directory.
    '''
    python_version = sys.version.split(' ', maxsplit=1)[0].replace('.', '')
    print(python_version)
    return
    pip_packages = [
        f'pip install {package}' if package != "pyaudio"
            else "pip install .whl\\" + sorted(os.listdir(".whl"), key = lambda x: x in python_version)[0]
        for package in dependencies
    ]

    for package in pip_packages:
        subprocess.Popen(package)


sync_dependencies()
