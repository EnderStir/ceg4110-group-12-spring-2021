# Reference: https://realpython.com/how-to-make-a-discord-bot-python/
import discord
import command
import running
from replit import db

TOKEN = db["BOT_KEY"]
client = discord.Client()


# When the bot is ready for use
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord?')


initialCmd = {
    '-overview': (0, command.overview),
    '-monster': (1, command.monster, command.help_monster),
    '-weapon': (1, command.weapon, command.help_weapon),
    '-material': (1, command.material, command.help_material),
    '-save': (1, command.save, command.help_save),
    '-vendors': (0, command.vendor),
    '-products': (1, command.products, command.help_products),
    '-events': (0, command.events),
    '-location': (1, command.location, command.help_location),
    '-hunter tools': (0, command.hunters_tools),
    '-tip': (0, command.tip),
    '-guiding': (1, command.guiding, command.help_guiding),
    '-item': (1, command.item, command.help_item),
    '-defeatedMonster': (1, command.defeated_monster, command.help_defeated_monster),
    '-whoKilledMe': (1, command.who_killed_me, command.help_who_killed_me),
    '-armor': (1, command.armor, command.help_armor),
    '-skill': (1, command.skill, command.help_save)
}


# When a message is received
@client.event
async def on_message(message):
    response = None

    if message.content.split()[0] in initialCmd:
        cmd = message.content.split()[0]
        if initialCmd[cmd][0] == 0:
            response = initialCmd[cmd][1]()
        else:
            if message.content.split()[0] == message.content:
                response = initialCmd[cmd][2]()
            else:
                param = message.content.split(" ", 1)[1]
                response = initialCmd[cmd][1](param)

    if response is not None:
        if isinstance(response, discord.Embed):
            await message.channel.send(embed=response)
        else:
            await message.channel.send(response)


running.keep_bot_alive()
client.run(TOKEN)
