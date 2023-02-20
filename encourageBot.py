import discord
import os
import requests
import json
import random
from dotenv import load_dotenv


# Creamos una instancia del bot
client = discord.Client(intents=discord.Intents.default())


sad_words = ['sad','depressed','unhappy','angry','miserable','depressing']

starter_encouragements = ['Cheer up!', 'Hang in there','You are a great person / bot!']

def get_quote():
    #Recibimos un random quote y lo pasamos a Json
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + ' -' + json_data[0]['a']
    return(quote)




# Registramos un evento con el decorador de Client
@client.event
#Este evento va a iniciarse cuando el botón este listo para ser usado
#Este evento inicia cuando el bot está listo básicamente
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    msg = message.content
    
    if msg.startswith('$hello'):
        await message.channel.send('Hello!')

    if msg.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))


load_dotenv()
TOKEN = os.getenv('TOKEN')

client.run(TOKEN)


