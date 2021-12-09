import os
import discord
import discord.utils
from discord.ext import commands, tasks
from discord.ext.commands import Bot
try:
  import mysql.connector
except:
  os.system('pip install mysql-connector-python')
  import mysql.connector
from mysql.connector.constants import ClientFlag


#Establishes API key for discord
my_secret = os.environ['client_secret'] 
client =  discord.Client(intents=discord.Intents.all())

#Establishes connection to mysql database
password = os.environ['db-password']
username = os.environ['db-username']
IP = os.environ['db-IP']

db =  mysql.connector.connect(
  host = IP,
  user = username,
  passwd = password,
  database = "preferences"
)

crsr = db.cursor()



# Function for getting server prefix from database
async def determine_prefix(bot, message):
  guild = message.guild
  crsr.execute("SELECT server_id FROM prefixes WHERE server_id= %s", (int(guild.id),))
  result = crsr.fetchone()
  if result != None:
       crsr.execute("SELECT prefix FROM prefixes WHERE server_id=%s", (int(guild.id),))
       return crsr.fetchone()
  else:
     crsr.execute("INSERT INTO prefixes (server_id, prefix) VALUES(%s,%s)", (guild.id, "!",))
     crsr.execute("SELECT prefix FROM prefixes WHERE server_id=%s", (int(guild.id),))
     return crsr.fetchone()

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

@bot.command()
async def setprefix(ctx, new_prefix):
  crsr.execute("UPDATE prefixes SET prefix=%s WHERE server_id=%s", (new_prefix, int(ctx.guild.id)))
    
  await ctx.send("The new prefix for the server is " + str(new_prefix))
bot.run(my_secret)
client.run(my_secret)


