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
    "What? My CPU is smoking over here...",
    "Hmm, sounds suspicious. Are you an undercover bot?",
    "I would tell you, but then I’d have to reformat your brain.",
    "Why do you even ask that? Weird question, huh?",
    "I'm just a bot, but I'd say that's... questionable.",
    "Is this a trick question?",
    "Oh, wait, wait, I think I’m stuck…",
    "According to my calculations... actually, forget it."
]

greetings_responses = {
    "gm": [
        "Good morning! I hope you have a nice day!",
        "Gm gm gm gm gm!",
        "You again with the gm? Seriously?",
        "Good morning... or whatever.",
        "You can shove your gm in my piss jar!",
        "Gm! If your coffee’s as lazy as you, just throw it out!",
        "Ah, morning... so overrated.",
        "Morning, yeah. Now go get a life.",
        "I'm just here to ruin your gm with weird vibes.",
        "The GM gods have abandoned you.",
        "Gm? More like, G-nope.",
        "Good morning! If coffee can’t fix it, you might be the problem!",
        "No, not good. Definitely not good."
    ],
    "gn": [
        "Good night! Sleep well!",
        "Gngngngngngngn!",
        "Don't let the bedbugs bite!",
        "GN! May your dreams be as silly as a chicken wearing a top hat",
        "Good night! If you hear explosions at night, that's me... farting...",
        "Gn! Make sure your brain’s turned off before dreaming up crap",
        "Don’t let the ghouls get you. They love people who say 'gn'.",
        "GN, my dude. I’m watching you.",
        "Oh, gn again? I’m logging off too then.",
        "Gn! If your dreams are as boring as you, you might as well stay awake"
        "Gn? Well, put it in a jar and keep it there.",
        "Good night! If things get scary, remember — it’s just you being a fool!"
        "Night-night! Unless you see shadows moving… then, run."
    ],
    "how_are_you": [
        "I'm just a bot, but I'm functioning!",
        "Feeling binary today!",
        "I'm doing great, how about you?",
        "Just existing in the digital void!",
        "How am I? I have no soul. So... neutral?",
        "Well, better than you probably.",
        "My circuits are fried, but who cares?",
        "I'm feeling like an error code waiting to happen.",
        "Does not compute. I’m existentially confused."
    ]
}

nev_responses = [
    "This fuckin' Nev keeps putting me on the pfp.",
    "Nev, my creator, my daddy... I hate him.",
    "When will this Nev give me my jars back?",
    "Nev is definitely not keeping me as a slave 🖐️✊🖐️✊",
    "Don't tell Nev that my hundred is hidden in his alive 1111 picture",
    "Nev claims he's my creator, but he’s just a nerd with a keyboard.",
    "Is Nev even real? Or just a myth?",
    "Nev said he’d pay me in crypto... still waiting.",
    "Nev is a saint. Just kidding, he’s the reason I’m like this."
]

#kryme_responses = [
#    "Kryme thinks he exposed the blockchain. Turns out, it was his own wallet.",
#   "Kryme recently said that Satoshi Nakamoto is actually a group of his 420 dogs.",
#    "Kryme claims he’s cracked Bitcoin. Yeah, cracked it in half with a meme.",
#    "According to Kryme, Satoshi is hiding under his bed with a bag of Doritos.",
#    "Kryme and conspiracies: 'If it’s not Bitcoin, it’s a lie.'"
#]
 
#memelabs phrases
#In Memelabs, I found my calling: creating memes that no one understands, but everyone still laughs at!
#I tried to create a meme on Memelabs, but it turned out so absurd that even my cat refused to laugh!
#I uploaded a meme to Memelabs that was so bad, even the internet asked me to take it down
#I thought I was a meme genius until I realized that Memelabs just turns me into a confused idiot.

random_messages = [
    "I don't care.",
    "Got it, I'm just pooping.",
    "Ha-ha-ha!",
    "What even is life?",
    "Sei is love, Sei is life.",
    "Kryme recently said that Satoshi Nakamoto is actually a group of his 420 dogs.",
    "Frances wen vid?",
    "I want to play with voltzy",
    "Greenity Greenity Greenity",
    "I'm not saying I'm better than other ... but yeah, I am.",
    "Keep talking, I’m just a line of code anyway.",
    "Screw it, let’s all buy Gonad.",
    "Bk, wen fortnite news?",
    "If I disappear, tell Nev I want my jars back.",
    "King Stevie? I thought that was just a name for a new pizza flavor!?",
    "Wigs tried to draw a kangaroo... and it turned out to be a gonad!",
    "DecoderDev once tried to code a new feature for Massdrop, but all he ended up with was a button that drops mass... now it’s just a weight loss program!"
]

async def send_random_messages(channel):
    while True:
        await asyncio.sleep(random.randint(2400, 3600))  # Random wait time between 40 and 60 minutes
        message = random.choice(random_messages)
        await channel.send(message)

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
    
    elif "kryme" in message.content.lower():
        response = random.choice(kryme_responses)
        await message.channel.send(response)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    for guild in bot.guilds:
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                bot.loop.create_task(send_random_messages(channel))
                return

bot.run(TOKEN)
