# 🛠️ Discord Bot to Manage Exaroton Servers

KikoMine is a Discord bot developed in Python that allows you to manage Minecraft servers hosted on the [Exaroton](https://exaroton.com/) platform directly from Discord.

> 💡 Unlike the official Exaroton bot, this bot gives you control over who can access which commands using roles or user ID. By default, all users in your Discord server can use all the commands, but this behavior is easily configurable in [permissions.py](permissions.py)

## 🚀 Features

- 👁‍🗨 | View server info
- 🔍 | Check server status
- 🚀 | Start server
- ⏹️ | Stop server
- 🔁 | Restart server
- 📦 | View and change allocated RAM

and more..

Commands organized with `discord.app_commands` (slash commands)

## 📦 Requirements

- Python 3.10+
- An account on [Exaroton](https://exaroton.com/)
- A configured Minecraft server on Exaroton
- A registered Discord bot with a token

## 🧪 Installation

1. Clone the repository:
``` git
    git clone https://github.com/beckerfelipee/KikoMine.git
    cd KikoMine
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

## 🧾 Default Commands

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

---
> You can easily create more commands by following the existing code structure.

## 📄 License

This project is open-source and licensed under the [MIT License](LICENSE).
