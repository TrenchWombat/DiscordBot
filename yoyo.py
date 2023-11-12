import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is now online')

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content == 'yo':
        await message.channel.send('yo')

client.run('MTE3MzM3MjI1Nzk2MDIwMjMxMQ.GfMfGC.UopWEMVrUqDKn3jghp5LwAqLPNTTd_rqfFXP5w')
