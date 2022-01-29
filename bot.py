import discord, iodatabase, classes, random, time, config
seed = str(time.time())
random.seed(version=seed)

def init_log():
    timestamp = time.strftime("%y-%m-%d+%H-%M-%S")
    log = iodatabase.create_connection(timestamp)
    iodatabase.create_table(log, 'log')
    return log

client = discord.Client()
log = init_log()

@client.event
async def on_ready():
    iodatabase.execute(log, classes.DataLog(type="system", channel=None, 
                                            user=client.user, content="Bot started!"))

@client.event
async def on_message(message: discord.Message):
    if message.author.name == client.user.name:
        return
    iodatabase.execute(log, classes.DataLog(type="message", channel=message.channel.name, 
                                            user=message.author, content=message.content))


client.run( config.token )
