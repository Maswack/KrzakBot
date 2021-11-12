import discord
from discord.ext import commands
import main as MP

def read_token():
    with open(".env", "r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='$', intents=intents)

@client.event
async def on_message(message):
    server_id = client.get_guild(906933692721659936)

    if str(message.content)[0] == "$":
        msg = message.content.replace("$", "")
        res = MP.discord_response(msg)
        await message.channel.send(res)

client.run(token)