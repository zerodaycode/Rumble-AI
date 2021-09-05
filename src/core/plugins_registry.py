import os

from src.utils.rumble_logger import Logger
from src.core.core_exceptions.plugin_exceptions import NoInheritsFromSkill


class PluginsRegistry:
    """
        Takes care about handle a way to store and retrieve all the Rumble's availiable plugins.
        Provides a way to get new plugins from outside (internet, ex: GitHub repo), to handle it's
        validation as a Rumble skill...
    """

    def __init__(self):
        self.root_plugins_dir = 'src/plugins/'
        self.plugin_instance_identifiers: list = []

    def scan_plugins_directory(self) -> None:
        """ Looks for plugins on the plugins folder """
        current_dir_level = ''

        Logger.info('Elements founded on plugins folder:')

        for plugin_dir_name in os.listdir( self.root_plugins_dir ):
            if os.path.isdir( current_dir_level := self.root_plugins_dir + plugin_dir_name ):
                if plugin_identifier := self._validate_plugin( plugin_dir_name, current_dir_level ):
                    if plugin_identifier not in self.plugin_instance_identifiers:
                        Logger.success( f'Valid plugin founded! -> { plugin_identifier }', 3 )
                    else:
                        Logger.warning(f'Plugin already tracked! -> {plugin_identifier}', 3)
                else:
                    Logger.error( f'NOT a valid plugin -> { plugin_identifier }', 3 )

    def _validate_plugin(self, plugin_dir_name: str, current_dir_level: str ) -> str:
        """ Founded a plugin candidate on plugins folder, validates if it's OK to be added as a Rumble skill """
        print( '\t' + f'Plugin candidate on directory: { plugin_dir_name }' )
        if PluginsRegistry._validate_plugin_folder_name( plugin_dir_name ):
            print( '\t\t' + f'{ plugin_dir_name } is a valid folder name' )
            for filename in os.listdir( current_dir_level ):
                print( '\t\t\t' + f'File { filename } ON { plugin_dir_name }' )
                if PluginsRegistry._validate_plugin_file_name( filename ):
                    file_path = current_dir_level + f'/{ filename }'
                    if identifier := PluginsRegistry._validate_file_and_get_instance_identifier( file_path ):
                        print( identifier )
                        self.plugin_instance_identifiers.append( identifier )
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
    def _validate_file_and_get_instance_identifier(filepath: str) -> str:
        """
            Verifies that the structure imposed on a plugin class is met.
            After this, if all imposed criteria are met, returns a dict with the plugin's class identifier,
            and parses the file looking for the necessary attrs of the inner dict (name, description and tags)
            in order to be added on the skills registry
        """
        with open( filepath, 'r') as plugin_file_class:
            for line in plugin_file_class.readlines():
                line = line.strip( '\n' )
                if line.__contains__( 'class' ):
                    class_signature_elements = line.split( ' ' )
                    print( f'Class signature: { class_signature_elements }' )
                    class_keyword = class_signature_elements[ 0 ]
                    class_identifier = class_signature_elements[ 1 ]
                    if class_identifier.__contains__( '(Skill)' ):  # Checks that the plugin inherits from the ABC Skill
                        return class_identifier.split( '(' )[ 0 ]
                    else:
                        raise NoInheritsFromSkill( class_identifier.split( '(' )[ 0 ] )


