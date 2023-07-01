import discord
from NewFunctionsPYC import Slash_Command, slashContext
from discord.ext import commands

class statCheck(commands.Cog):
    def __init__(self, client: discord.Client) -> None:
        self.client = client
        super().__init__()

    @Slash_Command(name="stat", description="Check if bot is working well.")
    async def stat(self, Interaction: slashContext):
        await Interaction.response.send_message(f"Hello {Interaction.author}! Bot is actually on!")

def setup(bot: commands.Bot):
    bot.add_cog(statCheck(bot))