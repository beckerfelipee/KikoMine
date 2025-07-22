# 🛠️ KikoMine — Bot de Discord para Gerenciar Servidores Exaroton

KikoMine é um bot de Discord desenvolvido em Python que permite gerenciar servidores de Minecraft hospedados na plataforma [Exaroton](https://exaroton.com/), diretamente do Discord. Ele oferece comandos para iniciar, parar, reiniciar o servidor e ajustar a quantidade de RAM alocada.

## 🚀 Funcionalidades

- 🔍 Verificar status do servidor
- ▶️ Iniciar servidor
- ⏹️ Parar servidor
- 🔁 Reiniciar servidor
- 📦 Ver e alterar a quantidade de RAM alocada
- 🧠 Comandos organizados com `discord.app_commands` (slash commands)

## 📦 Requisitos

- Python 3.8+
- Conta na [Exaroton](https://exaroton.com/)
- Um servidor de Minecraft configurado na Exaroton
- Um bot de Discord registrado com token

## 🧪 Instalação

1. Clone o repositório:
``` git
    git clone https://github.com/seu-usuario/kikomine-bot.git
    cd kikomine-bot
```
2. Instale as dependências:
``` bash
    pip install -r requirements.txt
```
3. Crie um arquivo `.env` com as seguintes variáveis:
``` bash
    DISCORD_BOT_TOKEN=seu_token_do_discord
    EXAROTON_API_TOKEN=seu_token_da_exaroton
    SERVER_ID=id_do_seu_servidor
```
4. Execute o bot:
``` python
    python bot.py
```
## 🧾 Comandos Disponíveis

### `/server`
Exibe o status atual do servidor Minecraft.

### `/start`
Inicia o servidor.

### `/stop`
Desliga o servidor.

### `/restart`
Reinicia o servidor.

### `/ram get`
Mostra a quantidade atual de RAM alocada.

### `/ram set <valor> [restart]`
Define uma nova quantidade de RAM (entre 2 e 10 GB). Pode reiniciar automaticamente, se necessário.

### `/ram help`
Exibe ajuda sobre os comandos de RAM.

## 📄 Licença

Este projeto é open-source e está licenciado sob a [MIT License](LICENSE).
