import nextcord
from nextcord import Interaction
from nextcord.ext import commands



intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True

client = commands.Bot(command_prefix = '/', intents= intents)

@client.event
async def on_ready():
    print("The bot is here")

testingSERVERID = 800097892353179658
@client.slash_command(description="Replies with hello", guild_ids=[testingSERVERID])
async def hello(interaction: nextcord.Interaction):
    print("running hello: command")
    print("interaction object")
    print(interaction)
    await interaction.send("sup", ephemeral=True)


client.run('MTA0ODM4NzQ1NzEyNjc2MDQ4OA.G8oTSz.T95qXf2g4OhcKhWTbn5AR1Jz4F2ERpw4Bzc064')
