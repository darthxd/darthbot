import discord
from NewFunctionsPYC import Slash_Command, slashContext
from discord.ext import commands

class botStart(commands.Cog):
    def __init__(self, client: discord.Client) -> None:
        self.client = client
        super().__init__()

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Bot on! Logged as {self.client.user}!')
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Bot On! Criado por darthxd!"))

def setup(bot: commands.Bot):
    bot.add_cog(botStart(bot))