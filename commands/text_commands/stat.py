import discord
from discord.ext import commands

class statCheck(commands.Cog):
    def __init__(self, client: discord.Client) -> None:
        self.client = client
        super().__init__()

    @commands.command(name="stat", description="Check if bot is working well.")
    async def stat(self, ctx):
        author = str(ctx.author)
        await ctx.reply(f"Olá {author[:-2]}! O Bot está on!")
        

def setup(bot: commands.Bot):
    bot.add_cog(statCheck(bot))