from dotenv import load_dotenv
import os
import discord
from discord.ext import commands
from commands.random_image_command import randomImage

# Load token from .env file
load_dotenv()
token = os.getenv("TOKEN")

# Set intents
intents = discord.Intents.all()
intents.message_content = True

# Bot instance
bot = commands.Bot(command_prefix='$', intents=intents)

# Commands
randomImage(bot)

bot.run(token)
