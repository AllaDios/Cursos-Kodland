import discord 
from discord.ext import commands
import secret

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos dentro {bot.user}')

bot.run(secret.token)