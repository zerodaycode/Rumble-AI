import os

from src.utils.rumble_logger import Logger
from src.core.core_exceptions.plugin_exceptions import NotValidPluginFound, NoInheritsFromSkill
from src.core.core_exceptions.skills_exceptions import SkillNotContainsNameParameter, SkillNamesListWrongLength


class PluginsRegistry:
    """
        Takes care about handle a way to store and retrieve all the Rumble's availiable plugins.
        Provides a way to get new plugins from outside (internet, ex: GitHub repo), to handle it's
        validation as a Rumble skill...
    """

    def __init__(self):
        self.root_plugins_dir = 'src/plugins/'
        self.plugins: list = [ ]

        # Auto-scan for plugins every new fresh start
        self.scan_plugins_directory()

    @property
    def get_plugins(self) -> list:
        return self.plugins

    def scan_plugins_directory(self) -> None:
        """ Looks for plugins on the plugins folder """
        current_dir_level = ''

        Logger.info('Looking for availiable plugins:')
        for plugin_dir_name in os.listdir( self.root_plugins_dir ):

            if os.path.isdir( current_dir_level := self.root_plugins_dir + plugin_dir_name ):
                plugin_identifier = PluginsRegistry._validate_plugin( plugin_dir_name, current_dir_level )

                if plugin_identifier is not None:
                    if plugin_identifier not in self.plugins:
                        self.plugins.append( plugin_identifier )
                        Logger.success( f'Valid plugin founded! -> { list( plugin_identifier.keys() )[ 0 ] }', 3 )
                    else:
                        Logger.warning( f'Plugin already tracked! -> { list( plugin_identifier.keys() )[ 0 ] }', 3 )

    @staticmethod
    def _validate_plugin(plugin_dir_name: str, current_dir_level: str ) -> str:
        """ Founded a plugin candidate on plugins folder, validates if it's OK to be added as a Rumble skill """
        print( '\t' + f'Plugin candidate on directory: { plugin_dir_name }' )
        if PluginsRegistry._validate_plugin_folder_name( plugin_dir_name ):
            print( '\t\t' + f'{ plugin_dir_name } is a valid folder name' )

            for filename in os.listdir( current_dir_level ):
                print( '\t\t\t' + f'File { filename } ON { plugin_dir_name }' )

                if PluginsRegistry._validate_plugin_file_name( filename ):
                    file_path = current_dir_level + f'/{ filename }'

                    if identifier := PluginsRegistry._validate_file( file_path ):
                        return identifier

    @staticmethod
    def _validate_plugin_folder_name(plugin_dir_name: str) -> bool:
        """ Validates that the plugin's folder name follows the convention to be added as a skill """
        dirname_splitted = plugin_dir_name.split( "_" )
        if dirname_splitted[ len( dirname_splitted  ) - 1 ] == 'plugin':
            return True

    @staticmethod
    def _validate_plugin_file_name(filename: str) -> bool:
        """
            Validates that the main plugin's filename follows the convention to be added as a skill
            ('main file' here means the file which stores the main class that represents entry point of the skill)
        """
        filename_splitted = filename.split( "_" )
        if filename_splitted[ len( filename_splitted ) - 1 ] == 'plugin.py':
            print( '\t\t\t' + f'{ filename } is a valid filename' )
            return True

    @staticmethod
    def _validate_file(filepath: str) -> str:
        """
            Verifies that the structure imposed on a plugin class is met.
            After this, if all imposed criteria are met, returns a dict with the plugin's class identifier,
            and parses the file looking for the necessary attrs of the inner dict (name, description and tags)
            in order to be added on the skills registry
        """
        contains_class: bool = False
        contains_valid_name_param: bool = False
        contains_valid_description_param: bool = False
        contains_valid_tags_param: bool = False

        class_identifier: str = ''
        name_param: str = ''
        description_param: str = ''
        english_tags: list[str] = []
        spanish_tags: list[str] = []

        with open( filepath, 'r' ) as plugin_file_class:  # Reads the plugin's main class file
            for line_number, line in enumerate( plugin_file_class.readlines() ):
                line_number += 1
                line = line.strip( '\n' )  # Avoid unnecessary line breaks

                if line_number == 3:  # Were should live the name attr
                    contains_valid_name_param = PluginsRegistry._validate_name_attr( line )
                    # Retrieves the list with the skill names
                    name_param = line.strip('\n')\
                        .split( 'name: list[str] = [' )[ 1 ]\
                        .replace( ']', '' )\
                        .replace( "'", '' )\
                        .strip()\
                        .split( ', ' )

                # TODO Creates custom exception for each field
                if line.__contains__( 'description' ) and line_number == 4:  # Were should live the description attr
                    contains_valid_description_param = True
                    Logger.success( 'Validated description', 4 )
                    # Retrieves the description attr by parsing the line
                    description_param = line.split( '=' )[ 1 ].strip().replace( "'", '' )

                if line.__contains__( 'tags' ) and line_number == 5:  # Were should live the tags attr
                    if line.split( '=' )[ 0 ].rstrip() == 'tags: dict':
                        contains_valid_tags_param = True
                        Logger.success( 'Validated tags', 4 )

                # Retrieves the list of tags by language
                if line.__contains__( 'english' ):
                    english_tags = PluginsRegistry._retrieve_skill_tags_from_plugin( line )
                if line.__contains__('spanish'):
                    spanish_tags = PluginsRegistry._retrieve_skill_tags_from_plugin( line )

                if line.__contains__( 'class' ):
                    contains_class = True
                    # Validates the class identifier
                    class_identifier = PluginsRegistry._validate_class_identifier( line )

        try:
            if contains_class and contains_valid_name_param and contains_valid_description_param\
                    and contains_valid_tags_param:

                import importlib
                fmt_path = filepath.replace( '/', '.')[:-3]
                module = importlib.import_module( fmt_path )
                class_identifier = getattr( module, class_identifier )

                return {
                    class_identifier: {
                        'name': name_param,
                        'description': description_param,
                        'tags': {
                            'english': english_tags,
                            'spanish': spanish_tags
                        }
                    }
                }
            else:
                raise NotValidPluginFound( class_identifier )
        except NotValidPluginFound as error:
            Logger.error( error, 3)

    @staticmethod
    def _validate_class_identifier(line: str) -> str:
        """
            Finds the line where the class signature lives, and parses it, ensuring that it's
            meeting the stablished criteria, like 'should inherit' from Skill abstract base class.
        """
        class_signature_elements = line.split( ' ' )
        class_keyword = class_signature_elements[ 0 ]  # Should be the class keyword
        class_identifier = class_signature_elements[ 1 ]  # Should be the class name

        try:
            # Checks that the plugin inherits from the abstract base class Skill
            if class_identifier.__contains__( '(Skill)' ):
                return class_identifier.split( '(' )[ 0 ]
            else:
                raise NoInheritsFromSkill(
                    class_identifier.split('(')[ 0 ].strip(':') + ' class'
                )
        except NoInheritsFromSkill as error:
            Logger.error( error, 3 )
            return class_identifier  # Returns a str containing the plugins identifier
            # with the PLUGIN_ERROR label, in order to make it easy the workflow
            # of send to stdout the INFO about a wrong or corrupt plugin.

    # <<<<<<<<<<<<<< -------------- Validators of plugin's skill class members ---------------- >>>>>>>>>>>>>>>
    @staticmethod
    def _validate_name_attr(line: str) -> bool:
        try:
            if line.__contains__('name'):
                try:
                    name_validator = line.split(" [")[1].strip(']').replace("'", '').split(',')
                    if len(name_validator) == 2:  # TODO Match it against the len of the availiable langs
                        Logger.success('Validated name', 4)
                        return True
                    else:
                        raise SkillNamesListWrongLength(len(name_validator))
                except SkillNamesListWrongLength as error:
                    Logger.error(error, 4)
            else:
                raise SkillNotContainsNameParameter
        except SkillNotContainsNameParameter as error:
            Logger.error(error, 4)

    # <<<<<<<<<<<<<< -------------- Retrieve data from attrs zone ---------------- >>>>>>>>>>>>>>>
    @staticmethod
    def _retrieve_skill_tags_from_plugin(line: str) -> str:
        line = line.split('[')[1] \
            .strip('\n')
        if line.endswith(','):
            line = line.strip()[0: len(line) - 2]
        return line.replace(']', '') \
            .replace("'", '') \
            .strip() \
            .split(', ')
