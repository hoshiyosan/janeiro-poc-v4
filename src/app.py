from janeiro_log import setup_logging

setup_logging()

from janeiro_api import RestAPI

api = RestAPI()

api.setup()
