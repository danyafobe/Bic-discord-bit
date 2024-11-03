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
    "Oh, wait, wait, I think I’m stuck…"
]

greetings_responses = {
    "gm": [
        "Good morning! I hope you have a nice day!",
        "Gm gm gm gm gm!",
        "Ugh, another morning, right?",
        "You can shove your gm in my piss jar!",
        "No, not good."
    ],
    "gn": [
        "Good night! Sleep well!",
        "Gngngngngngngn!",
        "Don't let the bedbugs bite!",
        "You can put your gn where the sun doesn't shine!",
        "Good night! If you hear explosions at night, that's me... farting..."
    ],
    "how_are_you": [
        "I'm just a bot, but I'm functioning!",
        "Feeling binary today!",
        "I'm doing great, how about you?",
        "Just existing in the digital void!"
    ]
}

nev_responses = [
    "This fuckin Nev keeps putting me on the pfp.",
    "Nev, my creator, my daddy... I hate him.",
    "When will this Nev give me my jars back?",
    "Nev is definitely not keeping me as a slave 🖐️✊🖐️✊",
    "Don't tell Nev that my hundred is hidden in his alive 1111 picture"
]

random_messages = [
    "I don't care.",
    "Got it, I'm just pooping.",
    "Ha-ha-ha!",
    "Just living the bot life!",
    "What even is life?"
]

async def send_random_messages(channel):
    print(f"Started sending random messages in {channel.name}")
    while True:
        await asyncio.sleep(random.randint(1200, 1800))  # Random wait time between 20 and 30 minutes
        message = random.choice(random_messages)
        await channel.send(message)
        print(f"Sent random message: {message}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if re.search(r'\?$', message.content):
        response = random.choice(funny_responses)
        await message.channel.send(response)
    
    elif message.content.lower().startswith('gm'):
        response = random.choice(greetings_responses["gm"])
        await message.channel.send(response)

    elif message.content.lower().startswith('gn'):
        response = random.choice(greetings_responses["gn"])
        await message.channel.send(response)

    elif re.search(r'how.*are.*you', message.content.lower()):
        response = random.choice(greetings_responses["how_are_you"])
        await message.channel.send(response)
    
    elif "nev" in message.content.lower():
        response = random.choice(nev_responses)
        await message.channel.send(response)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    for guild in bot.guilds:
        print(f"Checking channels in guild: {guild.name}")
        for channel in guild.text_channels:
            print(f"Found channel: {channel.name}")
            if channel.permissions_for(guild.me).send_messages:
                print(f"Bot has permission to send messages in {channel.name}. Starting random messages...")
                bot.loop.create_task(send_random_messages(channel))
                return
            else:
                print(f"Bot does not have permission to send messages in {channel.name}.")
    print("No suitable channel found to send random messages.")

bot.run(TOKEN)
