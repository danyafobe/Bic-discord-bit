import discord
import random
import re
import os

# Загружаем токен из переменной окружения
TOKEN = os.getenv("DISCORD_TOKEN")

# Устанавливаем намерения
intents = discord.Intents.default()
intents.message_content = True  # Это необходимо для получения текстовых сообщений

# Создаем экземпляр клиента
bot = discord.Client(intents=intents)

# Список смешных ответов
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

# Функция для генерации смешного ответа
def generate_funny_response(question):
    if random.random() < 0.3:  # 30% вероятности выдать смешной ответ
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

# Событие, когда бот получает сообщение
@bot.event
async def on_message(message):
    if message.author == bot.user:  # Игнорируем собственные сообщения
        return

    if re.search(r'\?$', message.content):  # Проверяем, заканчивается ли сообщение вопросительным знаком
        response = generate_funny_response(message.content)  # Генерируем ответ
        await message.channel.send(response)  # Отправляем ответ в канал

# Событие, когда бот готов
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Запускаем бота
bot.run(TOKEN)
