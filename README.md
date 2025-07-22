# 🛠️ KikoMine — Discord Bot to Manage Exaroton Servers

KikoMine is a Discord bot developed in Python that allows you to manage Minecraft servers hosted on the [Exaroton](https://exaroton.com/) platform directly from Discord. It offers commands to start, stop, restart the server, and adjust the allocated RAM.

## 🚀 Features

- 👁‍🗨 | View server info
- 🔍 | Check server status
- 🚀 | Start server
- ⏹️ | Stop server
- 🔁 | Restart server
- 📦 | View and change allocated RAM
- 🧠 | Commands organized with `discord.app_commands` (slash commands)

## 📦 Requirements

- Python 3.8+
- An account on [Exaroton](https://exaroton.com/)
- A configured Minecraft server on Exaroton
- A registered Discord bot with a token

## 🧪 Installation

1. Clone the repository:
``` git
    git clone https://github.com/your-username/kikomine-bot.git
    cd kikomine-bot
```

2. Install the dependencies:
``` bash
    pip install -r requirements.txt
```

3. Create a `.env` file with the following variables:
``` bash
    DISCORD_BOT_TOKEN=your_discord_token
    EXAROTON_API_TOKEN=your_exaroton_token
    SERVER_ID=your_server_id
```

4. Run the bot:
``` python
    python bot.py
```

## 🧾 Available Commands

### `/server`
Displays the current status of the Minecraft server.

### `/start`
Starts the server.

### `/stop`
Stops the server.

### `/restart`
Restarts the server.

### `/ram get`
Shows the currently allocated RAM.

### `/ram set <value> [restart]`
Sets a new amount of RAM (between 2 and 10 GB). Can restart automatically if needed.

### `/ram help`
Displays help for RAM commands.

## 📄 License

This project is open-source and licensed under the [MIT License](LICENSE).
