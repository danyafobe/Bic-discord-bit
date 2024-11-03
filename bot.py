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
    "Oh, wait, wait, I think I’m stuck…"
]

def generate_funny_response(question):
    if random.random() < 0.3: 
        return random.choice(funny_responses)
    elif "how" in question.lower():
        return "Well… somehow, I guess."
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

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

bot.run(TOKEN)
