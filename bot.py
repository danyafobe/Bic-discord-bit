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

gm_responses = [
    "Gm! I hope your coffee is stronger than my brain!",
    "Good morning! Are we sure it’s a good one?",
    "Gm! Stop spamming me with good mornings, will ya?",
    "Good morning, sunshine! Or is it just my screen glare?",
]

gn_responses = [
    "Gn! Sweet dreams! Or nightmares, I don’t judge.",
    "Good night! Don’t let the bedbugs bite, unless they’re friendly.",
    "Gn! I’ll be here, waiting for more of your messages.",
    "Good night! You guys really know how to spam me, huh?",
]

how_are_you_responses = [
    "How am I? I’m just a bunch of code, but thanks for asking!",
    "I'm doing great! Just sitting here, waiting for your messages.",
    "Oh, you know, living the dream... of a chatbot!",
    "How am I? I don't have feelings, but I feel... confused!",
    "Doing well! Just hoping for fewer spam messages.",
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

    # Проверяем на Gm или Gn
    if message.content.lower() == "gm":
        response = random.choice(gm_responses)
        await message.channel.send(response)
    elif message.content.lower() == "gn":
        response = random.choice(gn_responses)
        await message.channel.send(response)

    # Проверяем на How are you?
    if re.search(r'how (are you|are you doing)', message.content.lower()):
        response = random.choice(how_are_you_responses)
        await message.channel.send(response)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

bot.run(TOKEN)
