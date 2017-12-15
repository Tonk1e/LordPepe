import discord
import asyncio
import random
import json
import time
import aiohttp

client = discord.Client()

class Lord_Pepe_API(discord.Client):

        DANK_POINTS_FILE = open('resources/dank_points.json')
        DANK_POINTS = json.load(DANK_POINTS_FILE)
        ADMINS_FILE = open('resources/admins.json')
        ADMINS = json.load(ADMINS_FILE)
        BANNED_PLAYERS_FILE = open('resources/banned.json')
        BANNED_PLAYERS = json.load(BANNED_PLAYERS_FILE)
        SECRETS = json.load(open('resources/SECRETS.json'))


        def __init__(self):
                self.http = client.http
                self.connection = client.connection
                self._resolve_destination = client._resolve_destination
                self.loop = client.loop
                self._listeners = client._listeners

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
                        print('Command idea: {}'.format(m_c))

        async def devil(channel, content, m_author, self):
                voice = await self.join_voice_channel(channel)
                await voice.create_ytdl_player()

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
                        right_answers = right_answers + 1
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
                        question_num = question_num + 1
                        print(int)
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


        async def register_forDankPoints(user_name, user_id, message_channel_id, self):
            if not ("{}/{}".format(user_name, user_id) in DANK_POINTS):
                DANK_POINTS["{}/{}".format(user_name, user_id)] = 0
                DANK_POINTS["REGISTERED_USERS"] = DANK_POINTS["REGISTERED_USERS"] + 1
                with open ('resources/dank_points.json', 'w') as DANKK_POINTS_FILE:
                    json.dump(DANK_POINTS, DANKK_POINTS_FILE)
                await client.send_message(discord.Object(message_channel_id), '**You have been registered for dank points. Yay.**')
            else:
                await client.send_message(discord.Object(message_channel_id), '**You already have an account you retard.**')


        async def add_dankPoints(user, self):
            if ("{}/{}".format(user.name, user.id) in DANK_POINTS):
                DANK_POINTS["{}/{}".format(user_name, user_id)] = DANK_POINTS["{}/{}".format(user.name, user.id)] + rand.randint(1, 100)

        async def dank_quiz(m_author, channel, self):
            if ("{}/{}".format(m_author.name, m_author.id in DANK_POINTS)):
                questions = ["**Is 21 a good meme?**", "**Should Jake Paul die in a hole?**", "**Are transgenders real?**", "**Was 9/11 a social experiment?**"]
                rand_question = random.choice(questions)
                await client.send_message(channel, rand_question)
                if (rand_question == questions[0]):
                    ans = await client.wait_for_message(author=m_author)
                    if (ans.content.lower() == 'no'):
                        await client.send_message(channel, "**Ding ding!**")
                        amount_of_points = random.randint(1, 15)
                        await client.send_message(channel, f"**You have been awarded {amount_of_points} Dank Points!**")
                        DANK_POINTS["{}/{}".format(m_author.name, m_author.id)] = DANK_POINTS["{}/{}".format(m_author.name, m_author.id)] + amount_of_points

                    else:
                        await client.send_message(channel, "**You got it wrong you pleb.**")
                        await client.send_message(channel, "**You got no Dank Points.**")

                if (rand_question == questions[1]):
                    ans = await client.wait_for_message(author=m_author)
                    if (ans.content.lower() == 'yes'):
                        await client.send_message(channel, "**Ding ding!**")
                        amount_of_points = random.randint(1, 15)
                        await client.send_message(channel, f"**You have been awarded {amount_of_points} Dank Points!**")
                        DANK_POINTS["{}/{}".format(m_author.name, m_author.id)] = DANK_POINTS["{}/{}".format(m_author.name, m_author.id)] + amount_of_points
                        with open ('resources/dank_points.json', 'w') as DANKK_POINTS_FILE:
                            json.dump(DANK_POINTS, DANKK_POINTS_FILE)
                    else:
                        await client.send_message(channel, "**You got it wrong you pleb.**")
                        await client.send_message(channel, "**You got no Dank Points.**")

                if (rand_question == questions[2]):
                    ans = await client.wait_for_message(author=m_author)
                    if (ans.content.lower() == 'no'):
                        await client.send_message(channel, "**Ding ding!**")
                        amount_of_points = random.randint(1, 15)
                        await client.send_message(channel, f"**You have been awarded {amount_of_points} Dank Points!**")
                        DANK_POINTS["{}/{}".format(m_author.name, m_author.id)] = DANK_POINTS["{}/{}".format(m_author.name, m_author.id)] + amount_of_points
                        with open ('resources/dank_points.json', 'w') as DANKK_POINTS_FILE:
                            json.dump(DANK_POINTS, DANKK_POINTS_FILE)
                    else:
                        await client.send_message(channel, "**You got it wrong you pleb.**")
                        await client.send_message(channel, "**You got no Dank Points.**")

                if (rand_question == questions[3]):
                    ans = await client.wait_for_message(author=m_author)
                    if (ans.content.lower() == 'yes'):
                        await client.send_message(channel, "**Ding ding!**")
                        amount_of_points = random.randint(1, 15)
                        await client.send_message(channel, f"**You have been awarded {amount_of_points} Dank Points!**")
                        DANK_POINTS["{}/{}".format(m_author.name, m_author.id)] = DANK_POINTS["{}/{}".format(m_author.name, m_author.id)] + amount_of_points
                        with open ('resources/dank_points.json', 'w') as DANKK_POINTS_FILE:
                            json.dump(DANK_POINTS, DANKK_POINTS_FILE)
                    else:
                        await client.send_message(channel, "**You got it wrong you pleb.**")
                        await client.send_message(channel, "**You got no Dank Points.**")
            else:
                await client.send_message(channel, '**You do not have a Dank Points account.**')
                await client.send_message(channel, "**Please create one with** `$d-register`.")

        async def dank_balance(channel, m_author, self):
            if (f"{m_author.name}/{m_author.id}" in DANK_POINTS):
                balance = DANK_POINTS[f"{m_author.name}/{m_author.id}"]
                em = discord.Embed()
                em.title = f"{m_author.name}'s Dank Points Account"
                if (balance == 1):
                    em.add_field(name="Balance:", value=f"{balance} Dank Point.")
                    await client.send_message(channel, embed=em)
                else:
                    em.add_field(name="Balance:", value=f"{balance} Dank Points.")
                    await client.send_message(channel, embed=em)
            else:
                await client.send_message(channel, "**You do not have a Dank Points account**")
                await client.send_message(channel, "**Please create one with** `$d-register`.")

        async def dank_donate(donation_amount, donate_recipient, channel, m_author, self):
            if (f"{m_author.name}/{m_author.id}" in DANK_POINTS):
                balance1 = DANK_POINTS[f"{m_author.name}/{m_author.id}"]
                balance2 = DANK_POINTS[f"{donate_recipient.name}/{donate_recipient.id}"]
                if (balance1 - donation_amount > 0):
                    DANK_POINTS[f"{m_author.name}/{m_author.id}"] = DANK_POINTS[f"{m_author.name}/{m_author.id}"] - donation_amount
                    DANK_POINTS[f"{donate_recipient.name}/{donate_recipient.id}"] = DANK_POINTS[f"{donate_recipient.name}/{donate_recipient.id}"] + donation_amount
                    with open ('resources/dank_points.json', 'w') as DANKK_POINTS_FILE:
                        json.dump(DANK_POINTS, DANKK_POINTS_FILE)
                    await client.send_message(channel, f"**{donation_amount} Dank Points were transferred from {m_author.name}'s account to {donate_recipient.name}'s account.**")
                    await self.dank_balance(channel, donate_recipient, self)
                else:
                    await client.send_message(channel, "**You do not have sufficient funds to complete this action.**")
            else:
                await client.send_message(channel, "**You do not have a Dank Points account**")
                await client.send_message(channel, "**Please create one with** `$d-register`.")

        async def dank_shop(channel, m_author, self):
            if (f"{m_author.name}/{m_author.id}" in DANK_POINTS):
                shop = discord.Embed()
                shop.title = "Dank Shop:"
                shop.add_field(name="1. Admin:", value="Grants you admin permissions. Price: 10, 000 DP.")
                await client.send_message(channel, embed=shop)
                await client.send_message(channel, "**Please enter the number of dat ting you wanna buy.**")
                bought_number = await client.wait_for_message(author=m_author)
                if (bought_number.content == '1'):
                    balance = DANK_POINTS[f"{m_author.name}/{m_author.id}"]
                    if (balance >= 10000):
                        ADMINS[f"{m_author.id}"] = "true"
                        balance = balance - 10000
                        with open ('resources/admins.json', 'w') as admins_file:
                            json.dump(ADMINS, admins_file)
                        with open ('resources/dank_points.json', 'w') as dank_points_file:
                            json.dump(DANK_POINTS, dank_points_file)
                    else:
                        await client.send_message(channel, "**You do not have sufficient funds to complete this action.**")

        async def get_youtube_url(search, self):
                GOOGLE_API_KEY = SECRETS["GOOGLE_API_KEY"]
                url = "https://www.googleapis.com/youtube/v3/search"
                with aiohttp.ClientSession() as session:
                        async with session.get(url, params={"type" : "video",
                                                      "q" : search,
                                                      "part" : "snippet",
                                                      "key" : GOOGLE_API_KEY}) as resp:
                                data = await resp.json()

                if data["items"]:
                        video = data["items"][0]
                        response = "https://youtu.be/" + video["id"]["videoId"]
                        print(response)
                else:
                        response = NOT_FOUND
                return response

        async def generate_passkey(self):
                passkey = random.randint(1, 1000000000000000)
                return passkey

        async def autism(channel, self):
                await self.send_message(channel, 'http://www.instagram.com/3than_wa15h')

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

        async def help(channel, self):
                with open('resources/help.txt', 'r') as help_file:
                        help_file_read = help_file.read()
                        await self.send_message(channel, help_file_read)


        async def random_meme(channel, self):
                random_memes = ['memes/meme1.jpg', 'memes/meme2.jpeg', 'memes/meme3.jpg', 'memes/meme4.jpg', 'memes/meme5.jpeg', 'memes/meme6.jpg', 'memes/meme7.png', 'memes/meme8.jpg', 'memes/meme9.jpg', 'memes/meme10.jpg']
                await self.send_file(channel, fp=random.choice(random_memes))
                await self.send_message(channel, '**A meme a day, keeps the feminists away.**')

        async def ws_close(channel, self):
                await client.send_message(channel, ':white_check_mark: **Websocket Close Request received.** :white_check_mark:')
                await client.send_message(channel, '**Goodbye cruel world!** :middle_finger:')
                await client.logout()

        async def send_bully_message(victim, channel, self):
                bully_messages = ["**{} has AIDS.**".format(victim.name), "**{}'s Dad is 44.**".format(victim.name), "**Brush your teeth {}.**".format(victim.name)]
                await client.send_message(channel, random.choice(bully_messages))

        async def clear(m_author, chan, self):
                await self.send_message(chan, '**Are you completely sure that you want to clear this chat?**')
                aa = await self.wait_for_message(author=m_author, content=None)
                if (aa.content == 'yes'):
                        cll = await self.purge_from(chan,
                                        limit = 1000,
                                        check = None)
                time.sleep(1)
                rr = await self.send_message(channel, '**{} messages have been cleared.**'.format(len(cll)))
                time.sleep(2)
                await self.delete_message(rr)
                if (aa.content == 'no'):
                        await self.send_message(chan, 'Ok. I will **not** clear.')

        async def memeism_info(channel, self):
                with open ('resources/info.txt', 'r') as info:
                        info_ = info.read()
                        await self.send_message(channel, "```{}```".format(info_))

        async def return_memeism_server(channel, self):
                memeism_server_get_method = await self.get_memeism_server(self)
                await client.send_message(channel, memeism_server_get_method)

        async def bully_Rickbot(channel, self):
                Rickbot_bully_messages = ['**Rickbot is a piece of shit.**', '**At least make Rickbot work.**', '**Where did you make Rickbot? The toilet store?**', '**Why does Rickbot exist?**', '**Just kill him.**', "**He's terrible.**"]
                times = [0, 1, 2, 3, 4, 5]
                for integer in times:
                        await client.send_message(channel, Rickbot_bully_messages[integer])
                        time.sleep(1)

        async def banUser(user, self):
            user_dm = await client.start_private_message(user)
            await client.send_message(user_dm, "**Well done. You've been banned you prick.**")
            BANNED_PLAYERS[user.id] = "banned"
            with open('resources/banned.json', 'w') as banned_players_file:
                json.dump(BANNED_PLAYERS, banned_players_file)

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

