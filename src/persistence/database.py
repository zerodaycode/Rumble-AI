'''
    The persistence module of Rumble.
    
    Here is how we deal with the user's configuration and Rumble configuration
    storage.

    The actual implementation (with MongoDB) is completly deprecated, and we are waiting
    for a new review
'''

# from pymongo import MongoClient


class RumblePersistence:
    '''The type that holds the persistence actions'''

    def __init__(self):
        """
            Rumble persistence desing model it's under revision
        """
        # pass
#         # Creating a pymongo client
#         self.mongo_client = MongoClient('localhost', 27017)
#         # Getting the database instance
#         self.database = self.mongo_client['RumblePersistence']
#         # The configuration collection
#         self.configuration = self.database['Configuration']
