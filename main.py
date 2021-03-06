import discord
import os

TOKEN = os.environ['TOKEN']


client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        hello = ':wave: Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, hello)
    elif message.content.startswith('!help'):
        help = '"!hello": lässt den bot antworten'.format(message)
        await client.send_message(message.channel, help)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
