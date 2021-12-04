import discord
import asyncio
from discord.ext import commands
from replit import db

# Discord Bot Cog responsible for RoleReact embed setup
class RoleReact(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.server_id = None
    self.msg_id = None
  
  # Displays when cog has been loaded in
  @commands.Cog.listener()
  async def on_ready(self):
    print(f"{self.__class__.__name__} Cog has been loaded\n-----")
  
  
def setup(bot):
  bot.add_cog(RoleReact(bot))