import discord
import asyncio
import requests, json, random
from discord.ext import commands
from replit import db

# Discord Bot Cog responsible for RoleReact embed setup
class Quiz(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.server_id = None
    self.msg_id = None
  
  # Displays when cog has been loaded in
  @commands.Cog.listener()
  async def on_ready(self):
    print(f"{self.__class__.__name__} Cog has been loaded\n-----")
  
  @commands.command(name='quiz', description="plays a quiz game")
  async def Quiz(self, ctx):

    # Sets player's score to 0 to start
    score = 0

    # Gets question for quiz
    def get_question():
      question_num = random.randint(0, 29)
      response = requests.get("https://opentdb.com/api.php?amount=30&type=boolean")
      json_data = json.loads(response.text)
      question = json_data["results"][question_num]["question"]
      answer = json_data["results"][question_num]["correct_answer"]
      question = question.replace('&quot;', "'")
      question = question.replace('&#039;', "'")
      return [question, answer]

    # Starts quiz dialogue
    await ctx.send(f"I will ask 10 true/false questions and you'll try to answer them correctly.")

    # Asks 10 Questions
    for i in range(10):

      # gets question and its respective answer
      question = get_question()
      question_prompt = question[0]
      await ctx.send(question_prompt)

      answer = question[1]
      valid_response = ['True', 'False', 'true', 'false']
      response = 'flag'

      # Performs player I/O and input validation
      while response not in valid_response:
        response = await self.bot.wait_for("message")
        response = response.content
        if response not in valid_response:
          await ctx.send(f"Please enter a valid response!")
      
      if response.lower() == answer.lower():
        await ctx.send(f"Correct!.")
        score += 1
      else:
        await ctx.send(f"Incorrect!.")

    # Prints out the final score of the plater
    await ctx.send("Congratulations you got " + str(score) + " out of 10 correct!")


def setup(bot):
  bot.add_cog(Quiz(bot))