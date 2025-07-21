import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

# Import exaroton and set our token
from exaroton import Exaroton

api_token = os.getenv("EXAROTON_API_TOKEN")
exa = Exaroton(api_token)

server_id = "GWQI2TAtLCpj7FhO"

exa.get_server_logs(server_id)

server_info = exa.get_server(server_id)
print(server_info)
"""
{
    "_": "Server",
    "id": "GWQI2TAtLCpj7FhO",
    "name": "GND_ATM9TTS",
    "address": "GND_ATM9TTS.exaroton.me",
    "motd": "\u00a7f\u00a7lAllTheMods9: To the Sky server",
    "status": "Offline",
    "port": 48245,
    "players": {
        "_": "Players",
        "max": 20,
        "count": 0,
        "list": []
    },
    "software": {
        "_": "Software",
        "id": "Flt6RsflglDPDJ0q",
        "name": "Forge",
        "version": "1.20.1 (47.4.0)"
    },
    "shared": false
}
"""

print()

server_ram = exa.get_server_ram(server_id)
print(server_ram)
"""
5
"""

#server_ram = exa.set_server_ram(server_id, 5)
#print(server_ram)

"""
status = exa.start(server_id)
print(status)

status = exa.restart(server_id)
print(status)

status = exa.stop(server_id)
print(status)
"""