import os
import discord
import discord.utils
from discord.ext import commands, tasks
from discord.ext.commands import Bot
from replit import db


#Establishes API key for discord
my_secret = os.environ['client_secret'] 
client =  discord.Client(intents=discord.Intents.all())


# Function for getting server prefix from database
async def determine_prefix(bot, message):
  guild = message.guild.id
  try:
    prefix = db[str(guild)][0]["prefix"]
  except:
    prefix = "!"
  
  return prefix
  

#Makes bot object for bot functionalities
bot = commands.Bot(command_prefix = determine_prefix, intents=discord.Intents.all())
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

# Adds new server to database
@bot.event
async def on_guild_join(guild):
  server_id = guild.id
  if len(db.prefix(str(server_id))) == 0:
    print("server added")
    db[str(server_id)] = [{"prefix" : "!", "profanity toggle" : "ON"}]
  
  
bot.run(my_secret)
client.run(my_secret)


