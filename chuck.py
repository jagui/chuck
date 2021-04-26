import os
import random as rnd

import aiohttp
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")


chucknorris_api_url = "https://api.chucknorris.io/jokes/"
random_url = chucknorris_api_url + "random"
search_url = chucknorris_api_url + "search?query="


bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("!"), intents=discord.Intents.default()
)


@bot.command()
async def random(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get(random_url) as r:
            if r.status == 200:
                js = await r.json()
                await ctx.send(js["value"])


@bot.command()
async def search(ctx, query):
    async with aiohttp.ClientSession() as session:
        async with session.get(search_url + query) as r:
            if r.status == 200:
                js = await r.json()
                joke = rnd.choice(js["result"])
                await ctx.send(joke["value"])


bot.run(TOKEN)
