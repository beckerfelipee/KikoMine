import os
import discord
import asyncio
from dotenv import load_dotenv
from exaroton import Exaroton
from discord import app_commands

# Carrega variáveis de ambiente
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
EXAROTON_TOKEN = os.getenv("EXAROTON_API_TOKEN")
SERVER_ID = os.getenv("SERVER_ID")

# Inicializa cliente Exaroton
exa = Exaroton(EXAROTON_TOKEN)

# Cria cliente Discord com intents e árvore de comandos
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# Espera por status desejado
async def wait_for_status(desired_status, check_interval=3):
    while True:
        status = exa.get_server(SERVER_ID).status
        if status.lower() == desired_status.lower():
            break
        await asyncio.sleep(check_interval)

class RamGroup(app_commands.Group):
    def __init__(self):
        super().__init__(name="ram", description="Gerencia a RAM do servidor")

    # /ram get
    @app_commands.command(name="get", description="Mostra a RAM atual do servidor")
    async def get(self, interaction: discord.Interaction):
        ram = exa.get_server_ram(SERVER_ID)
        await interaction.response.send_message(f"📦 RAM atual do servidor: `{ram} GB`")

    # /ram help
    @app_commands.command(name="help", description="Exibe ajuda sobre o comando de RAM")
    async def help(self, interaction: discord.Interaction):
        help_msg = (
            "`/ram get` → Mostra a RAM atual\n"
            "`/ram help` → Exibe esta ajuda\n"
            "`/ram set <valor>` → Define nova RAM\n"
            "`/ram set <valor> <restart>` → Altera RAM e reinicia o servidor\n\n"
            "**Recomendações:**\n"
            "🛋️ AFK/ocioso → `2 GB`\n"
            "🎮 Jogando normalmente → `5 GB`\n"
            "🚨 Lag ou travamentos → `6-10 GB`\n"
        )
        await interaction.response.send_message(help_msg)

    # /ram set <valor> [restart]
    @app_commands.command(name="set", description="Define nova RAM (entre 2 e 10 GB)")
    @app_commands.describe(
        valor="Nova quantidade de RAM (2 a 10 GB)",
        restart="Reiniciar automaticamente após aplicar a mudança"
    )
    async def set(
        self,
        interaction: discord.Interaction,
        valor: int,
        restart: bool = False
    ):
        ram = exa.get_server_ram(SERVER_ID)

        if valor < 2 or valor > 10:
            await interaction.response.send_message("❌ Valor inválido. A RAM deve estar entre `2` e `10` GB.")
            return

        if valor == ram:
            await interaction.response.send_message(f"👌 A RAM já está definida para `{ram} GB`. Nenhuma alteração necessária.")
            return

        if not restart:
            try:
                exa.set_server_ram(SERVER_ID, valor)
                await interaction.response.send_message(f"✅ RAM alterada para `{valor} GB`. Inicie o servidor para aplicar.")
            except Exception:
                await interaction.response.send_message("⚠️ Não foi possível aplicar a RAM agora. Tente novamente com `restart: true` ou desligue o servidor.")
            return

        server = exa.get_server(SERVER_ID)

        if server.status != "Offline":
            await interaction.response.send_message("🛑 Parando o servidor para alterar a RAM...")
            exa.stop(SERVER_ID)
            await wait_for_status("Offline")

        # Após garantir que está offline, aplicar a RAM
        try:
            await interaction.response.send_message(f"⚙️ Alterando RAM para `{valor} GB`...")
            exa.set_server_ram(SERVER_ID, valor)

            # Verifica se o servidor estava online antes
            if server.status != "Offline":
                await interaction.response.send_message("🚀 Iniciando o servidor novamente... \nIsso pode levar alguns minutos.")
                exa.start(SERVER_ID)
                await wait_for_status("Online")
                await interaction.followup.send("✅ Servidor iniciado com nova configuração de RAM.")
            else:
                await interaction.response.send_message("✅ RAM alterada com sucesso")
                await interaction.response.send_message("⚠️ O servidor está Offline. Use `/start` para iniciá-lo.")
        except Exception as e:
            await interaction.followup.send(f"❌ Erro ao configurar a RAM: `{e}`")


# Adiciona o grupo de comandos RAM à árvore
tree.add_command(RamGroup())
# Evento de pronto
@client.event
async def on_ready():

    await tree.sync()  # sincroniza os comandos com o Discord
    await tree.sync(guild=None) # limpa comandos antigos da aplicação globalmente
    print(f"✅ Bot {client.user.name} está online e comandos sincronizados!")


# /server
@tree.command(name="server", description="Exibe o status atual do servidor")
async def server(interaction: discord.Interaction):
    server = exa.get_server(SERVER_ID)
    status_emoji = {
        "Online": "🟢",
        "Offline": "🔴"
    }.get(server.status, "⚙️")
    await interaction.response.send_message(
        f"🖥️ **Servidor:** {server.name}\n"
        f"📡 **Status:** {status_emoji} {server.status}\n\n"
        f"🌐 **Endereço:** `{server.address}:{server.port}`"
    )


# /start
@tree.command(name="start", description="Inicia o servidor")
async def start(interaction: discord.Interaction):
    server = exa.get_server(SERVER_ID)
    if server.status == "Offline":
        await interaction.response.send_message("🔄 Iniciando o servidor... \nIsso pode levar alguns minutos.")
        exa.start(SERVER_ID)
        await wait_for_status("Online")
        await interaction.followup.send("✅ Servidor iniciado com sucesso!")
    elif server.status == "Online":
        await interaction.response.send_message("🟢 O servidor já está online.")
    else:
        await interaction.response.send_message(f"⏳ O servidor está no seguinte estado: {server.status}")


# /stop
@tree.command(name="stop", description="Desliga o servidor")
async def stop(interaction: discord.Interaction):
    server = exa.get_server(SERVER_ID)
    if server.status != "Offline":
        await interaction.response.send_message("🛑 Encerrando o servidor...")
        exa.stop(SERVER_ID)
        await wait_for_status("Offline")
        await interaction.followup.send("👍 Servidor encerrado com sucesso.")
    else:
        await interaction.response.send_message("⚠️ O servidor já está desligado.")


# /restart
@tree.command(name="restart", description="Reinicia o servidor")
async def restart(interaction: discord.Interaction):
    server = exa.get_server(SERVER_ID)
    if server.status != "Offline":
        await interaction.response.send_message("🔁 Reiniciando o servidor... \nIsso pode levar alguns minutos.")
        exa.restart(SERVER_ID)
        await wait_for_status("Online")
        await interaction.followup.send("✅ Servidor reiniciado.")
    else:
        await interaction.response.send_message("⚠️ O servidor está Offline. Use `/start` para iniciá-lo.")

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

# Inicia o bot
client.run(DISCORD_TOKEN)

