import discord
from discord.ext import commands
import random

class randomResp(commands.Cog):
    def __init__(self, client: discord.Client) -> None:
        self.client = client
        super().__init__()

    @commands.command(name="random")
    async def random(self, ctx, *, msg):
        chance = random.randint(0, 1)
        if(chance == 0):
            await ctx.reply('Não!')
        else:
            await ctx.reply('Sim!')
        

def setup(bot: commands.Bot):
    bot.add_cog(randomResp(bot))