import discord
import os
from decouple import config
from discord.ext import commands

client = commands.Bot(intents=discord.Intents.all(), command_prefix=".", help_command=commands.MinimalHelpCommand())

for filename in os.listdir("./commands/events"):
    if filename.endswith(".py") and not filename.startswith("__"):
        client.load_extension(f"commands.events.{filename[:-3]}")

for filename in os.listdir("./commands/text_commands"):
    if filename.endswith(".py") and not filename.startswith("__"):
        client.load_extension(f"commands.text_commands.{filename[:-3]}")

token = config("TOKEN")
client.run(token)
