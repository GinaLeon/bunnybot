import nextcord
from nextcord import Interaction
from nextcord.ext import commands

intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True

client = commands.Bot(command_prefix = '>', intents= intents)

@client.event
async def on_ready():
    print("The bot is here")

testingSERVERID = 800097892353179658
@nextcord.slash_command(name = "hello", description="Replies with hello", guild_ids=[testingSERVERID])
async def hellocommand(interaction: Interaction):
    await interaction.response.send_message("Hello")

client.run('MTA0ODM4NzQ1NzEyNjc2MDQ4OA.Gn4h6_.gW2-2SXmGtDqI8f3mTlB0GavZsuMrXuCS95d1Q')
