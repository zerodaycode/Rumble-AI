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
    def ident_message(ident_lvl):
        identation = ''
        for _ in range( ident_lvl ):
            identation += '\t'
        return identation

    @staticmethod
    def info(message, ident_lvl=0):
        identation = Logger.ident_message( ident_lvl )
        print( f'{Logger.CYAN}{identation}INFO: {message} {Logger.ENDC}' )

    @staticmethod
    def success(message, ident_lvl=0):
        identation = Logger.ident_message( ident_lvl )
        print( f'{Logger.GREEN}{identation}{message}{Logger.ENDC}' )

    @staticmethod
    def warning(message, ident_lvl=0):
        identation = Logger.ident_message(ident_lvl)
        print( f'{Logger.WARNING}{identation}WARNING: {message} {Logger.ENDC}' )

    @staticmethod
    def error(message, ident_lvl=0):
        identation = Logger.ident_message(ident_lvl)
        print( f'{Logger.FAIL}{identation}ERROR: {message} {Logger.ENDC}' )
