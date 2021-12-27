import discord, os, random, json
from dateutil.relativedelta import *
from dateutil.easter import *
from dateutil.rrule import *
from dateutil.parser import *
from datetime import *
import datetime
from discord.ext import commands
from random import randint

client = discord.Client()

randomColour= [0xFF0000,0x0000FF,0x008000,0xFFFF00,0xFFA500,0x800080,0xFFC0CB,0x000000,0x964B00,0xFFFFFF, 0xFF00FF, 0x00FFFF, 0x32CD32, 0x808080, 0x89CFF0, 0x800000, 0xFDFD96, 0x77dd77, 0xff6961, 0xC3B1E1]

class Moderation(commands.Cog):

	def __init__(self, client):
		self.client = client



	@commands.command()
	@commands.has_permissions(kick_members=True)
	async def kick(self, ctx, member : discord.Member=None, *, reason=None):
		"""This command kicks a members from a server."""

		if member is None:
			await ctx.reply("**You need to ping someone to kick.\nExample: `@asshole#1234`**")
		elif reason is None:
			await ctx.reply("**You should supply a reason next time. \nExample: `>kick @asshole#1234 being an asshole.`**")
		if member is not None:
			
			memberEmbed = discord.Embed(
				title=f"You've been kicked from {ctx.message.guild.name}",
				description = f"Reason: {reason}",
				color=0x2F3136
			)
			await member.send(embed=memberEmbed)

			await member.kick(reason=reason)
			kick = discord.Embed(
				title = f'Kick Ticket',
				color = 0x2F3136,
			)
			kick.add_field(
				name="Kicked User",
				value=member.mention
			)
			kick.add_field(
				name="Reason",
				value=reason,
				inline=False
			)
			kick.add_field(
				name="ID",
				value=member.id
			)
			kick.set_footer(
				text = f'Kick was issued by {ctx.message.author}',
				icon_url=ctx.author.avatar.url,
			)
			imgFile = discord.File("docs/images/bagHead_modAction.png", filename="image.png")
			kick.set_thumbnail(
				url="attachment://image.png"
			)
			await ctx.send(file=imgFile, embed=kick)



	@commands.command()
	@commands.has_permissions(ban_members=True)
	async def ban(self, ctx, member:discord.Member, *, reason=None):
		"""This command bans a user from a server"""

		if member is None:
			await ctx.send("**You need to ping someone to kick.\nExample: `@asshole#1234`**")
			return
		elif reason is None:
			await ctx.send("**You should supply a reason next time. Example: `>ban @asshole#1234 being an asshole.`**")

		if member is not None:

			memberEmbed = discord.Embed(
				title=f"You've been banned from {ctx.message.guild.name}",
				description = f"Reason: {reason}",
				color=0x2F3136
			)
			await member.send(embed=memberEmbed)


			await member.ban(reason=reason)
			ban = discord.Embed(
			title = f'Ban Ticket',
			color = 0x2F3136,
			)
			ban.add_field(
				name="Banned User",
				value=member.mention
			)
			ban.add_field(
				name="Reason",
				value=reason,
				inline=False
			)
			ban.add_field(
				name="ID",
				value=member.id
			)
			ban.add_field(
				name="Unban Command",
				value=">unban userID"
			)
			ban.set_footer(
				text = f'Ban was issued by {ctx.message.author}',
				icon_url=ctx.author.avatar.url,
			)
			imgFile = discord.File("docs/images/bagHead_modAction.png", filename="image.png")
			ban.set_thumbnail(
				url="attachment://image.png"
			)
			await ctx.send(file=imgFile, embed=ban)



	@commands.cooldown(3, 5, commands.BucketType.user)
	@commands.command(pass_context=True)
	@commands.has_permissions(ban_members=True)
	async def unban(self, ctx, id: int):
		"""This command unbans a user based on their user ID"""

		user = await self.client.fetch_user(id)
		await ctx.guild.unban(user)
		unban_message = f'{user} has been unbanned'

		embed = discord.Embed(
			title = 'Unban',
			description = unban_message,
			color = 0x2F3136,
		)
		imgFile = discord.File("docs/images/bagHead_modAction.png", filename="image.png")
		embed.set_thumbnail(
			url="attachment://image.png"
		)
		await ctx.send(file=imgFile, embed=embed)



	@commands.cooldown(1, 1, commands.BucketType.user)
	@commands.command()
	async def afk(self, ctx, member:discord.Member):
		"""Sets a person as AFK in a server until they are back"""


		with open("docs/json/afk.json") as f:
			afk = json.load(f)

		afkNick = f"[AFK] {ctx.author.display_name}"
		await ctx.author.edit(nick=afkNick)



	@commands.cooldown(1, 15, commands.BucketType.user)
	@commands.command()
	async def membercount(self, ctx):
		"""This command gets the number of members in the server this was called in"""

		total = len(ctx.guild.members)

		embed = discord.Embed(
			title='<:bagHead:890566843549491250> Member Count',
			description=f'**There are __{total}__ members on this server.**',
			color=random.choice(randomColour)
		)
		await ctx.send(embed=embed)



	@commands.command(pass_context=True)
	@commands.has_permissions(administrator=True)
	async def info(self, ctx, member : discord.Member):
		"""Gets information on the user"""


		roleList = [] # pre-defining the list to use when grabbing the server's roles
		memberRoles = [] # pre-defining the list of roles the member has

		for role in ctx.guild.roles:
			roleList.append(role.id) # add all the roles in the server to a list

		# if the member has a role listed in the array (also called list), append it to the memberRoles list
		for roles in member.roles:
			if roles.id in roleList:
				memberRoles.append(roles.id)
			else:
				pass
		memberRoles.reverse() # reversing the order because it goes reverse normally
		
		# makes a str that has all of the users roles
		rolesStr = "" 
		for i in memberRoles:
			rolesStr += f"<@&{i}>\n"

		roleEmbed = discord.Embed(
			title=f"{member}",
			description=f"<@{member.id}>",
			color=0x2F3136
		)

		roleEmbed.add_field(
			name="Roles",
			value=rolesStr,
			inline=False
		)

		roleEmbed.add_field(
			name="Server Nickname",
			value=member.display_name
		)

		roleEmbed.add_field(
			name="Created On",
			value=member.created_at,			
		)

		roleEmbed.add_field(
			name="Joined Server On",
			value=member.joined_at
		)

		roleEmbed.add_field(
			name="User ID",
			value=member.id
		)

		# checks if user is a bot
		if member.bot:
			botStr = "Yes"
		elif not member.bot:
			botStr = "No"
		roleEmbed.add_field(
			name="Bot",
			value=botStr
		)

		# checks if a user is admin
		if member.guild_permissions.administrator is True:
			adminStr = "Yes"
		else:
			adminStr = "No"
		roleEmbed.add_field(
			name="Admin",
			value=adminStr
		)

		roleEmbed.set_thumbnail(
			url=member.avatar.url
		)

		await ctx.send(embed=roleEmbed)
				

	@commands.command()
	@commands.has_permissions(manage_roles=True)
	async def role(self, ctx, member:discord.Member, mode, role:discord.Role):
		if mode != "+" and mode != "-":
			await ctx.reply("**You need to provide if you're adding or removing a role.\n`+` to add, `-` to remove**")
		elif mode == "+":
			await member.add_roles(role)
			await ctx.reply(f"**{role.name} added to {member.name}**")
		elif mode == "-":
			await member.remove_roles(role)
			await ctx.reply(f"**{role.name} removed from {member.name}**")



	@commands.command(aliases=["permissions"])
	async def perms(self, ctx, member: discord.Member = None):
		await ctx.reply("**Command not finished!**")


	@commands.command()
	@commands.has_permissions(manage_roles=True)
	async def mute(self, ctx, member:discord.Member, duration, reason=None):
		
		time_now = discord.utils.utcnow()

		for i in duration:
			if i == "s":
				duration_int = duration.replace("s","")
				duration_int = int(duration_int)
				added_time = datetime.timedelta(seconds=duration_int)

			elif i == "m":
				duration_int = duration.replace("m","")
				duration_int = int(duration_int)
				added_time = datetime.timedelta(minutes=duration_int)

			elif i == "h":
				duration_int = duration.replace("h","")
				duration_int = int(duration_int)
				added_time = datetime.timedelta(hours=duration_int)

			elif i == "d":
				duration_int = duration.replace("d","")
				duration_int = int(duration_int)
				added_time = datetime.timedelta(days=duration_int)

			elif i == "y":
				duration_int = duration.replace("y","")
				duration_int = int(duration_int)
				added_time = datetime.timedelta(years=duration_int)
			else:
				pass
				
		if not int(duration_int):
			return
		timeout_dur = time_now + added_time

		await member.timeout(until=timeout_dur, reason=reason)

		mutedEmbed = discord.Embed(
			title=f"Muted {member.name}",
			description=f"Duration: {duration}\nReason: {reason}",
			color=0x2F3136
		)
		mutedEmbed.set_footer(
			text=f"Muted by {ctx.author.name}",
			icon_url=ctx.author.avatar.url
		)

		imgFile = discord.File("docs/images/bagHead_modAction.png", filename="image.png")
		
		mutedEmbed.set_thumbnail(
			url="attachment://image.png"
		)
		await ctx.send(embed=mutedEmbed,file=imgFile)


	@commands.command()
	@commands.has_permissions(manage_roles=True)
	async def unmute(self, ctx, member:discord.Member, reason=None):
		
		await member.remove_timeout(reason=reason)

		unmutedEmbed = discord.Embed(
			title=f"Unmuted {member.name}",
			description=f"Reason: {reason}",
			color=0x2F3136
		)
		unmutedEmbed.set_footer(
			text=f"Unmuted by {ctx.author.name}",
			icon_url=ctx.author.avatar.url
		)

		imgFile = discord.File("docs/images/bagHead_modAction.png", filename="image.png")

		unmutedEmbed.set_thumbnail(
				url="attachment://image.png"
		)

		await ctx.send(embed=unmutedEmbed, file=imgFile)


def setup(client):
	client.add_cog(Moderation(client))