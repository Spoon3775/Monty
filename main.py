import discord.py
from discord.ext import commands
import logging 
import logging.handlers

from dotenv import load_dotenv
import asyncio
import os

class MyBot(commands.bot):
    def __init__(self):
        super().__init__(command_prefix = '$', intents = discord.intents.all())
        self.help_command = HelpCmd()
    
    async def setup_hook(self):
        print("Loading Bot")

    async def on_ready(self):
        print(f"Logged in as {self.user.name}")

async def main():
    bot = MyBot()
    await bot.start(os.getenv("TOKEN"))

asyncio.run(main())