import discord
import config
import calculations

client = discord.Client()

@client.event
async def on_ready():
    calculations.clear()
    calculations.logger(client.user, "Connected to the server!")

@client.event
async def on_message(message):
    if message.author.name == client.user.name:
        return
    if message.content == "!time":
        await message.channel.send(f"Time: {calculations.Time()}")
    elif message.content == "!ping":
        await message.channel.send("pong")
    calculations.logger(message.author.name, message.content)

client.run( config.token )
