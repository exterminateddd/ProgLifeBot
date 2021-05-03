from discord.ext.commands import Cog, command
from discord.utils import get

from utils import get_cfg
from emoji import emojize


class MemesControl(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    @Cog.listener()
    async def on_message(self, msg):
        await self.bot.process_commands(msg)
        if msg.channel.id != int(get_cfg()['channels']['memes']):
            return
        if not 2 > len(msg.attachments) > 0:
            await msg.delete()
            return
        await msg.add_reaction(emojize(':thumbs_up:'))
        await msg.add_reaction(emojize(':thumbs_down:'))
        await msg.add_reaction("\N{no entry sign}")


    @Cog.listener()
    async def on_raw_reaction_add(self, pl):
        user = pl.member
        reaction = pl.emoji
        if user.bot: return
        if pl.channel_id != int(get_cfg()['channels']['memes']) or reaction.name != '\N{no entry sign}':
            return
        
        msg = get(await get(user.guild.text_channels, id=int(get_cfg()['channels']['memes'])).history(limit=10).flatten(), id=pl.message_id)
        
        if user.guild_permissions.administrator or msg.author.id == user.id:
            await msg.delete()


def setup(bot):
    bot.add_cog(MemesControl(bot))
