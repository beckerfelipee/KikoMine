import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()

# Import exaroton and set our token
from exaroton import Exaroton

api_token = os.getenv("EXAROTON_API_TOKEN")
exa = Exaroton(api_token)

server_id = "EXAMPLEID2O13O214J"

server_info = exa.get_server(server_id)
print(server_info)
"""
{
    "_": "Server",
    "id": "EXAMPLEID2O13O214J",
    "name": "EXAMPLE_NAME",
    "address": "EXAMPLE_NAME.exaroton.me",
    "motd": "\u00a7f\u00a7lExample motd!",
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
        "id": "Example_Software_ID12314",
        "name": "Forge",
        "version": "1.20.1 (47.4.0)"
    },
    "shared": false
}
"""
