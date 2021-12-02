import discord
import asyncio
import requests, json, random
from discord.ext import commands
import os, praw

my_client = os.environ['client_id']
my_secret = os.environ['secret']
my_username= os.environ['username']
my_password = os.environ['password']


class Memes(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.Cog.listener()
  async def on_ready(self):
    print(f"{self.__class__.__name__} Cog has been loaded\n-----")

  @commands.command(name='meme',description="sends a meme in chat")
  async def Meme(self, ctx):
    reddit = praw.Reddit(client_id = my_client, client_secret = my_secret, username = my_username, password = my_password, user_agent = "prawpython",check_for_async=False)
    subreddit = reddit.subreddit("memes")
    all_subs = []

    top = subreddit.top(limit = 50)

    for submission in top:
      all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    url = random_sub.url

    em = discord.Embed(title = name)

    em.set_image(url = url)

    await ctx.channel.send(embed = em)


def setup(bot):
  bot.add_cog(Memes(bot))