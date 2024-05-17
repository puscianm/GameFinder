import sys
sys.path.append("../")

from igdb.wrapper import IGDBWrapper
from secure import passwords
wrapper = IGDBWrapper("GameComparison", passwords.APIKEY)

'''With a wrapper instance already created'''
# JSON API request
byte_array = wrapper.api_request(
            'games',
            'fields id, name; offset 0; where platforms=48;'
          )
# parse into JSON however you like...

# Protobuf API request
from igdb.igdbapi_pb2 import GameResult
byte_array = wrapper.api_request(
            'games.pb', # Note the '.pb' suffix at the endpoint
            'fields id, name; offset 0; where platforms=48;'
          )
games_message = GameResult()
games_message.ParseFromString(byte_array) # Fills the protobuf message object with the response
games = games_message.games

print(games)


