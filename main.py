import discord

TOKEN = 'REPLACE_WITH_YOUR_TOKEN'

client = discord.Client()

async def check_groups(): 
    for channel in client.private_channels:
        if(isinstance(channel, discord.GroupChannel)):
            await channel.send("again skids, as i keep saying: i can auto leave these. your shitty spammer barely works lmao")
            print(f"We're leaving {channel.name}!")
            await channel.leave(silent=True)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    print(client.private_channels)
    await check_groups()

client.run(TOKEN)
