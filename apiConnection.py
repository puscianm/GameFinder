import sys
import requests
import json
sys.path.append("../")

from secure import passwords

url = "https://api.igdb.com/v4/games"
headers = {
    "Client-ID": passwords.CLIENTID,
    "Authorization": f"Bearer {passwords.ACCESTOKEN}",
    "Content-Type": "application/json"  # Dodaj ten nagłówek, aby wskazać, że dane są przesyłane w formacie JSON
}
data = "fields name, rating_count; sort rating_count desc;"

response = requests.post(url, headers=headers, data=data)

if response.status_code == 200:
    print("Success!")

    json_formatted_str = json.dumps(response.json(), indent=3)
    print(json_formatted_str)
else:
    print(f"Failed with status code: {response.status_code}")
    print(response.text)  # Wyświetla tekst odpowiedzi, aby zobaczyć, co poszło nie tak