import discord, random, os
from discord.ext import commands
from random import randint

randomColour= [0xFF0000,0x0000FF,0x008000,0xFFFF00,0xFFA500,0x800080,0xFFC0CB,0x000000,0x964B00,0xFFFFFF, 0xFF00FF, 0x00FFFF, 0x32CD32, 0x808080, 0x89CFF0, 0x800000, 0xFDFD96, 0x77dd77, 0xff6961, 0xC3B1E1]

client = discord.Client()

class Secret(commands.Cog):

	def __init__(self, client):
		self.client = client

	"""
	SECRET COMMANDS

	Secret commands are commands that are not listed! They have a 5 minute cooldown and delete the command call in chat after being used.

	SECRET COMMANDS
	"""


	@commands.cooldown(1, 300, commands.BucketType.user)
	@commands.command()
	async def fart(self,ctx):
		"""Release immense gas in the chat."""

		gif_num = randint(1,5)
		fart_dir = f"docs/images/farts/bag_fart{gif_num}.gif"

		file = discord.File(fart_dir, filename="fart.gif")

		fart_embed = discord.Embed(
			title=f"{ctx.author.display_name} lets one rip"
		)
		fart_embed.set_image(
			url="attachment://fart.gif"
		)
		fart_embed.set_footer(
			text="This is a secret command",
			icon_url=ctx.author.avatar_url
		)

		await ctx.channel.purge(limit=2)
		await ctx.send(file=file, embed=fart_embed, delete_after=10)




	@commands.cooldown(1, 300, commands.BucketType.user)
	@commands.command()
	async def secret(self,ctx):
		"""If the user does `>secret`, do this command"""

		await ctx.channel.purge(limit=1)
		file_dir = "docs/images/bag_secret.gif" # gets secret gif

		file = discord.File(file_dir, filename="secret.gif") # assigns a file

		embed = discord.Embed(
			title="Shhh! You're using a secret command!",
			description=
			"Lets keep this between us :eyes:"
		)
		embed.set_image(
			url="attachment://secret.gif"
		)
		embed.set_footer(
			text="You've found a secret command! Wonder if there is any more..."
		)

		await ctx.send(file=file, embed=embed, delete_after=5)



def setup(client):
	client.add_cog(Secret(client))