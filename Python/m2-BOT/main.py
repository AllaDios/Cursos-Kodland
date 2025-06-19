import discord
from  discord.ext import commands
import secret
import random
import os
import requests
import json

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

url = "https://api.apileague.com/retrieve-random-meme?keywords=rocket"
api_key = "myapikey"

@bot.event
async def on_ready():
    print(f"Bot is ready as {bot.user}")

@bot.command()
async def mem(ctx):
    imagenes = os.listdir('images')
    imagen_aleatoria = random.choice(imagenes)
    with open(f'images/{imagen_aleatoria}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


@bot.command()
async def meme(ctx):
    meme_id = random.randint(1, 100)  # Cambia el rango si es necesario
    url = f"http://alpha-meme-maker.herokuapp.com/memes/{meme_id}"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "data" in data and "image" in data["data"]:
            await ctx.send(data["data"]["image"])  # Envía solo la imagen
        else:
            await ctx.send("No se encontró el meme.")
    else:
        await ctx.send("Error al obtener el meme.")

@bot.command()
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)

bot.run(secret.token)

