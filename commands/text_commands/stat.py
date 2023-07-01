import discord
from discord.ext import commands

class statCheck(commands.Cog):
    def __init__(self, client: discord.Client) -> None:
        self.client = client
        super().__init__()

    @discord.slash_command(name="stat", description="Check if bot is working well.")
    async def stat(self, Interaction: discord.Interaction):
        author = str(Interaction.author)
        await Interaction.response.send_message(f"Hello {author[:-2]}! Bot is actually on!")
        

def setup(bot: commands.Bot):
    bot.add_cog(statCheck(bot))