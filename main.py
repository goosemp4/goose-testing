import discord, random, os
from discord.ext import commands
from keep_alive import keep_alive
from discord.utils import find
# discord.py API docs: https://discordpy.readthedocs.io/en/latest/api.html
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='>', intents=intents)
client.remove_command('help')


# prints on the console that the bot is up and running and changes the status
@client.event
async def on_ready():
	print(
		"\n\n-------------------------\nBAG HEAD IS ONLINE\n-------------------------\n\n"
	)
	await client.change_presence(activity=discord.Activity(
		type=discord.ActivityType.playing, name=f">help | In {str(len(client.guilds))} servers")) # changes the presence


# sends a message when it joins the server for the first time. doesnt send if the server doesnt have a general channel
@client.event
async def on_guild_join(guild):
	embed = discord.Embed(
		title="Thank you for inviting me!",
		description=
		"Thank you for inviting Bag Head to your server.\nTo get started, do `>help` to get a list of all commands.\nOur [support server](https://discord.com/invite/ndMXuqp3uY) is listed on our [top.gg](https://top.gg/bot/795762695403732993) profile and in the help command message."
	)
	general = find(lambda x: x.name == 'general', guild.text_channels) # looks for a channel named general
	if general and general.permissions_for(guild.me).send_messages:
		await general.send(embed=embed)
	
	channel = client.get_channel(869019940680769646)
	await guild.owner.send(embed=embed)
	await channel.send(f"**Joined server**")


# loads all the cogs into 'main.py'
client.load_extension('cogs.commands.fun')
client.load_extension('cogs.commands.msg')
client.load_extension('cogs.commands.mod')
client.load_extension('cogs.commands.games')
client.load_extension('cogs.commands.role')
client.load_extension('cogs.commands.misc')
client.load_extension('cogs.commands.secretCommands')
client.load_extension('cogs.commands.msgTriggers')


# if a command flags an error it handles it
@client.event
async def on_command_error(ctx, error):
	"""Handles errors"""

	error_ping = 0
	
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send(
			"Hey dummy! You're missing something for this command! Try again with the correct format idiot."
		)
		error_type = "MissingRequiredArgument"
		error_ping = 1

	if isinstance(error, commands.BotMissingPermissions):
		await ctx.send(
			"Missing permissions to do this! Please check my permissions and try again dumbass."
		)
		error_type = "BotMissingPermissions"
		error_ping = 1

	if isinstance(error, commands.ChannelNotFound):
		await ctx.send("Channel not found. This is awkward.")
		error_type = "ChannelNotFound"
		error_ping = 1

	if isinstance(error, commands.CommandNotFound):
		return

	if isinstance(error, commands.CommandOnCooldown):
		cooldownMessage = discord.Embed(
			title="Command on Cooldown",
			description="Woah there buster, you're too spicy!\n\nWait between 3-15 seconds before using that command again!",
			color=0xFF0000
		)

		imgFile = discord.File("docs/images/bagHead_angry.png", filename="angry.png")
		cooldownMessage.set_thumbnail(
			url="attachment://angry.png"
		)
		await ctx.reply(file=imgFile, embed=cooldownMessage)
		error_type = "CommandOnCooldown"
		error_ping = 1

	if isinstance(error, commands.NotOwner):
		await ctx.send("Sorry! You're not the owner, you can't do that.")
		error_type = "NotOwner"
		error_ping = 1

	if isinstance(error, commands.MemberNotFound):
		await ctx.send(
			"This is awkward, I can't find that member. Try again maybe?")
		error_type = "MemberNotFound"
		error_ping = 1

	if isinstance(error, commands.MissingRole):
		error_type = "MissingRole"
		error_ping = 1

	if isinstance(error, commands.TooManyArguments):
		error_type = "TooManyArguments"
		error_ping = 1

	if isinstance(error, commands.RoleNotFound):
		await ctx.send(
			"I can't find that role. It's either not there or your didn't spell it correctly. Idiot"
		)
		error_type = "RoleNotFound"
		error_ping = 1

	if isinstance(error, commands.UserNotFound):
		await ctx.send("I can't find that user. Weird...")
		error_type = "UserNotFound"
		error_ping = 1

	if isinstance(error, commands.UserInputError):
		return

	if isinstance(error, commands.ArgumentParsingError):
		error_type = "ArgumentParsingError"
		error_ping = 1

	if isinstance(error, commands.BadArgument):
		error_type = "BadArgument"
		error_ping = 1

	if isinstance(error, commands.BadBoolArgument):
		error_type = "BadBoolArgument"
		error_ping = 1

	if isinstance(error, commands.BadColourArgument):
		error_type = "BadColourArgument"
		error_ping = 1

	if isinstance(error, commands.BadInviteArgument):
		error_type = "BadInviteArgument"
		error_ping = 1

	if isinstance(error, commands.BadUnionArgument):
		error_type = "BadUnionArgument"
		error_ping = 1

	if isinstance(error, commands.CommandError):
		print("")

	if isinstance(error, commands.CommandRegistrationError):
		error_type = "CommandRegistrationError"
		error_ping = 1

	if isinstance(error, commands.ConversionError):
		error_type = "ConversionError"
		error_ping = 1

	if isinstance(error, commands.EmojiNotFound):
		error_type = "EmojiNotFound"
		error_ping = 1

	if isinstance(error, commands.NoPrivateMessage):
		error_type = "NoPrivateMessage"
		error_ping = 1


	if isinstance(error, commands.NSFWChannelRequired):
		error_type = "NSFWChannelRequired"
		error_ping = 1
	
	else:
		raise error


	error_ping = 0
	error_write = open('docs/text/errortrack.txt', 'a')
	error_write.write(f"\n{ctx.author.name}#{ctx.author.discriminator} | {error_type}")
	error_write.close()
	error_type = ""


