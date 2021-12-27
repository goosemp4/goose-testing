import discord, json, random
from discord.ext import commands
from random import randint

randomColour= [0xFF0000,0x0000FF,0x008000,0xFFFF00,0xFFA500,0x800080,0xFFC0CB,0x000000,0x964B00,0xFFFFFF, 0xFF00FF, 0x00FFFF, 0x32CD32, 0x808080, 0x89CFF0, 0x800000, 0xFDFD96, 0x77dd77, 0xff6961, 0xC3B1E1]

client = discord.Client()

class Games(commands.Cog):
	
	def __init__(self, client):
		self.client = client

  # ---
  # this command flips a coin, heads or tails
	@commands.cooldown(3, 5, commands.BucketType.user)
	@commands.command(aliases = ['flip', 'coinflip', 'flipcoin'])
	async def coin(self, ctx):
		"""Flips a 'coin' and sends it back"""
		result = randint(1,2)
		if result == 1:
			coinEmbed = discord.Embed(
				title=":coin: Heads",
				color=0xFFFF00
			)
		else:
			coinEmbed = discord.Embed(
				title=":coin: Tails",
				color=0xFFFF00
			)
		await ctx.reply(embed=coinEmbed)

  
 
	@commands.cooldown(4, 5, commands.BucketType.user)
	@commands.command(aliases=['dice','rolldice'])
	async def roll(self, ctx):
		"""Rolls a dice, 1-6 and sends the result back to the user"""
		roll = randint(1,6)
		diceEmbed = discord.Embed(
			title=f":game_die: You rolled a {str(roll)}",
			color=0xFF0000
		)
		await ctx.send(embed=diceEmbed)

	

	@commands.cooldown(2,3, commands.BucketType.user)
	@commands.command()
	async def rps(self, ctx, move=None):		
		if move.lower() == "rock" or move.lower() == "paper" or move.lower() == "scissors":
			moveList = ["ROCK","PAPER", "SCISSORS"]
			aiMove = random.choice(moveList)

			if aiMove == "ROCK" and move.upper() == "ROCK" or aiMove == "PAPER" and move.upper() == "PAPER" or aiMove == "SCISSORS" and move.upper() == "SCISSORS":
				tieEmbed = discord.Embed(
					title="Tie",
					description=f"You chose **{move.upper()}**\nI chose **{aiMove}**",
					color=0xFFFF00
				)
				await ctx.reply(embed=tieEmbed, mention_author=False)
			elif aiMove == "ROCK" and move.upper() == "SCISSORS" or aiMove == "PAPER" and move.upper() == "ROCK" or aiMove == "SCISSORS" and move.upper() == "PAPER":
				loseEmbed = discord.Embed(
					description=f"You chose **{move.upper()}**\nI chose **{aiMove}**\n\nL Bozo",
					color=0xFF0000
				)
				loseEmbed.set_author(
					name="Bag Head wins",
					icon_url=self.client.user.avatar_url
				)
				await ctx.reply(embed=loseEmbed, mention_author=False)
			else:
				winEmbed = discord.Embed(
					description=f"You chose **{move.upper()}**\nI chose **{aiMove}**",
					color=0x00FF00
				)
				winEmbed.set_author(
					name=f"{ctx.author.name} wins",
					icon_url=ctx.author.avatar_url
				)
				await ctx.reply(embed=winEmbed, mention_author=False)
		
		else:
			await ctx.reply("**:x: That's not a valid move you idiot\nValid moves are `rock`, `paper`, and `scissors`**")


	@commands.cooldown(2, 10, commands.BucketType.user)
	@commands.command()
	async def dare(self, ctx):
		"""Gives the user a dare to do"""
	
		with open("cogs/docs/json/responses.json") as f:
			data = json.load(f)
			dareList = dict
			for i in data:
				for x in i:
					if x == "dare":
						dareList = i['dare']
			selectedDare = random.choice(dareList)

		dareEmbed = discord.Embed(
			title="Dare",
			description=selectedDare,
			color=random.choice(randomColour)
		)
		dareEmbed.set_footer(
			text=f"Dare asked by {ctx.author.name}",
			icon_url=ctx.author.avatar_url
		)
		await ctx.reply(embed=dareEmbed, mention_author=False)


	@commands.cooldown(2, 10, commands.BucketType.user)
	@commands.command()
	async def truth(self, ctx):
		"""Gives the user a dare to do"""
	
		with open("cogs/docs/json/responses.json") as f:
			data = json.load(f)
			truthList = dict
			for i in data:
				for x in i:
					if x == "truth":
						truthList = i['truth']
			selectedTruth = random.choice(truthList)

		truthEmbed = discord.Embed(
			title="Truth",
			description=selectedTruth,
			color=random.choice(randomColour)
		)
		truthEmbed.set_footer(
			text=f"Truth asked by {ctx.author.name}",
			icon_url=ctx.author.avatar_url
		)
		await ctx.reply(embed=truthEmbed, mention_author=False)



	@commands.command(aliases=["wouldyourather"])
	async def wyr(self,ctx):
		"""Would you rather questions"""

		with open("cogs/docs/json/responses.json") as f:
			data = json.load(f)
			wyrList = dict
			for i in data:
				for x in i:
					if x == "would you rather":
						wyrList = i['would you rather']
			selectedChoice = random.choice(wyrList)

		wyrEmbed = discord.Embed(
			title="Would you rather",
			description=selectedChoice,
			color=random.choice(randomColour)
		)
		wyrEmbed.set_footer(
			text=f"Asked by {ctx.author.name}",
			icon_url=ctx.author.avatar_url
		)
		await ctx.reply(embed=wyrEmbed, mention_author=False)



def setup(client):
	client.add_cog(Games(client))
