import os
import discord
import asyncio
from dotenv import load_dotenv
from exaroton import Exaroton
from discord import app_commands

# Load environment variables
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
EXAROTON_TOKEN = os.getenv("EXAROTON_API_TOKEN")
SERVER_ID = os.getenv("SERVER_ID")

# Initialize Exaroton client
exa = Exaroton(EXAROTON_TOKEN)

# Create Discord client with intents and command tree
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


# Wait for desired status
async def wait_for_status(desired_status, check_interval=3):
    while True:
        status = exa.get_server(SERVER_ID).status
        if status.lower() == desired_status.lower():
            break
        await asyncio.sleep(check_interval)


class RamGroup(app_commands.Group):

    def __init__(self):
        super().__init__(name="ram", description="Manages the server's RAM")

    # /ram get
    @app_commands.command(name="get",
                          description="Displays the server's current RAM")
    async def get(self, interaction: discord.Interaction):
        ram = exa.get_server_ram(SERVER_ID)
        await interaction.response.send_message(
            f"📦 Current server RAM: `{ram} GB`")

    # /ram help
    @app_commands.command(name="help",
                          description="Displays help for the RAM command")
    async def help(self, interaction: discord.Interaction):
        help_msg = (
            "`/ram get` → Shows current RAM\n"
            "`/ram help` → Displays this help\n"
            "`/ram set <value>` → Sets new RAM\n"
            "`/ram set <value> <restart>` → Changes RAM and restarts the server\n\n"
            "**Recommendations:**\n"
            "🛋️ AFK/idle → `2 GB`\n"
            "🎮 Normal gameplay → `5 GB`\n"
            "🚨 Lag or stuttering → `6-10 GB`\n")
        await interaction.response.send_message(help_msg)

    # /ram set <value> [restart]
    @app_commands.command(name="set",
                          description="Sets new RAM (between 2 and 10 GB)")
    @app_commands.describe(
        valor="New RAM amount (2 to 10 GB)",
        restart="Automatically restart after applying the change")
    async def set(self,
                  interaction: discord.Interaction,
                  valor: int,
                  restart: bool = False):
        ram = exa.get_server_ram(SERVER_ID)

        if valor < 2 or valor > 10:
            await interaction.response.send_message(
                "❌ Invalid value. RAM must be between `2` and `10` GB.")
            return

        if valor == ram:
            await interaction.response.send_message(
                f"👌 RAM is already set to `{ram} GB`. No changes needed.")
            return

        if not restart:
            try:
                exa.set_server_ram(SERVER_ID, valor)
                await interaction.response.send_message(
                    f"✅ RAM changed to `{valor} GB`. Start the server to apply."
                )
            except Exception:
                await interaction.response.send_message(
                    "⚠️ Could not apply RAM now. Try again with `restart: true` or stop the server."
                )
            return

        server = exa.get_server(SERVER_ID)
        await interaction.response.send_message(
            f"🔄 Changing RAM to `{valor} GB` and restarting the server...")

        if server.status != "Offline":
            await interaction.followup.send(
                "🛑 Stopping the server to change RAM...")
            exa.stop(SERVER_ID)
            await wait_for_status("Offline")

        # After ensuring it's offline, apply RAM
        try:
            await interaction.followup.send(
                f"⚙️ Changing RAM to `{valor} GB`...")
            exa.set_server_ram(SERVER_ID, valor)

            # Check if the server was online before
            if server.status != "Offline":
                await interaction.followup.send(
                    "🚀 Restarting the server... \nThis may take a few minutes."
                )
                exa.start(SERVER_ID)
                await wait_for_status("Online")
                await interaction.followup.send(
                    "✅ Server started with new RAM configuration.")
            else:
                await interaction.followup.send(
                    "✅ RAM successfully changed \n⚠️ The server is Offline. Use `/start` to start it."
                )
        except Exception as e:
            await interaction.followup.send(
                f"❌ Error setting RAM: `{e}`")


# Add RAM command group to the tree
tree.add_command(RamGroup())


# Ready event
@client.event
async def on_ready():

    await tree.sync()  # sync commands with Discord
    await tree.sync(guild=None)  # clear old global application commands
    print(f"✅ Bot {client.user.name} is online and commands are synced!")


# /server
@tree.command(name="server", description="Displays the current server status")
async def server(interaction: discord.Interaction):
    server = exa.get_server(SERVER_ID)
    status_emoji = {"Online": "🟢", "Offline": "🔴"}.get(server.status, "⚙️")
    await interaction.response.send_message(
        f"━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"   🖥️ **Minecraft ATM 9 Server**\n"
        f"━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"🌍 **Name:** `{server.name}`\n"
        f"📡 **Status:** {status_emoji} `{server.status}`\n"
        f"📌 **Address:**\n```{server.address}:{server.port}```")


# /start
@tree.command(name="start", description="Starts the server")
async def start(interaction: discord.Interaction):
    server = exa.get_server(SERVER_ID)
    if server.status == "Offline":
        await interaction.response.send_message(
            "🔄 Starting the server... \nThis may take a few minutes.")
        exa.start(SERVER_ID)
        await wait_for_status("Online")
        await interaction.followup.send("✅ Server started successfully!")
    elif server.status == "Online":
        await interaction.response.send_message("🟢 The server is already online.")
    else:
        await interaction.response.send_message(
            f"⏳ The server is currently in the following state: {server.status}")


# /stop
@tree.command(name="stop", description="Stops the server")
async def stop(interaction: discord.Interaction):
    server = exa.get_server(SERVER_ID)
    if server.status != "Offline":
        await interaction.response.send_message("🛑 Shutting down the server...")
        exa.stop(SERVER_ID)
        await wait_for_status("Offline")
        await interaction.followup.send("👍 Server shut down successfully.")
    else:
        await interaction.response.send_message(
            "⚠️ The server is already offline.")


# /restart
@tree.command(name="restart", description="Restarts the server")
async def restart(interaction: discord.Interaction):
    server = exa.get_server(SERVER_ID)
    if server.status != "Offline":
        await interaction.response.send_message(
            "🔁 Restarting the server... \nThis may take a few minutes.")
        exa.restart(SERVER_ID)
        await wait_for_status("Online")
        await interaction.followup.send("✅ Server restarted.")
    else:
        await interaction.response.send_message(
            "⚠️ The server is Offline. Use `/start` to start it.")


"""
keep_alive = True

if keep_alive:
    from flask import Flask
    from threading import Thread

    app = Flask('')

    @app.route('/')
    def home():
        return "✅ KikoMine está online!"

    def run_web():
        app.run(host='0.0.0.0', port=8080)

    def keep_alive():
        thread = Thread(target=run_web)
        thread.start()

    keep_alive()
"""

# Inicia o bot
client.run(DISCORD_TOKEN)
