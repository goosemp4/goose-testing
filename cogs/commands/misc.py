import discord
from discord.ext import commands
import random

randomColour = [
	0xFF0000, 0x0000FF, 0x008000, 0xFFFF00, 0xFFA500, 0x800080, 0xFFC0CB,
	0x000000, 0x964B00, 0xFFFFFF, 0xFF00FF, 0x00FFFF, 0x32CD32, 0x808080,
	0x89CFF0, 0x800000, 0xFDFD96, 0x77dd77, 0xff6961, 0xC3B1E1
]


class Misc(commands.Cog):
	def __init__(self, client):
		self.client = client


	@commands.cooldown(1, 15, commands.BucketType.user)
	@commands.command()
	async def vote(self, ctx):
		"""Sends a link to the top.gg website to vote for Bag Head"""
	
		embed = discord.Embed(
			title="<:bagHead:890566843549491250> Vote for Bag Head on top.gg",
			description="Click [here](https://top.gg/bot/795762695403732993/vote) to vote.",
			color=random.choice(randomColour),
		)
		await ctx.send(embed=embed)




	@commands.cooldown(1, 15, commands.BucketType.user)
	@commands.command()
	async def donate(self, ctx):
		"""Sends a link to the donation page where users can donate"""

		embed = discord.Embed(
			title='<:bagHead:890566843549491250> Donate pls',
			description=
			"Click [here](https://donatebot.io/checkout/795764929063682109) to donate.")
		await ctx.send(embed=embed)
		logChannel = self.client.get_channel(869019940680769646)
		await logChannel.send(f"**{ctx.author}** used the __Donate__ command.")




	@commands.command()
	async def invite(self, ctx):
		"""Sends an invite link to the user so they can invite the bot to another server"""

		invite = discord.Embed(
			title="<:bagHead:890566843549491250> Invite",
			description = "Click [here](https://discord.com/api/oauth2/authorize?client_id=795762695403732993&permissions=372501511&scope=bot) to invite me to another server.",
			color = random.choice(randomColour)
		)
		await ctx.send(embed=invite)




	@commands.cooldown(2, 15, commands.BucketType.user)
	@commands.command(aliases = ['report'])
	async def bug(self, ctx, *, bug_msg):
		"""Allows users to report bugs about the bug. They are logged in the interal server"""

		if bug_msg is None:
			await ctx.reply("<:bagHead:890566843549491250> Please supply a bug! *idiot...*")

		elif bug_msg is not None:

			# creates an embed to reply to the user with
			bugReply = discord.Embed(
				title="Thank you for reporting a bug! You're pretty swag.",
				colour=0x77dd77
			)
			await ctx.reply(embed=bugReply)


			channel = self.client.get_channel(869013037540057098) # gets the internals bug report channel

			bugEmbed = discord.Embed(
				title="Bug Reported",
				description=bug_msg
			)
			bugEmbed.set_author(
				name=ctx.author,
				icon_url=ctx.author.avatar_url
			)
			bugEmbed.add_field(
				name="Reported by",
				value=f"<@{ctx.author.id}>"
			)

			await channel.send(embed=bugEmbed)
			return




	@commands.cooldown(2, 15, commands.BucketType.user)
	@commands.command(aliased =["suggsestion"])
	async def suggest(self, ctx, *, suggestion=None):
		"""Allows users to report bugs about the bug. They are logged in the interal server"""

		if suggestion is None:
			await ctx.reply("<:bagHead:890566843549491250> Please supply a suggestion! *idiot...*")

		elif suggestion is not None:

			# creates an embed to reply to the user with
			suggestReply = discord.Embed(
				title="Thank you for this suggestion! If it's cool enough, it might just be added.",
				colour=0x77dd77
			)
			await ctx.reply(embed=suggestReply)


			channel = self.client.get_channel(869013019714281472) # gets the internals bug report channel

			suggestEmbed = discord.Embed(
				title="Suggestion",
				description=suggestion
			)
			suggestEmbed.set_author(
				name=ctx.author,
				icon_url=ctx.author.avatar_url
			)
			suggestEmbed.add_field(
				name="Suggested by",
				value=f"<@{ctx.author.id}>"
			)

			await channel.send(embed=suggestEmbed)
			return


	@commands.command(aliases=["ping"])
	async def isalive(self, ctx):
		await ctx.reply("**Alive and working!**")



# -------------------------------
def setup(client):
	client.add_cog(Misc(client))
