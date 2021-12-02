import os
import discord
import discord.utils
from discord.ext import commands, tasks
from discord.ext.commands import Bot

#Establishes API key for discord
my_secret = os.environ['client_secret'] 
client =  discord.Client(intents=discord.Intents.all())

#Makes bot object for bot functionalities
bot = commands.Bot(command_prefix = "=", intents=discord.Intents.all())
client =  discord.Client(intents=discord.Intents.all())

#loads/unloads cogs for Discord Bot
@bot.command()
async def load(ctx, extension):
  client.load(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
  client.unload(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
     bot.load_extension(f'cogs.{filename[:-3]}')

#Prints log in to terminal, verify proper connection to server
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

bot.run(my_secret)
client.run(my_secret)