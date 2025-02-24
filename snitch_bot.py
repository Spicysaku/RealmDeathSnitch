import discord
import asyncio
import image_downloader as imd
import guild_graveyard as gg
import json
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path('/Users/valentinthevoz/Desktop/Python projects/RealmDeathSnitch/.venv/include/keys.env'))


intents = discord.Intents.default()
client = discord.Client(intents=intents)
channel_id = int(os.getenv("CHANNEL_ID"))
channel = None

imd.Download_Images()
with open('last death.json', 'w') as f:
    json.dump(gg.guild_graveyard("Anti Furry Force", 0), f)
f.close()

async def run_guild_graveyard():
    while True:
        print("update")
        latest_death = gg.guild_graveyard("Anti Furry Force", 0)
        if latest_death != json.load(open('last death.json')) and latest_death['player-name'] != "private":
            print("someone died")
            with open('last death.json', 'w') as f:
                json.dump(latest_death, f)
            f.close()
            channel = client.get_channel(int(channel_id))
            await channel.send(f"**{latest_death['player-name']}** died at **{latest_death['time']}**\n"
                               f"**Killer:** {latest_death['killed_by']}\n")
        await asyncio.sleep(60)  # Wait for 60 seconds

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    client.loop.create_task(run_guild_graveyard())

discord_key = os.getenv("DISCORD_KEY")
client.run(discord_key)