randomColour = [
	0xFF0000, 0x0000FF, 0x008000, 0xFFFF00, 0xFFA500, 0x800080, 0xFFC0CB,
	0x000000, 0x964B00, 0xFFFFFF, 0xFF00FF, 0x00FFFF, 0x32CD32, 0x808080,
	0x89CFF0, 0x800000, 0xFDFD96, 0x77dd77, 0xff6961, 0xC3B1E1
]


# just hide this
@client.command()
async def upcoming(ctx):
	upcoming = discord.Embed(
		title='Here is a list of upcoming commands and features.',
		color=0x17B15D
	)

	upcoming.add_field(
		name='__ASCII text__',
		value='Converts your message into ASCII.',
	)

	upcoming.add_field(
		name='__Slash Commands__',
		value=
		'Most message commands like leetify, ASCII and maybe some others will be converted into slash commands in the near future.',
	)

	upcoming.add_field(
		name='__Gifs__',
		value='Gifs are to be added to things like kill, throw, etc.',
	)

	upcoming.add_field(
		name='__Join Role__',
		value='Set up roles to give new members that join the server',
	)

	upcoming.add_field(
		name='__Pat__',
		value='Ping a user to pat them on the head.',
	)

	upcoming.add_field(
		name='__Marry__',
		value='Marry another user.',
	)

	upcoming.add_field(
		name='__Fuck__',
		value='Get freaky with another user. :wink: .',
	)

	upcoming.add_field(
		name='__Logs__',
		value=
		'Logs to be added that track deleted messages, edited messages, role changes, etc.'
	)

	newfeatures = discord.Embed(title='Newly Added Features', color=0xFFE662)
	newfeatures.add_field(
		name='__Donate__',
		value=
		'You can now donate if you wish. This does not provide anything **at the moment** but will later on. It\'s really just there for being kind. If you\'d like the benefits that may come for donating in the future, join the support server and simply verify you donated.'
	)

	newfeatures.add_field(
		name='__Avatar Grabber__',
		value='You can now get people\'s avatars.'
	)

	newfeatures.add_field(
		name='__Member count__',
		value='You can new view how many members a discord server has.'
	)

	newfeatures.add_field(
		name='__Help Menu__',
		value='The help menu has finally been updated! Check it out with `>help`'
	)

	newfeatures.add_field(
		name='__Moderation Commands__',
		value='The moderation have gotten a re-work and are much easier to read and provide more information now.'
	)

	newfeatures.add_field(
		name='__Bug Report__',
		value='You can now report bugs! Just do `>bug *msg about bug and what causes it*`'
	)
	newfeatures.add_field(
		name='__Reaction Roles__',
		value='You can now have reaction roles for messages! `>reactrole [channel] [message id] [emoji] [role]`'
	)

	await ctx.send(
		f"**{ctx.author.display_name}**, you've been sent a dm with the upcoming commands."
	)
	await ctx.author.send(embed=upcoming)
	await ctx.author.send(embed=newfeatures)
	print("Upcoming cmd")



