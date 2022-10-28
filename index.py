import imp
from os import listdir
from nextcord.ext import commands
from nextcord import Interaction
import nextcord
import os
from config import TOKEN

bot = commands.Bot()

#Que hacer al iniciar el bot
@bot.event
async def on_ready():
    print(f'{bot.user.display_name} está en linea ouo')


for fn in os.listdir('./cogs'):
    if fn.endswith('.py'):
        bot.load_extension(f'cogs.{fn[:-3]}')


bot.run(TOKEN)