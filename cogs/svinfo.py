import interactions
from nextcord.ext import commands
from nextcord import File
import nextcord
import easy_pil
from easy_pil import *

class svinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    #El comando ouo
    @nextcord.slash_command(description='Muestra la información del servidor')
    async def serverinfo(self, inter):

        #Hacer la imagen del comando de rango
        fondo = Editor('./cogs/src/svinfo_bg.png')

        fondo.rectangle((0, 0), width=700, height=100, fill="#ffe400")
        try:
            pfpServer = await load_image_async(inter.guild.icon.url)
        except:
            pfpServer = await load_image_async('https://external-preview.redd.it/4PE-nlL_PdMD5PrFNLnjurHQ1QKPnCvg368LTDnfM-M.png?auto=webp&s=ff4c3fbc1cce1a1856cff36b5d2a40a6d02cc1c3')
        cargarpfp = Editor(pfpServer).resize((150, 150))

        fondo.paste(cargarpfp, (15, 15))

        unisansH = Font("./fonts/UniSansH.otf", 72)
        unisansHs = Font("./fonts/UniSansH.otf", 60)

        fondo.text((180,27), f'{inter.guild.name}', font=unisansH, color='#ffffff')

        foto = File(fp=fondo.image_bytes, filename='svinfo.png')
        await inter.response.send_message(file=foto)



def setup(bot):
    bot.add_cog(svinfo(bot))
