from discord.ext import commands
from discord.utils import get
from discord import Emoji, Embed, Colour


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=['tempmute', 'мут'])
    async def mute(self, ctx, member, time):
        pass


def setup(bot):
    bot.add_cog(Moderation(bot))
