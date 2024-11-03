import discord
import random
import re
import os
import asyncio

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

funny_responses = [
    "Uhhh… wait, I didn’t get that...",
    "Hold on… let me think…",
    "Mmm… can you make it easier? My brain hurts...",
    "Maybe yes? But also… maybe no.",
    "This is, like, a hard one... you sure you wanna know?",
    "Well, obviously it’s… actually, I’m lost.",
    "Why do you even ask that? Weird question, huh?",
    "Is this a trick question?",
    "Oh, wait, wait, I think I’m stuck…",
    "Uh, let me consult my magic 8-ball... it's saying 'Ask again later.'"
]

# New reactions to "gm" and "gn"
morning_responses = [
    "Good morning! Are we there yet? Gm gm gm gm gm!",
    "Mornin’! Why are you awake so early?",
    "Rise and shine! I think I need more coffee...",
    "Put your gm in my piss jar!",
    "Good morning! Did you bring me breakfast?"
]

night_responses = [
    "Good night! Sleep tight, don’t let the bed bugs bite!",
    "Nighty night! Dream about food...!",
    "Sweet dreams! Don’t forget to count sheep... gngngngngngngn!",
    "Put your gn in my piss jar!",
    "Good night! If you hear strange noises, it's just me thinking about life."
]

random_messages = [
    "I don't care.",
    "Okay, I’m off to take a shit.",
    "Hahaha!",
    "I love you mate",
    "Fuck off!!",
    "What even is life?",
]

def generate_funny_response(question):
    if random.random() < 0.3:
        return random.choice(funny_responses)
    elif "how" in question.lower():
        return random.choice([
            "Well… somehow, I guess.",
            "I'm doing as well as a bot can!",
            "Uhh... I'm fine? I think?",
            "You know, just hanging out in the cloud!"
        ])
    elif "why" in question.lower():
        return "Because… uh… it just happened like that!"
    elif "what" in question.lower():
        return "Ah, that’s, like… you know… yeah, that."
    elif "where" in question.lower():
        return "Somewhere out there, I think."
    else:
        return "Hmm… tough question… not sure I got an answer."

async def send_random_messages(channel):
    while True:
        await asyncio.sleep(random.randint(300, 600))  # Wait for a random interval (5 to 10 minutes)
        message = random.choice(random_messages)
        await channel.send(message)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if re.search(r'\?$', message.content):
        response = generate_funny_response(message.content)
        await message.channel.send(response)

    if message.content.lower() in ["gm", "good morning"]:
        response = random.choice(morning_responses)
        await message.channel.send(response)

    if message.content.lower() in ["gn", "good night"]:
        response = random.choice(night_responses)
        await message.channel.send(response)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    # Start the random messages task in the channel where the bot is first available
    for guild in bot.guilds:
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                bot.loop.create_task(send_random_messages(channel))
                return

bot.run(TOKEN)
