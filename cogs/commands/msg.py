import discord
from discord.ext import commands
import random

randomColour = [
	0xFF0000, 0x0000FF, 0x008000, 0xFFFF00, 0xFFA500, 0x800080, 0xFFC0CB,
	0x000000, 0x964B00, 0xFFFFFF, 0xFF00FF, 0x00FFFF, 0x32CD32, 0x808080,
	0x89CFF0, 0x800000, 0xFDFD96, 0x77dd77, 0xff6961, 0xC3B1E1
]

client = discord.Client()

randomNumber_causeRandint_isntWorking = [1, 2]

def intCheck(value):
	"""Function used to check if a value is an integer"""
	try:
		int(value)
		return True
	except ValueError or TypeError:
		return False

class Message(commands.Cog):
	def __init__(self, client):
		self.client = client


	@commands.cooldown(3, 10, commands.BucketType.user)
	@commands.has_permissions(manage_messages=True)
	@commands.command(aliases=['delete', 'del', 'clear', 'clr'])
	async def purge(self, ctx, amount):
		"""This command deletes an amount of messages specified by the command author"""
		purgeMessage = discord.Embed(
			title=f"{amount} messages have been deleted",
			color=0xFF0000
		)
		purgeMessage.set_footer(
			text=f"purged by {ctx.author.display_name}",
			icon_url=ctx.author.avatar_url
		)
		isInt = intCheck(amount)
		if isInt:
			await ctx.channel.purge(limit=int(amount)+1)
			await ctx.send(embed=purgeMessage)
		else:
			await ctx.reply(f":x: **I can't purge '{amount}' messages idiot. Say a number like 1 or 2**")





	global snipes
	snipes = {}
	snipe_counter = 0
	@commands.Cog.listener()
	async def on_message_delete(self, message):
		"""This stores the last deleted message by any user on any server"""

		if message.author.bot:
			return
		snipes[message.channel.id] = message

	@commands.cooldown(1, 3, commands.BucketType.user)
	@commands.command()
	async def snipe(self, ctx):
		"""This command sends back the most recently deleted message on a server"""

		#im not bothering explaining how this command works, idk either lolw

		channel_id = ctx.channel.id
		try:
			snipe = snipes[channel_id]
		except KeyError:
			await ctx.send('Nothing to snipe, sorry.')
			return

		embed = discord.Embed()
		embed.set_author(name=f"{snipe.author}",
						icon_url=snipe.author.avatar_url)
		embed.description = snipe.content
		embed.color = 0xff6961
		embed.timestamp = snipe.created_at
		embed.set_footer(text=f"Sniped by {ctx.author.display_name}\n",
						icon_url=ctx.author.avatar_url)
		await ctx.send(embed=embed)




	@commands.cooldown(2, 5, commands.BucketType.user)
	@commands.command()
	async def leetify(self, ctx, *, message="Nothing to leetify"):
		"""Converts text a user sent into leet text"""

		word = message
		word = word.lower()
		word = word.replace('a', '4')
		word = word.replace('e', '3')
		word = word.replace('g', '6')
		word = word.replace('i', '1')
		word = word.replace('o', '0')
		word = word.replace('s', '5')
		word = word.replace('t', '7')
		word = word.replace('l', '1')
		await ctx.send(word)



	
	@commands.cooldown(2, 5, commands.BucketType.user)
	@commands.command()
	async def binary(self,ctx,*,message='Nothing to binaryify'):
		"""Converts what the user said to the binary equivelant"""

		word = message
		word = word.lower()
		word = word.replace('a',' 00001 ')
		word = word.replace('b',' 00010 ')
		word = word.replace('c',' 00011 ')
		word = word.replace('d',' 00100 ')
		word = word.replace('e',' 00101 ')
		word = word.replace('f',' 00110 ')
		word = word.replace('g',' 00111 ')
		word = word.replace('h',' 01000 ')
		word = word.replace('i',' 01001 ')
		word = word.replace('j',' 01010 ')
		word = word.replace('k',' 01011 ')
		word = word.replace('l',' 01100 ')
		word = word.replace('m',' 01101 ')
		word = word.replace('n',' 01110 ')
		word = word.replace('o',' 01111 ')
		word = word.replace('p',' 10000 ')
		word = word.replace('q',' 10001 ')
		word = word.replace('r',' 10010 ')
		word = word.replace('s',' 10011 ')
		word = word.replace('t',' 10100 ')
		word = word.replace('u',' 10101 ')
		word = word.replace('v',' 10110 ')
		word = word.replace('w',' 10111 ')
		word = word.replace('x',' 11000 ')
		word = word.replace('y',' 11001 ')
		word = word.replace('z',' 11010 ')
		await ctx.send(word)


	@commands.command()
	async def quote(self, ctx, msgLink, channel):
		"""Sends a message link to a channel"""
		# do this command




def setup(client):
	client.add_cog(Message(client))
