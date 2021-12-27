import discord
from discord.ext import commands
import json

randomColour= [0xFF0000,0x0000FF,0x008000,0xFFFF00,0xFFA500,0x800080,0xFFC0CB,0x000000,0x964B00,0xFFFFFF, 0xFF00FF, 0x00FFFF, 0x32CD32, 0x808080, 0x89CFF0, 0x800000, 0xFDFD96, 0x77dd77, 0xff6961, 0xC3B1E1]

client = discord.Client()

class Role(commands.Cog):

	def __init__(self, client):
		self.client = client


	@commands.Cog.listener()
	async def on_raw_reaction_add(self, payload):
		"""Detects reactions for react-role"""

		if payload.member.bot is True:
			pass
		
		else:
			with open('docs/json/reactrole.json') as rrFile:
				dataStuff = json.load(rrFile)
				for x in dataStuff:
					if x['emoji'] == str(payload.emoji) and x['messageID'] == str(payload.message_id):
	
						role = discord.utils.get(self.client.get_guild(payload.guild_id).roles, id = x['roleID'])

						await payload.member.add_roles(role)
				
				rrFile.close()


		

	@commands.Cog.listener()
	async def on_raw_reaction_remove(self, payload):
		"""Removes role if user removes reaction"""

		with open('docs/json/reactrole.json') as rrFile:
			dataStuff = json.load(rrFile)
			for x in dataStuff:
				if x['emoji'] == str(payload.emoji) and x['messageID'] == str(payload.message_id):

					role = discord.utils.get(self.client.get_guild(payload.guild_id).roles, id = x['roleID'])

					await self.client.get_guild(payload.guild_id).get_member(payload.user_id).remove_roles(role)
			
			rrFile.close()



	@commands.command(pass_context=True, aliases = ["rr", "reactionrole"])
	@commands.has_permissions(administrator=True)
	async def reactrole(self, ctx, channel, msgID, emoji, role: discord.Role):
		"""React role"""
		
		channelid = ""
		for i in channel:
			try:
				i = int(i)
				i = str(i)
				channelid += i

			except ValueError or TypeError:
				pass

		await self.client.wait_until_ready()
		channel = self.client.get_channel(int(channelid))
		message = await channel.fetch_message(msgID)
		await message.add_reaction(emoji)

		with open("docs/json/reactrole.json") as jfile:
			data = json.load(jfile)

			new_reactrole = {
				'roleName':role.name,
				'roleID':role.id,
				'emoji':emoji,
				'messageID':msgID
			}

			data.append(new_reactrole)

			jfile.close()
		
		with open("docs/json/reactrole.json", "w") as f:
			json.dump(data, f, indent=4)
			f.close()
		
		await ctx.reply("<a:check:871550585197969519> **Reaction role successfully added!**", mention_author=False)


def setup(client):
	client.add_cog(Role(client))