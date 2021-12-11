import discord
import asyncio
from discord.ext import commands
from replit import db

# Discord Bot Cog responsible for RoleReact embed setup
class Prefix(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.server_id = None
  
  # Displays when cog has been loaded in
  @commands.Cog.listener()
  async def on_ready(self):
    print(f"{self.__class__.__name__} Cog has been loaded\n-----")
  
  # 'setprefix' Command
  @commands.command(name='setprefix',description="Allows for the prefix of the bot to be changed")
  @commands.has_permissions(administrator=True)
  async def setprefix(self, ctx, newprefix):
    # Gets Server ID
    self.server_id = ctx.guild.id

    # Sets server prefix to 'newprefix' which taken as an extra arguement to the command
    db[str(self.server_id)][0]["prefix"] = newprefix

    # confirmation message
    await ctx.send("The new prefix for the server is " + newprefix)

    
def setup(bot):
  bot.add_cog(Prefix(bot))
