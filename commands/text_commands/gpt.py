import discord
from NewFunctionsPYC import CommandPrefix, prefixContext
from discord.ext import commands
import openai
from decouple import config

class gptMsg(commands.Cog):
    def __init__(self, client: discord.Client) -> None:
        self.client = client
        super().__init__()

    @CommandPrefix(name="gpt")
    async def random(self, ctx: prefixContext, *, msg: str):
        openai.api_key = config('API_KEY')
        messages = [ {"role": "system", "content": "Você é um assistente pessoal."} ]
        message = msg
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        await ctx.reply(reply)

def setup(bot: commands.Bot):
    bot.add_cog(gptMsg(bot))