import os
import discord
import asyncio
import random
import operator
import json
import time

client = discord.Client()

class Lord_Pepe_API(discord.Client):

        def __init__(self, *args, **kwargs):
                self.http = client.http
                self.connection = client.connection
                self._resolve_destination = client._resolve_destination
                self.loop = client.loop
                self._listeners = client._listeners


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

        async def get_command_ideas(user_id, self):
                user = await client.get_user_info(user_id)
                user_dm = await client.start_private_message(user)
                await self.send_message(user_dm, '**What is your idea?**')
                message_ = await self.wait_for_message(author=user, content=None)
                m_c = message_.content
                with open('resources/ideas.txt', 'a') as ideas_file:
                        print('Command idea: {}'.format(m_c), file=ideas_file)

        async def devil(m_author, self):
                await self.join_voice_channel(m_author.voice.voice_channel)
                await self.create_ytdl_player()

        async def maths_quiz(author, channel, self):
                operators = ['/', '*', '+', '-']
                randint1 = random.randint(0, 100)
                randint2 = random.randint(0, 100)
                randoperator_str = random.choice(operators)
                if (randoperator_str == '/'):
                        ans = randint1 / randint2
                elif (randoperator_str == '*'):
                        ans = randint1 * randint2
                elif (randoperator_str == '+'):
                        ans = randint1 + randint2
                elif (randoperator_str == '-'):
                        ans = randint1 - randint2
                await client.send_message(channel, 'What is {} {} {}?'.format(randint1, randoperator_str, randint2))
                await client.wait_for_message(author=author, content=None)
                answer = int(message.content)
                if(answer == ans):
                        await client.send_message(channel, '**Ding!**')
                        ++right_answers
                else:
                        await client.send_message(channel, '**Wrong!**')

        async def maths_quiz_main(author, channel, self):
                global right_answers
                right_answers = 0
                global question_num
                question_num = 0
                random_list = [0, 1, 2, 3, 4]
                for int in random_list:
                        for_running = True
                        await self.maths_quiz(author, channel)
                        ++question_num
                while(for_running):
                        if (question_num >= 5):
                                for_running = False
                                question_num = 0

        async def terminal_to_speech(self):
                recipient_id = input('UserID>>>')
                recipient = await self.get_user_info(recipient_id)
                print('The message will be send to {}.'.format(recipient.name))
                terminal_msg = input('Message>>>')
                recipient_dm = await self.start_private_message(recipient)
                await self.send_message(recipient_dm, terminal_msg)

        async def generate_passkey(self):
        	passkey = random.randint(1, 1000000000000000)
        	return passkey

        async def help(channel, self):
                with open('resources/help.txt', 'r') as help_file:
                        help_file_read = help_file.read()
                        await self.send_message(channel, help_file_read)

        async def autism(channel, self):
                await self.send_message(channel, 'http://www.instagram.com/3than_wa15h')

        async def random_meme(channel, self):
                random_memes = ['memes/meme1.jpg', 'memes/meme2.jpeg', 'memes/meme3.jpg', 'memes/meme4.jpg', 'memes/meme5.jpeg', 'memes/meme6.jpg', 'memes/meme7.png', 'memes/meme8.jpg', 'memes/meme9.jpg', 'memes/meme10.jpg']
                await self.send_file(channel, fp=random.choice(random_memes))
                await self.send_message(channel, '**A meme a day, keeps the feminists away.**')

        async def ws_close(channel, self):
        	await client.send_message(channel, ':white_check_mark: **Websocket Close Request received.** :white_check_mark:')
        	await client.send_message(channel, '**Goodbye cruel world!** :middle_finger:')
        	await client.logout()

        async def clear(m_author, chan, self):
                await self.send_message(chan, '**Are you completely sure that you want to clear this chat?**')
                aa = await self.wait_for_message(author=m_author, content=None)
                if (aa.content == 'yes'):
                        cll = await self.purge_from(chan,
                                         limit = 1000,
                                         check = None)
                time.sleep(1)
                rr = await self.send_message(chan, '**{} messages have been cleared.**'.format(len(cll)))
                time.sleep(2)
                await self.delete_message(rr)
                if (aa.content == 'no'):
                        await self.send_message(chan, 'Ok. I will **not** clear.')

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

class CLI:

        def __init__(self):
                pass

        async def cli_main(self):
                print('PEPE CLI VERSION 1.0.0')
                comm = input('>>>')
                if (comm == 'dm'):
                        await Lord_Pepe_API.terminal_to_speech(Lord_Pepe_API(discord.Client))
                        await self.cli_main(self)
                else:
                        print('Unknown command.')
                        await self.cli_main(self)

class Lord_Pepe:

        global SECRETS
        SECRETS = json.load(open('resources/SECRETS.json'))

        @client.event
        async def on_ready():
            print('Our lord and savior is online.')
            passkeyy = await Lord_Pepe_API(discord.Client).generate_passkey()
            global passkeyy_
            passkeyy_ = str(passkeyy)
            print(passkeyy_)


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

                if message.content.lower().startswith('$idea'):
                        await Lord_Pepe_API.get_command_ideas(message.author.id, Lord_Pepe_API(discord.Client))

                if message.content.lower().startswith('$play'):
                        yt_url = message.content[6:]
                        channel = message.author.voice.voice_channel
                        voice = await client.join_voice_channel(channel)
                        yt_dl_player = await voice.create_ytdl_player(yt_url, before_options=" -reconnect 1 -reconnect_streamed 1" " -reconnect_delay_max 5")
                        yt_dl_player.start()

                if message.content.lower().startswith('$maths'):
                        await Lord_Pepe_API.maths_quiz_main(message.author, message.channel, Lord_Pepe_API(discord.Client))

                if message.content.lower().startswith('$clear'):
                        m_author = message.author
                        chan = message.channel
                        await Lord_Pepe_API.clear(m_author, chan, Lord_Pepe_API(discord.Client))

                if message.content.lower().startswith('$autism'):
                    await Lord_Pepe_API.autism(Lord_Pepe_API(discord.Client))

                if message.content.startswith(passkeyy_):
                	await Lord_Pepe_API.ws_close(message.channel, Lord_Pepe_API)

        client.run(SECRETS["token"])
