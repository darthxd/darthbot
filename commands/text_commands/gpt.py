import discord
from discord.ext import commands
import openai
from decouple import config

class gptMsg(commands.Cog):
    def __init__(self, client: discord.Client) -> None:
        self.client = client
        super().__init__()

    @commands.command(name="gpt")
    async def random(self, ctx: discord.Interaction, *, msg: str):
        openai.api_key = config('API_KEY')
        messages = [ {"role": "system", "content": "Você é um assistente pessoal de um servidor do discord."} ]
        author = str(ctx.author)
        message = (f"Olá chatgpt. Eu sou o {author[:-2]}. {msg}")
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