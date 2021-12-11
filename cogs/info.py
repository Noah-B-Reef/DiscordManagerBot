import discord
import asyncio
from discord.ext import commands
from replit import db

# Discord Bot Cog responsible for sending Bot info to server owner
class Info(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.server_id = None
    self.msg_id = None
  
  # Displays when cog has been loaded in
  @commands.Cog.listener()
  async def on_ready(self):
    print(f"{self.__class__.__name__} Cog has been loaded\n-----")
  

  # Sends message to owner when joining server
  @commands.Cog.listener()
  async def on_guild_join(self, guild):
    owner = guild.owner
    embed=discord.Embed(title= "Thanks for Inviting Manager 1.0", description="Thank you for checking out Manager 1.0, a Discord Manager Bot! To get started check out: https://github.com/Noah-B-Reef/DiscordManagerBot/blob/main/README.md for more information related to commands for the bot. Have fun!", color=0xFF5733)
    await owner.send(embed=embed)
  
def setup(bot):
  bot.add_cog(Info(bot))