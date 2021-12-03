import discord
import asyncio
from discord.ext import commands
from replit import db

# Discord Bot Cog responsible for Rules embed setup
class Rules(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.server_id = None
    self.msg_id = None
  
  # Displays when cog has been loaded in
  @commands.Cog.listener()
  async def on_ready(self):
    print(f"{self.__class__.__name__} Cog has been loaded\n-----")
  
  @commands.command(name="ruleSetup", description="Sets the rules for the server!")
  @commands.has_permissions(administrator=True)
  async def rulesetup(self,ctx):

    # Gets Server ID
    self.server_id = ctx.guild.id

    # Starts rulesetup dialogue

    # Retrives title for server rules
    await ctx.send(f"Enter the title for the server rules: ")
    response = await self.bot.wait_for("message")
    title = response.content

    # Retrives the rules for the server
    await ctx.send(f"Enter the rules for the server: ")
    response = await self.bot.wait_for("message")
    rules = response.content

    # Retrives channel ID to send server rules
    await ctx.send("Please enter the channel id that you'd like the rules to be sent to: ")
    response = await self.bot.wait_for("message")
    channel = self.bot.get_channel(int(response.content))

    # Sends Rules as an embed
    embed=discord.Embed(title= title, description=rules, color=0xFF5733)
    msg = await channel.send(embed=embed)
    self.msg_id = msg.id

    # Adds msg_id for the rules embed to database
    db[str(self.server_id)] = [self.msg_id]

    
    
    
def setup(bot):
  bot.add_cog(Rules(bot))