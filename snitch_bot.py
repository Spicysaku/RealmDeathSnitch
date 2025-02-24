import discord
import asyncio
import image_downloader as imd
import guild_graveyard as gg
import json

intents = discord.Intents.default()
client = discord.Client(intents=intents)

imd.Download_Images()
with open('last death.json', 'w') as f:
    json.dump(gg.guild_graveyard("Anti Furry Force", 0), f)
f.close()

async def run_guild_graveyard():
    while True:
        gg.guild_graveyard("Anti Furry Force", 0)
        await asyncio.sleep(60)  # Wait for 60 seconds

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    client.loop.create_task(run_guild_graveyard())

client.run('YOUR_BOT_TOKEN')