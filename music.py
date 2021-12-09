import discord
import asyncio
from discord.ext import commands
from replit import db
import youtube_dl

# Discord Bot Cog responsible for RoleReact embed setup
class Music(commands.Cog):
  def __init__(self, client):
    self.client = client
    self.msg_id = None
  
  # Displays when cog has been loaded in
  @commands.Cog.listener()
  async def on_ready(self):
    print(f"{self.__class__.__name__} Cog has been loaded\n-----")
  
  @commands.command()
  async def join(self, ctx):
    if ctx.author.voice is None:
      await ctx.send("You are currently not in a voice channel!")
    
    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
      await voice_channel.connect()
    
    else:
      await ctx.voice_client.move_to(voice_channel)

  
  @commands.command()
  async def disconnect(self, ctx):
    await ctx.voice_client.disconnect()
  
  @commands.command()
  async def play(self, ctx, url):
    ctx.voice_client.stop()
    FFMPEG_OPTIONS = { 'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    YTDL_OPTIONS = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'restrictfilenames': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': True,
        'no_warnings': True,
        'default_search': 'auto',
        'source_address': '0.0.0.0',
    }

    vc = ctx.voice_client

    with youtube_dl.YoutubeDL(YTDL_OPTIONS) as ydl:
      info = ydl.extract_info(url, download=False)
      url2 = info[0][0]['url']
      source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
      vc.play(source)

  @commands.command()
  async def pause(self, ctx):
    await ctx.voice_client.pause()
    await ctx.send("Paused :pause_button:")

  @commands.command()
  async def resume(self, ctx):
    await ctx.voice_client.resume()
    await ctx.send("Paused :play_pause:")

def setup(bot): 
  bot.add_cog(Music(bot))