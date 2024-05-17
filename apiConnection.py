import sys
import requests
sys.path.append("../")

from secure import passwords

myHeader={
    "client_id":passwords.CLIENTID,
    "client_secret" : passwords.APIKEY,
    "grant_type":"client_credentials"
}

response = requests.post("https://id.twitch.tv/oauth2/", headers= myHeader)
print(response.text)