import discord
import asyncio
from discord.ext import commands
from replit import db
import pandas as pd
from time import sleep

# Discord Bot Cog responsible for Profanity Filter setup
class Filter(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.server_id = None
    self.msg_id = None
  
  # Displays when cog has been loaded in
  @commands.Cog.listener()
  async def on_ready(self):
    print(f"{self.__class__.__name__} Cog has been loaded\n-----")
  
  # Listens for a message and checks/handles messages with profanity
  @commands.Cog.listener()
  async def on_message(self, message):

    # Reads in user message and loads in profanity csv
    msg = message.content
    df = pd.read_csv('https://query.data.world/s/o5363h3dmwli3yuolcxwg52llwxpmh')

    # Checks to see if message sender was the bot itself
    if message.author == self.bot.user:
      return

    # Deletes and responds to profanity by the offender
    msg = msg.split()

    if msg in df.values:
      await message.delete()
      embed = discord.Embed(title="Curse Filter", description="Your messsage contained profanity and was deleted. Please review the rules of the server before messaging!", color=0xFF5733)

      msg = await message.channel.send(embed=embed)

      # Deletes message after 3 seconds
      sleep(3)
      await msg.delete()

    
def setup(bot):
  bot.add_cog(Filter(bot))