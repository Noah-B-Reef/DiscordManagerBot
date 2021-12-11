import discord
import asyncio
from discord.ext import commands
from replit import db

# Discord Bot Cog responsible for RoleReact embed setup
class Mute(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.server_id = None
    self.user = None
  
  # Displays when cog has been loaded in
  @commands.Cog.listener()
  async def on_ready(self):
    print(f"{self.__class__.__name__} Cog has been loaded\n-----")
  
  # Creates the 'muted' role when joining the server
  @commands.Cog.listener()
  async def on_guild_join(self, guild):
    await guild.create_role(name="muted", colour=discord.Colour(0x808080), permissions=discord.Permissions(permissions=1024))

  # 'mute' command
  @commands.command(name='mute',description="mutes server member for specified time frame.")
  @commands.has_permissions(administrator=True)
  async def mute(self, ctx, user: discord.Member , mute_time: int):

    guild = await(self.bot.fetch_guild(ctx.message.guild.id))

    # gets the ID of the user to be muted
    member = await (guild.fetch_member(user.id))

    # Establishes and assigns 'muted' role to user
    muterole = discord.utils.get(ctx.guild.roles, name="muted")
    await member.add_roles(muterole)

    # Informs user of being muted
    embed=discord.Embed(title= "Muted", description="You muted " + user.mention + "for " + str(mute_time) + " seconds!", color=0xFF5733)
    await ctx.send(embed=embed)

    # Holds and un-mutes user after specified time
    await asyncio.sleep(mute_time)
    await member.remove_roles(muterole)


def setup(bot):
  bot.add_cog(Mute(bot))