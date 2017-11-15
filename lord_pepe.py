import os
import discord
import asyncio
import random

client = discord.Client()

class Lord_Pepe_API(discord.Client):
	def __init__(self, *args, **kwargs):
		self.http = client.http
		self.connection = client.connection
		self._resolve_destination = client._resolve_destination

	async def meme(memeIMG, channel, self):
		await self.send_file(channel, fp=memeIMG)
		await self.send_message(channel, 'Meme is served.')

	async def commandment(channel, self):
		commandments = ['1. Always be memeulous.', '2. Never mention 21 or what are those. These are classified as **__DEAD__** memes.', '3. Swear obedience to the dankest, the coolest, the hippest: Lord Pepe.', '4. Your mum is gay.', '5. If you see a feminist, slaughter them.']
		await self.send_message(channel, random.choice(commandments))

	async def get_follower(id, self):
		follower = await client.get_user_info(id)
		return follower

	async def add_follower(channel, ma_id, self):
		follower_added = await client.get_user_info(ma_id)
		follower_name = follower_added.name
		with open('resources/followers.txt', 'a') as followers:
			print(follower_name, file=followers)
		await self.send_message(channel, '**You have been registered as a follower of Memeism.**')

	async def return_all_followers(channel, self):
		with open('resources/followers.txt', 'r') as followers:
			all_followers = followers.read()
		await self.send_message(channel, '**Here are all the current followers of memeism:**')
		await self.send_message(channel, "```{}```".format(all_followers))

	async def check_if_registered(self):

	async def random_meme(channel, self):
		random_memes = ['memes/meme1.jpg', 'memes/meme2.jpeg', 'memes/meme3.jpg', 'memes/meme4.jpg', 'memes/meme5.jpeg', 'memes/meme6.jpg', 'memes/meme7.png', 'memes/meme8.jpg', 'memes/meme9.jpg', 'memes/meme10.jpg']
		await self.send_file(channel, fp=random.choice(random_memes))
		await self.send_message(channel, '**A meme a day, keeps the feminists away.**')

	async def memeism_info(channel, self):
		with open ('resources/info.txt', 'r') as info:
			info_ = info.read()
			await self.send_message(channel, "```{}```".format(info_))

	async def get_memeism_server(self):
		memeism_server = 'https://discord.gg/nkmSpS5'
		return memeism_server

	async def return_memeism_server(channel, self):
		memeism_server_get_method = await self.get_memeism_server(self)
		await self.send_message(channel, memeism_server_get_method)




class Lord_Pepe:

	@client.event
	async def on_ready():
		print('Our lord and savior is online.')

	@client.event
	async def on_message(message):

		if message.content.lower().startswith('$meme'):
			meme = message.content[6:]
			if meme == '1':
				memeIMG = 'memes/meme1.jpg'
			if meme == '2':
				memeIMG = 'memes/meme2.jpeg'
			if meme == '3':
				memeIMG = 'memes/meme3.jpg'
			if meme == '4':
				memeIMG = 'memes/meme4.jpg'
			if meme == '5':
				memeIMG = 'memes/meme5.jpeg'
			if meme == '6':
				memeIMG = 'memes/meme6.jpg'
			if meme == '7':
				memeIMG = 'memes/meme7.png'
			if meme == '8':
				memeIMG = 'memes/meme8.jpg'
			if meme == '9':
				memeIMG = 'memes/meme9.jpg'
			if meme == '10':
				memeIMG = 'memes/meme10.jpg'

			await Lord_Pepe_API.meme(memeIMG, message.channel, Lord_Pepe_API(discord.Client))

		if message.content.lower().startswith('$randmeme'):
			await Lord_Pepe_API.random_meme(message.channel, Lord_Pepe_API(discord.Client))

		if message.content.lower().startswith('$info'):
			await Lord_Pepe_API.memeism_info(message.channel, Lord_Pepe_API(discord.Client))

		if message.content.lower().startswith('$register'):
			ma_id = message.author.id
			await Lord_Pepe_API.add_follower(message.channel, ma_id, Lord_Pepe_API(discord.Client))

		if message.content.lower().startswith('$all_followers'):
			await Lord_Pepe_API.return_all_followers(message.channel, Lord_Pepe_API(discord.Client))

	client.run('MzgwMDk1NTQ5MTQ5NTQ0NDQ5.DOznMw.DVgUja8gKLD0t49hAUB7EoWJfCY')