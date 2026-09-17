import discord
from discord.ext import commands
import logging 
import logging.handlers

from dotenv import load_dotenv
import asyncio
import os

load_dotenv()

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix = '$', intents = discord.Intents.all())
        # self.help_command = HelpCmd()  # HelpCmd not defined yet
    
    async def setup_hook(self):
        print("Loading Bot")

        # Explicitly load each cog extension
        extensions = (
            "ext.general",
        )
        for ext in extensions:
            await self.load_extension(ext)

        await self.tree.sync()
        print("Synced Slash Commands Globally")

    async def on_ready(self):
        print(f"Logged in as {self.user.name}")

async def main():
    bot = MyBot()
    await bot.start(os.getenv("TOKEN"))

asyncio.run(main())