class Lord_Pepe_Game_API(discord.Client):

    def __init__(self):
        global card1
        card1 = json.load(open('resources/cards/card1.json'))
        global card2
        card2 = json.load(open('resources/cards/card2..json'))
        global cards
        cards = [card1.read(), card2.read()]
    
    async def gameChecker(amount, self):
        checking = True
        while(checking):
            if(amount > 1):
                game = True
                return game
                checking = False

    async def getCardInfo(players, cards, self):
        for player in players:
            CURRENT_PLAYERS = json.load(open('resources/currentPlayers.json'))
            CURRENT_PLAYERS[f"{player}"] = random.choice(cards)
            return CURRENT_PLAYERS[f"{player}"]

    async def returnAllPlayersCards(channel, players, cards, self):
        for player in players:
            thing = await self.getCardInfo(players, cards, self)
            user = await client.get_user_info(f"{player}")
            await client.send_message(channel, "```{user.name} : {thing}```")

    async def playerDeath(players, player, channel, card, self):
        await client.send_message(channel, f"```{player.name} has died while using the card {card}!```")
        CURRENT_PLAYERS[f"{player}"] = False
        players = players - 1
        if (players <= 1):
            await client.send_message

    async def getMove(_int, card, self):
        if (card == card1 and _int == 1):
            move = "```You flailed around your arms like a retard! It had no effect!```"
            return move
        if (card == card1 and _int == 2):
            move = "```You flailed around your legs like a retard! It had no effect!```"
            return move
        if (card == card1 and _int == 3):
            card1["hp"] = 0
            move = "```You hit yourself in the face! You died!``` ```HP : {}".format(card1["hp"])
            return move

    async def executeMove(player, _int, card, channel, self):
        move = await self.getMove(_int, card, self)
        await client.send_message(channel, move)
        if (move == "```You flailed around your arms like a retard! It had no effect!```"):
            pass
        elif(move == "```You flailed around your legs like a retard! It had no effect!```"):
            pass
        elif(move == "```You hit yourself in the face! You died!``` ```HP : {}".format(card1["hp"])):
            self.playerDeath(player, channel, card, self)

