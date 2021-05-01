import discord
import requests


API_URL = 'http://204.48.22.151:5555/model'
TOKEN = 'ВАШ ТОКЕ'
client = discord.Client()

def request_sentiment(message):
    data = {'x': [message]}
    res = requests.post(API_URL, json=data).json()
    santiment = res[0][0]
    return santiment

# @client.event - это декоратор. 
# Декораторами в питоне незывают функции, 
# который принимают функцию как аргумент и возвращают функцию
@client.event
async def on_ready():
    for guild in client.guilds:
        print('Hello '+str(guild))


@client.event
async def on_message(message):
    # В случае, если автором сообщения является бот
    # то мы не отвечаем. Иначе бот будет разговаривать сам с собой
    if message.author == client.user:
        return

    setiment = request_sentiment(message.content)
    if setiment == 'positive':
        await message.channel.send('Спасибо за добрые слова')     
    if setiment == 'negative':
        await message.channel.send('Хватит ругаться')     
    if setiment == 'neutral':
        await message.channel.send('Хорошо') 

# Команда должна быть всегда в самом низу нашего скрипта
client.run(TOKEN)