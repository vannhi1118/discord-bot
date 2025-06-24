import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

async def main():
    # Load cogs
    await bot.load_extension("cogs.word_train")
    await bot.start(TOKEN)

@bot.event
async def on_ready():
    print(f"✅ Bot is online as {bot.user}")

import asyncio
asyncio.run(main())