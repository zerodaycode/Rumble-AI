import subprocess
import os

print("Syncing Python's PIP dependencies")

''' This little module just takes care about autoconfigure this project before it starts to run '''

def sync_dependencies():
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
        'pymongo',  # Mongo DB Python's impl
        # 'pocketsphinx'  # Voice to text audio engine
    ]

    '''
        Install the packages listed on dependencies but not pyaudio. Pyaudio for Python > 3.6 it has to be manually builded,
        or installed vía the precompiled .whl file. I've included both for 3.9 version and 3.10, so it will takes the one for the
        correct Python version nowadays.
    
        The lambda expression orders the list taking 39(3.9) as a lower version than 310 (3.10) without manually changing anything.
    '''

    pip_packages = [
        f'pip install {package}' if package != "pyaudio"
        else "pip install .whl\\" + sorted(os.listdir(".whl"), key = lambda x: not x.__contains__("cp310"))[0]
        for package in dependencies
    ]

    for package in pip_packages:
        subprocess.Popen(package)


sync_dependencies()