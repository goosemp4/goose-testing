import discord, random, os
from discord.ext import commands
from random import randint

randomColour= [0xFF0000,0x0000FF,0x008000,0xFFFF00,0xFFA500,0x800080,0xFFC0CB,0x000000,0x964B00,0xFFFFFF, 0xFF00FF, 0x00FFFF, 0x32CD32, 0x808080, 0x89CFF0, 0x800000, 0xFDFD96, 0x77dd77, 0xff6961, 0xC3B1E1]

client = discord.Client()

class Triggers(commands.Cog):

	def __init__(self, client):
		self.client = client


	@commands.Cog.listener()
	async def on_message(self, message):
		"""Bag Head has a chance to send any of these messages depending on what a user say."""

		pull_the_trigger = randint(1,5) # 1 in 5 chance of actually activating the response when a user says something
		msg = message.content

		if pull_the_trigger == 1:

			# if user says 'desu vult', send funny crusade image kekw
			if msg.lower() == "deus vult":
				file_dir = "docs/images/WE WILL TAKE JERUSALEM.jpg"

				file = discord.File(file_dir, filename="deusvult.jpg")

				embed = discord.Embed(
					title="DEUS VULT, INFIDEL! TO THE HOLY CRUSADE!"
				)
				embed.set_image(
					url="attachment://deusvult.jpg"
				)

				await message.channel.send(file=file, embed=embed, delete_after=10)


			elif msg.lower() == "sex":
				await message.channel.send("Sex?! The only 6 inches should be the 6 inches for the holy sprit.")


			elif msg.lower() == "uwu" or msg.lower() == "owo" or msg.lower() == ":3":
				await message.channel.send(f"shut the fuck up. \"{msg}\", shut up.")


			elif msg.lower() == "faggot" or msg.lower() == "fag" or msg.lower() == "nigger" or msg.lower() == "retard":
				await message.channel.send(f"woah we got a cool kid! he uses the word {msg}!")


			elif msg.lower() == "ily":
				await message.channel.reply("omg i love you too!1!!!1")


			elif msg.lower() == "ily2":
				await message.channel.send(f"no, **I** love you too. Not {message.author.display_name}")


			elif msg.lower() == "shutup":
				await message.channel.send("no you shutup idiot.")
			
			elif msg.lower() == "bag":
				await message.channel.send("head")




def setup(client):
	client.add_cog(Triggers(client))