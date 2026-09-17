import discord
from discord.ext import commands
from ext.embed import EmbedHandler

class General(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.send(embed = EmbedHandler(description = f"Pong! {round(self.bot.latency * 1000)}ms"))

async def setup(bot: commands.Bot):
    await bot.add_cog(General(bot))
