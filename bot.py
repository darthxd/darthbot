import discord
import NewFunctionsPYC
from decouple import config
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = NewFunctionsPYC.Client(token=config('TOKEN'), poweredby=False, command_prefix=".")

client.load_cogs('./commands/events')
client.load_cogs('./commands/text_commands')

client.__run__()