# this command displays the help menu which is all the commands + some info.
@commands.cooldown(2, 15, commands.BucketType.user)
@client.command(aliases=["cmds", "commands"])
async def help(ctx, help_type=None):

	if help_type == None:

		help_basic = discord.Embed(
			title = "Help Commands",
			color = random.choice(randomColour)
		)

		help_basic.add_field(
			name=
			"Fun",

			value=
			"`>help fun`"
		)

		help_basic.add_field(
			name=
			"Games",

			value=
			"`>help games`"
		)

		help_basic.add_field(
			name=
			"User Commands",

			value=
			"`>help user`"
		)
		
		help_basic.add_field(
			name=
			"Moderation",

			value=
			"`>help mod`"
		)
		
		help_basic.add_field(
			name=
			"Roles",

			value=
			"`>help role`"
		)

		help_basic.add_field(
			name=
			"Message",

			value=
			"`>help msg`"
		)
		
		help_basic.add_field(
			name=
			"Misc Commands",

			value=
			"`>help misc`"
		)

		help_basic.add_field(
			name="Support Server",

			value = "Join the [support server](https://discord.gg/ndMXuqp3uY) if you need any help.",

			inline=False
		)
		await ctx.send(embed=help_basic)
	

	elif help_type == "fun":
		fun_cmds = discord.Embed(
			title="List of all fun commands",
			description=

			'`>randomfact`\nSends a random fact from the randfact API.\n\n'

			'`>istrue`\nSays its either true or not true.\n\n'

			'`>itisi`\nJust use the command to find out what it does.\n\n'

			'`>8ball msg`\nGives a random response to the msg given based on the magic 8ball.\n\n'

			'`>truthordare truth/dare`\nGives a truth or dare prompts.',

			color = random.choice(randomColour)
		)

		await ctx.author.send(embed=fun_cmds)

	
	elif help_type == "games":
		
		games_cmds = discord.Embed(
			title = "Games",
			description=

			'`>rps (move)`\nPlays a game of rock paper scissors against Goose Bot.\n*>rps rock*\n\n'

			'`>roll`\nRolls a dice (1-6).\n\n'

			'`>higherlower`\nPlays a number guessing game of higher lower against Goose Bot.\n**NOT WORKING**\n\n'

			'`>coin`\nFlips a coin. Heads or Tails.\n\n'

			'**Some of the game commands are buggy and need to be re-worked. No clue why some are buggy.**',

			color = random.choice(randomColour)
		)

		await ctx.author.send(embed=games_cmds)

	elif help_type == "user":

		user_cmds = discord.Embed(
			title="User Commands",
			description=

			'`>kill @user`\nProduces a random scenario on how you killed the user you mentioned.\n\n'

			'`>slap @user`\nProduces a random scenario on how you slapped the user you mentioned.\n\n'

			'`>slap @user gif`\nProduces a slapping gif rather than a random scenario.\n\n'

			'`>throw @user`\nProduces a random object that you throw at the user you mentioned.\n\n'

			'`>hug @user`\nHugs the user you mentioned.\n\n'

			'`>avatar @user`\nRetrieves the pinged user\'s avatar and sends it back.\n\n'

			'`>harass @user`\nInsults the user you mentioned.\n\n'

			'`>highfive @user`\nAttempts to highfive a user. If they do no respond back with `>highfive @messageAuthor` within 5 seconds after you start the command, they\'ll leave you hanging. [CURRENTLY NOT WORKING]\n\n'

			'`>praise @user`\nProduces a random message that praises the user you mentioned.\n\n'

			'`>kiss @user`\nGives the user you mention a kiss.\n\n'

			'`>pat @user`\nPats the user you mentioned.\n\n'
			
			'`>info @user`\nGets information on the user you mentioned.\n\n'

			,

			color = random.choice(randomColour)
		)

		await ctx.author.send(embed=user_cmds)

	elif help_type == "mod":

		mod_cmds = discord.Embed(
			title="Moderation Commands",
			description=
			'`>kick @user reason`\nKicks a user and allows you to give a reason. **[Kick Members Required]**\n*>kick @goose.mp4#1234 yelling at people in vc*\n\n'

			'`>ban @user reason`\nBans a user and allows you to give a reason. **[Ban Members Required]**\n*>ban @goose.mp4#1234 being really stupid*\n\n'

			'`>unban userID`\nUnbans a user based on their user ID. **[Ban Members Required]**\n*>unban 1234567890123*\n\n'

			'`>afk reason`\nLets someone know you\'re afk if they ping you and changes your nickname to the reason.\n[NOT CURRENTLY WORKING]\n\n'

			'`>membercount`\nWill tell you how many members the server you used this in has.\n\n'

			'`>joinmessage`\nSets up join messages when a user joins the server.'
			
			'`>joinedit`\nAllows you to edit join messages setup for the server'

			'`>leavemessage`\nSets up leave messages when a user leaves the server'

			'`>leaveedit`\nAllows you to edit leave messages setup for the server'
			,

			color = random.choice(randomColour)
		)

		await ctx.author.send(embed=mod_cmds)

	elif help_type == "role":

		role_cmds = discord.Embed(
			title = "Role Commands",
			description = 
			"`>reactrole [channel] [message id] [emoji] [role]`",

			color = random.choice(randomColour)
		)

		await ctx.author.send(embed=role_cmds)

	elif help_type == "msg":

		msg_cmds = discord.Embed(
			title="Message Commands",
			description=
			'`>purge #`\nDeletes # amount of messages.\n*>purge 14*\n\n'

			'`>snipe`\nRetrieves the most recently deleted message.\n\n'

			'`>leetify msg`\nMakes your message you included with the command leetified. h3110.\n*>leetify hey! whats up?*\n\n'

			'`>binary msg`\nConverts your message to binary\n*>binary hello! how are you*\n\n',

			color = random.choice(randomColour)
		)

		await ctx.author.send(embed=msg_cmds)

	elif help_type == "misc":

		misc_cmds = discord.Embed(
			title="Misc Commands",
			description=

			'`>vote`\nSends a message that provides a link to top.gg so you can vote for the bot! Does nothing but the creator appreciates it!\n\n'

			'`>upcoming`\nA list of upcoming commands and features.\n\n'

			'`>donate`\nBrings up the donation page if you wanted to donate.\n\n'
			
			'`>bug *msg about bug and how to cause it*`\nAllows you to report a bug and have it logged so the developer(s) can look at it later and fix it!\n*>bug slap command not doing a random message, just keeps messaging the same response*\n\n'

			'`>invite`\nProvides a link to invite Bag Head to another server.\n\n'

			'`>suggest suggestion`\nAllows you to suggest ideas to the developer(s) of Bag Head!\n*>suggest do better coding!11 you suck!!!*\n\n'

			,

			color = random.choice(randomColour)
		)

		await ctx.author.send(embed=misc_cmds)


	else:
		await ctx.send("Hey! That's not a help category. Idiot.")
		return

# -----
keep_alive()
client.run(os.getenv('token'))