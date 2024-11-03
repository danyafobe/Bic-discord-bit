import discord
import random
import re
import os

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
    "Mornin’! Why are you awake so early? gmgmgmgmgmgmg!",
    "Rise and shine! I think I need more coffee... gmgmgmgmg!",
    "Put your gm in my piss jar!",
    "Good morning! Did you bring me breakfast?"
]

night_responses = [
    "Good night! Sleep tight, don’t let the bed bugs bite! gngngngngngngn!",
    "Nighty night! Dream about food... gngngngngng!",
    "Sweet dreams! Don’t forget to count sheep... gngngngngngngn!",
    "Put your gn in my piss jar!",
    "Good night! If you hear strange noises, it's just me thinking about life."
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

bot.run(TOKEN)
