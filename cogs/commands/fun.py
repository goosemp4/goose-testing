import discord, json, randfacts, random
from discord.ext import commands
from random import randint



randomColour= [0xFF0000,0x0000FF,0x008000,0xFFFF00,0xFFA500,0x800080,0xFFC0CB,0x000000,0x964B00,0xFFFFFF, 0xFF00FF, 0x00FFFF, 0x32CD32, 0x808080, 0x89CFF0, 0x800000, 0xFDFD96, 0x77dd77, 0xff6961, 0xC3B1E1]


class Fun(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.cooldown(3, 6, commands.BucketType.user)
	@commands.command(aliases = ['rf', 'randfact'])
	async def randomfact(self, ctx):
		"""This function produces a random fact from the randfact API and sends it."""

		random_fact = randfacts.getFact() # gets fact from api

		embed = discord.Embed(
		title='Random Fact',
		description=random_fact, # setting fact as api message
		color=random.choice(randomColour),
		)
		embed.set_footer(
		text=f'Requested by {ctx.message.author.display_name}',
		icon_url=ctx.author.avatar_url
		)
		await ctx.send(embed=embed)



	@commands.cooldown(2, 6, commands.BucketType.user)
	@commands.command(aliases = ['8ball', '8b'])
	async def eightball(self, ctx, *, message=None):
		"""Sends a magic 8-ball type message in response to a question"""

		# list of all the responses
		ball_msg = ["Yes","No","Maybe","Perhaps","I think it would be better if you didn't know...","I wouldn't count on it","Sorry, what was the question again?","lmao no","Fuck if I know, go ask someone else","Fuck do I look like? A genie?","From what I can tell, yes","Most likely","Most likely not","You decide","Yeah probably","Probably not","I can without a doubt say **yes** to this.","I can without a doubt say **no** to this.","Fuck yeah","Fuck no", "Man, I'm not even gonna answer that shit", "Idk lol"]
		if message is None:
			await ctx.reply("**Ask a question and I'll tell you your fortune.**")
			return
		if message is not None:
			embed = discord.Embed(
				title = f":8ball: \"{message}\"", # gets a random response from the list
				color = random.choice(randomColour)
			)
			embed.add_field(
				name = random.choice(ball_msg),
				value = "⠀"
			)
			embed.set_footer(
				text = f"{ctx.author.display_name}'s fortune",
				icon_url=ctx.author.avatar_url
			)

		await ctx.reply(embed=embed) # reply saying their fortune

		

	@commands.cooldown(1, 3, commands.BucketType.user)
	@commands.command(aliases= ['Kill'])
	async def kill(self, ctx, member: discord.Member, gif=None):
		"""This command kills a user in a random way or with a gif"""

		# if the user does not want a gif
		if gif is None:

			# if its bag head
			if member.id == 795762695403732993:
				await ctx.reply("You go to kill me but I just say no and you stop trying. Dick.")
				return

			# if its no one
			if member is None:
				await ctx.send(f'**{ctx.message.author.display_name}** kills no one. alright then lmao.')
		
			# if its themself
			if member.mention == ctx.message.author.mention:
				await ctx.send("You kill yourself. You wanna talk about something?")
				return

			if member.mention != ctx.message.author.mention:
				with open("cogs/docs/json/responses.json") as f:
					data = json.load(f)
					killList = dict
					for i in data:
						for x in i:
							if x == "kill":
								killList = i['kill']
					killResponse = random.choice(killList)
					killResponse = killResponse.replace('author', f"**{ctx.message.author.display_name}**").replace('member', f"**{member.display_name}**")
					await ctx.send(killResponse)
		
		# if the user wants a gif
		elif gif.lower() == "gif":
			with open('docs/cmds/kills/kill_title.txt') as f:

				kill_responses = f.read().splitlines()
				kill = random.choice(kill_responses)
				gif_num = kill[-1]
				if gif_num == "*":
					gif_num = randint(1,3)

				elif gif_num != "*":
					kill = kill.replace('author', f"__{ctx.message.author.display_name}__").replace('member', f"__{member.display_name}__")
					
				kill = kill[:-1]
				f.close()
				slap_dir = f"docs/images/kill/bag_kill{gif_num}.gif"
				slap_file = discord.File(slap_dir, filename = "kill.gif")

				embed = discord.Embed(
					title=kill,
					color=random.choice(randomColour)
				)
				embed.set_image(
					url=f"attachment://kill.gif"
				)
				embed.set_footer(
					text=f"{ctx.author.display_name} kills {member.display_name}",
					icon_url=ctx.author.avatar_url
				)


				await ctx.send(file=slap_file, embed=embed)




	@commands.cooldown(1, 3, commands.BucketType.user)
	@commands.command(aliases= ['Slap'])
	async def slap(self, ctx, member: discord.Member=None, gif=None):
		"""Slaps another user with a random way or a gif"""

		# if the user does not want a gif
		if gif is None:

			# if its bag head
			if member.id == 795762695403732993:
				await ctx.send("You try and slap me but you can't because I make the rules.")
				return

			# if its no one
			if member is None:
				await ctx.send(f'**{ctx.message.author.display_name}** slaps the air.')
				return
			
			# if its themself
			if member.mention == ctx.message.author.mention:
				await ctx.send("You slap yourself. ok then lol.")
				return

			if member.mention != ctx.message.author.mention:
				with open("cogs/docs/json/responses.json") as f:
					data = json.load(f)
					slapList = dict
					for i in data:
						for x in i:
							if x == "slap":
								slapList = i['slap']
					slapResponse = random.choice(slapList)
					slapResponse = slapResponse.replace('author', f"**{ctx.message.author.display_name}**").replace('member', f"**{member.display_name}**")
					await ctx.send(slapResponse)
		
		if gif.lower() == "gif":
			with open('docs/cmds/slaps/slap_title.txt') as f:

				slap_responses = f.read().splitlines()
				slap = random.choice(slap_responses)
				gif_num = slap[-1]

				if gif_num == "*":
					gif_num = randint(1,17)

				elif gif_num != "*":
					slap = slap.replace('author', f"__{ctx.message.author.display_name}__").replace('member', f"__{member.display_name}__")
					
				slap = slap[:-1]
				f.close()
				slap_dir = f"docs/images/slap/bag_slap{gif_num}.gif"
				slap_file = discord.File(slap_dir, filename = "slap.gif")

				embed = discord.Embed(
					title=slap,
					color=random.choice(randomColour)
				)
				embed.set_image(
					url=f"attachment://slap.gif"
				)
				embed.set_footer(
					text=f"{ctx.author.display_name} slaps {member.display_name}",
					icon_url=ctx.author.avatar_url
				)
				await ctx.send(file=slap_file, embed=embed)
			



	@commands.cooldown(1, 3, commands.BucketType.user)
	@commands.command()
	async def throw(self, ctx, member: discord.Member=None):
		"""This command throws a random object at another user"""

		# if its no one
		if member is None:
			await ctx.send("Ping someone to throw something at them")
			return

		# if its bag head
		if member.id == 795762695403732993:
			await ctx.send("You throw something at me but I catch it and throw it back at you.")
			return

		# if its themself
		if member.mention == ctx.message.author.mention:
			await ctx.send("You can't throw something at yourself, idiot.")
			return

		if member.mention != ctx.message.author.mention:
			with open("cogs/docs/json/responses.json") as f:
				data = json.load(f)
				throwList = dict
				for i in data:
					for x in i:
						if x == "throw":
							throwList = i['throw']
				throwResponse = random.choice(throwList)
				throwResponse = throwResponse.replace('author', f"**{ctx.message.author.display_name}**").replace('member', f"**{member.display_name}**")
				await ctx.send(throwResponse)



	@commands.cooldown(1, 3, commands.BucketType.user)
	@commands.command()
	async def highfive(self, ctx, member: discord.Member):
		"""Highfive another user"""

		await ctx.send(f'{ctx.message.author.mention} highfives {member.mention}. :hand_splayed:')




	@commands.command()
	async def pat(self, ctx, member: discord.Member=None):
		"""Pats another user"""

		# if its no one
		if member is None:
			await ctx.send("You have to ping someone to pat.")
			return

		# if its bag head
		if member.id == 795762695403732993:
			await ctx.send("Thanks but no thanks.")
			return

		# if its themself
		if member.mention == ctx.message.author.mention:
			await ctx.send(f"**{ctx.message.author.display_name}** pats themselves on the head.")
			return

		if member.mention != ctx.message.author.mention:
			with open("cogs/docs/json/responses.json") as f:
				data = json.load(f)
				patList = dict
				for i in data:
					for x in i:
						if x == "pat":
							patList = i['pat']
				patResponse = random.choice(patList)
				patResponse = patResponse.replace('author', f"**{ctx.message.author.display_name}**").replace('member', f"**{member.display_name}**")
				await ctx.send(patResponse)



	@commands.cooldown(1, 3, commands.BucketType.user)
	@commands.command()
	async def hug(self, ctx, member : discord.Member):
		"""Hugs another user"""

		with open("cogs/docs/json/responses.json") as f:
			data = json.load(f)
			hugList = dict
			for i in data:
				for x in i:
					if x == "hug":
						hugList = i['hug']
			hugResponse = random.choice(hugList)
			hugResponse = hugResponse.replace('author', f"**{ctx.message.author.display_name}**").replace('member', f"**{member.display_name}**")
			await ctx.send(hugResponse)


	@commands.cooldown(1, 3, commands.BucketType.user)
	@commands.command()
	async def insult(self, ctx, member:discord.Member=None):
		"""Sends an insult to a targeted user"""

		# if you try to insult bag head
		if member.id == 795762695403732993:
			await ctx.send("No, fuck you.")
			return

		# if they dont include anyone
		if member is None:
			await ctx.send(f'**{ctx.message.author.display_name}** says some choice words to the air.')
			return
		
		# if they insult themselves. lol
		if member.mention == ctx.message.author.mention:
			await ctx.send("Ok, you're stupid. Ping someone else to insult them.")
			return

		if member.mention != ctx.message.author.mention:

			# get a random line from insult.txt and make it the message.
			with open("cogs/docs/json/responses.json") as f:
				data = json.load(f)
				insultList = dict
				for i in data:
					for x in i:
						if x == "insult":
							insultList = i['insult']
				insult = random.choice(insultList)
				insult = insult.replace('author', f"**{ctx.message.author.display_name}**").replace('member', f"**{member.display_name}**")
				await ctx.send(insult)




	@commands.cooldown(1, 3, commands.BucketType.user)
	@commands.command()
	async def kiss(self, ctx, member : discord.Member=None):
		"""Give another user a big ol' smooch ;)"""

		if member is None:
			await ctx.send("Ping someone to give them a kiss.")

		elif member.mention == ctx.message.author.mention:
			await ctx.send('You walk up to a mirror and "kiss" yourself')

		elif member.mention != ctx.message.author.mention and member is not None:
			with open("cogs/docs/json/responses.json") as f:
				data = json.load(f)
				kissList = dict
				for i in data:
					for x in i:
						if x == "kiss":
							kissList = i['kiss']
				kissResponse = random.choice(kissList)
				kissResponse = kissResponse.replace('author', f"**{ctx.message.author.display_name}**").replace('member', f"**{member.display_name}**")
				await ctx.send(kissResponse)




	@commands.cooldown(1, 5, commands.BucketType.user)
	@commands.command(aliases = ['av', 'pfp'])
	async def avatar(self, ctx, *, member : discord.Member=None):
		"""Gets the users avatar and sends it"""

		# if the author puts no one as the members, automatically make it them
		if member is not None:
			embed  = discord.Embed(
				title = f'{member.display_name}\'s avatar',
				color = random.choice(randomColour),
			)
			embed.set_footer(
				text=f"Avatar grabbed by {ctx.author.display_name}",
				icon_url=ctx.author.avatar_url
			)
			embed.set_image(url=ctx.author.avatar_url)
			embed.set_image(url=member.avatar_url)
			await ctx.send(embed=embed)

		# if the author actually puts a user
		elif member is None:
			embed  = discord.Embed(
				title = f'{ctx.author.display_name}\'s avatar',
				color = random.choice(randomColour),
			)
			embed.set_footer(
				text=f"Avatar grabbed by {ctx.author.display_name}",
				icon_url=ctx.author.avatar_url
			)
			embed.set_image(url=ctx.author.avatar_url)
			await ctx.send(embed=embed)

	@commands.cooldown(3, 5, commands.BucketType.user)
	@commands.command(aliases=["ppsize"])
	async def pp(self, ctx):
		size = randint(1,25)
		if size > 20:
			size = randint(1,25)
			if size > 20:
				size = randint(1,50)
				if size > 45:
					size = randint(1,50)
		
		stock = ""
		for i in range(size):
			stock = stock + "="
		
		ppEmbed = discord.Embed(
			title=f"{ctx.author.name}'s pp size",
			description=f"8{stock}D",
			color=random.choice(randomColour)
		)
		ppEmbed.set_footer(
			text=f"{size} inches",
			icon_url=ctx.author.avatar_url
		)
		await ctx.send(embed=ppEmbed)

	
	@commands.command()
	async def ship(self, ctx, member:discord.Member, member2:discord.Member=None):
		shipMeter = randint(1,100)

		if member2 is None:
			member2 = ctx.author

		shipEmbed = discord.Embed(
			title=f"{shipMeter}%",
			description=f"**{member.name}**   :heart:   **{member2.name}**",
			color=random.choice(randomColour)
		)
		await ctx.send(embed=shipEmbed)



	@commands.command()
	async def gay(self, ctx, member:discord.Member=None):

		if member is None:
			member = ctx.author

		gayPerc = randint(1,100)

		gayEmbed = discord.Embed(
			title=f"{member.name} is {gayPerc}% gay :rainbow_flag: ",
			colour=random.choice(randomColour)
		)
		
		await ctx.send(embed=gayEmbed)



	# -------------------------------
def setup(client):
	client.add_cog(Fun(client))
	