class Lord_Pepe:

        global SECRETS
        SECRETS = json.load(open('resources/SECRETS.json'))
        global GOOGLE_API_KEY
        GOOGLE_API_KEY = SECRETS["GOOGLE_API_KEY"]

        @client.event
        async def on_ready():
            print('Our lord and savior is online.')
            passkeyy = await Lord_Pepe_API.generate_passkey(Lord_Pepe_API)
            global passkeyy_
            passkeyy_ = str(passkeyy)
            print(passkeyy_)

        @client.event
        async def on_message(message):

                global players
                players = {}

                if (message.content.lower().startswith('$meme') and not message.author.id in BANNED_PLAYERS):
                    meme = message.content[6:]
                    if meme == '1':
                            memeIMG = 'memes/meme1.jpg'
                            await Lord_Pepe_API.meme(memeIMG, message.channel, Lord_Pepe_API(discord.Client))
                    elif meme == '2':
                            memeIMG = 'memes/meme2.jpeg'
                            await Lord_Pepe_API.meme(memeIMG, message.channel, Lord_Pepe_API(discord.Client))
                    elif meme == '3':
                            memeIMG = 'memes/meme3.jpg'
                            await Lord_Pepe_API.meme(memeIMG, message.channel, Lord_Pepe_API(discord.Client))
                    elif meme == '4':
                            memeIMG = 'memes/meme4.jpg'
                            await Lord_Pepe_API.meme(memeIMG, message.channel, Lord_Pepe_API(discord.Client))
                    elif meme == '5':
                            memeIMG = 'memes/meme5.jpeg'
                            await Lord_Pepe_API.meme(memeIMG, message.channel, Lord_Pepe_API(discord.Client))
                    elif meme == '6':
                            memeIMG = 'memes/meme6.jpg'
                            await Lord_Pepe_API.meme(memeIMG, message.channel, Lord_Pepe_API(discord.Client))
                    elif meme == '7':
                            memeIMG = 'memes/meme7.png'
                            await Lord_Pepe_API.meme(memeIMG, message.channel, Lord_Pepe_API(discord.Client))
                    elif meme == '8':
                            memeIMG = 'memes/meme8.jpg'
                            await Lord_Pepe_API.meme(memeIMG, message.channel, Lord_Pepe_API(discord.Client))
                    elif meme == '9':
                            memeIMG = 'memes/meme9.jpg'
                            await Lord_Pepe_API.meme(memeIMG, message.channel, Lord_Pepe_API(discord.Client))
                    elif meme == '10':
                            memeIMG = 'memes/meme10.jpg'
                            await Lord_Pepe_API.meme(memeIMG, message.channel, Lord_Pepe_API(discord.Client))

                    elif meme == None:
                        await client.send_message(message.channel, "**You didn't specify a meme you pleb.**")

                    else:
                        await client.send_message(message.channel, "**An error ocurred. It's your fault you pleb.**")

                if (message.content.lower() == '$randmeme' and not message.author.id in BANNED_PLAYERS):
                        await Lord_Pepe_API.random_meme(message.channel, Lord_Pepe_API(discord.Client))

                if message.content.lower().startswith('$info') and not message.author.id in BANNED_PLAYERS:
                        await Lord_Pepe_API.memeism_info(message.channel, Lord_Pepe_API(discord.Client))

                if message.content.lower().startswith('$register') and not message.author.id in BANNED_PLAYERS:
                        ma_id = message.author.id
                        await Lord_Pepe_API.add_follower(message.channel, ma_id, Lord_Pepe_API(discord.Client))

                if message.content.lower().startswith('$all_followers') and not message.author.id in BANNED_PLAYERS:
                        await Lord_Pepe_API.return_all_followers(message.channel, Lord_Pepe_API(discord.Client))

                if message.content.lower().startswith('$idea') and not message.author.id in BANNED_PLAYERS:
                        await Lord_Pepe_API.get_command_ideas(message.author.id, Lord_Pepe_API(discord.Client))

                if message.content.lower().startswith('$play') and not message.author.id in BANNED_PLAYERS:
                    if not (client.is_voice_connected(message.server)):
                        global voice
                        voice = await client.join_voice_channel(message.author.voice.voice_channel)
                        search = message.content[6:]
                        yt_url = await Lord_Pepe_API.get_youtube_url(search, Lord_Pepe_API)
                        YTDL_OPTS = {'format': 'webm[abr>0]/bestaudio/best',}
                        global player
                        player = await voice.create_ytdl_player(yt_url, options=YTDL_OPTS)
                        player.start()
                        await client.send_message(message.channel, "**Brace your ears. It's playing.**")
                    elif (client.is_voice_connected(message.server)):
                        player.stop()
                        print('Stopped previous stream.')
                        search = message.content[6:]
                        yt_url = await Lord_Pepe_API.get_youtube_url(search, Lord_Pepe_API)
                        YTDL_OPTS = {'format': 'webm[abr>0]/bestaudio/best',}
                        player = await voice.create_ytdl_player(yt_url, options=YTDL_OPTS)
                        player.start()
                        await client.send_message(message.channel, "**Brace your ears. It's playing.**")

                if message.content.lower().startswith('$quit'):
                    voice_client = client.voice_client_in(message.server)
                    voice.disconnect()

                if message.content.lower().startswith('$quit') and not message.author.id in BANNED_PLAYERS:
                    voice = client.voice_client_in(message.server)
                    voice.disconnect()


                if message.content.lower().startswith('$maths') and not message.author.id in BANNED_PLAYERS:
                        await Lord_Pepe_API.maths_quiz_main(message.author, message.channel, Lord_Pepe_API(discord.Client))

                if message.content.lower().startswith('$clear') and not message.author.id in BANNED_PLAYERS:
                        m_author = message.author
                        chan = message.channel
                        await Lord_Pepe_API.clear(m_author, chan, Lord_Pepe_API(discord.Client))

                if message.content.lower().startswith('$autism') and not message.author.id in BANNED_PLAYERS:
                    await Lord_Pepe_API.autism(message.channel, Lord_Pepe_API(discord.Client))

                if message.content.startswith(passkeyy_) and not message.author.id == '380095549149544449':
                        await Lord_Pepe_API.ws_close(message.channel, Lord_Pepe_API)

                if message.content.startswith('$bullyme') and not message.author.id in BANNED_PLAYERS:
                    await Lord_Pepe_API.send_bully_message(message.author, message.channel, Lord_Pepe_API)

                if (message.content.lower() == '$memeism') and not message.author.id in BANNED_PLAYERS:
                    await Lord_Pepe_API.return_memeism_server(message.channel, Lord_Pepe_API)

                if message.content.startswith('$rickbot') and not message.author.id in BANNED_PLAYERS:
                    await Lord_Pepe_API.bully_Rickbot(discord.Object('378954661648007168'), Lord_Pepe_API)

                if message.content.startswith('$d-register') and not message.author.id in BANNED_PLAYERS:
                    await Lord_Pepe_API.register_forDankPoints(message.author.name, message.author.id, message.channel.id, Lord_Pepe_API)

                if message.content.startswith('$d-quiz') and not message.author.id in BANNED_PLAYERS:
                    await Lord_Pepe_API.dank_quiz(message.author, message.channel, Lord_Pepe_API)

                if message.content.startswith('$d-balance') and not message.author.id in BANNED_PLAYERS:
                    await Lord_Pepe_API.dank_balance(message.channel, message.author, Lord_Pepe_API)

                if message.content.startswith('$d-donate') and not message.author.id in BANNED_PLAYERS:
                    donation_amount_str = message.content[10:]
                    donation_amount = int(donation_amount_str)
                    await client.send_message(message.channel, "**Please provide the ID of the user.**")
                    get_user = await client.wait_for_message(author=message.author)
                    user_id = get_user.content
                    user = await client.get_user_info(user_id)
                    await Lord_Pepe_API.dank_donate(donation_amount, user, message.channel, message.author, Lord_Pepe_API)

                if message.content.startswith('$d-shop') and not message.author.id in BANNED_PLAYERS:
                    await Lord_Pepe_API.dank_shop(message.channel, message.author, Lord_Pepe_API)

                if message.content.startswith('$yt'):
                    search = message.content[4:]
                    response = await Lord_Pepe_API.get_youtube_url(search, Lord_Pepe_API)
                    await client.send_message(message.channel, response)

                if message.content.startswith('$yt') and not message.author.id in BANNED_PLAYERS:
                    search = message.content[4:]
                    url = await Lord_Pepe_API.get_youtube_url(search, Lord_Pepe_API)
                    await client.send_message(message.channel, url)

                if message.content.startswith('$ban') and message.author.id == '292556142952054794':
                    await client.send_message(message.channel, "**Please the specify the ID of the user.**")
                    global ID_message
                    ID_message = await client.wait_for_message(author=message.author)
                    if (ID_message.content == None):
                        await client.send_message(message.channel, "**Specify a god damn user then.**")
                    else:
                        banned_user = await client.get_user_info(ID_message.content)
                        await Lord_Pepe_API.banUser(banned_user, Lord_Pepe_API)
                        await client.send_message(message.channel, "**It has been dealt with.**")

                if message.content.startswith('$g-start'):
                    amount = 0
                    await client.send_message(message.channel, f"**You have started a game, {message.author.name}.")
                    time.sleep(0.5)
                    await client.send_message(message.channel, "**Please type 'me plz' into the chat if you would like to join the game!**")
                    checkingAmount = True
                    while(checkingAmount):
                        wait_for_players = await client.wait_for_message(channel=message.channel)
                        if(wait_for_players.content.lower() == "me plz"):
                            await client.send_message(message.channel, f"```{wait_for_players.author.name} has joined the game!")
                        if(wait_for_players.content.lower() == "start" and wait_for_players.author == message.author):
                            amount = amount + 1
                            checker = await Lord_Pepe_Game_API.gameChecker(amount, Lord_Pepe_Game_API)
                            if(checker):
                                pass


        client.run(SECRETS["token"])
