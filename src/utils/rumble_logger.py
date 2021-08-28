class Logger:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    CYAN = '\033[36m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'

    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    ENDC = '\033[0m'

    @staticmethod
    def info(message):
        print(f'{Logger.CYAN}INFO: {message} {Logger.ENDC}')

    @staticmethod
    def warning(message):
        print(f'{Logger.WARNING}WARNING: {message} {Logger.ENDC}')

    @staticmethod
    def error(message):
        print(f'{Logger.FAIL}ERROR: {message} {Logger.ENDC}')
