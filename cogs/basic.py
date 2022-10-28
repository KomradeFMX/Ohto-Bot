import interactions
from nextcord.ext import commands
import nextcord

class basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    #El comando ouo
    @nextcord.slash_command(description='Haz que te salude ouo')
    async def hola(self, inter):
        await inter.response.send_message(f'¡Hola, {inter.user.display_name}! ouo')



def setup(bot):
    bot.add_cog(basic(bot))
