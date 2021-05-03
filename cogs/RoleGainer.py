from discord.ext.commands import Cog, command
from discord.utils import get

from utils import get_cfg, revert
from main import get_logger


class RoleGainer(Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @Cog.listener()
    async def on_raw_reaction_add(self, pl):
        user = pl.member
        reaction = pl.emoji
        
        log_code = 20
        log_msg = f"Пользователь @{user.name} взял роль {reaction.name}."
        try:
            if str(pl.channel_id) != get_cfg()['channels']['roles']: return
            if user.bot: return
            await user.add_roles(get(user.guild.roles, name=revert(get_cfg()['emojies'])[reaction.name]))
        except:
            log_code = 40
            log_msg = f"Пользователь @{user.name} не смог взять роль {reaction.name}."
        await get_logger('roles').add_log(log_code, "ROLE_GAIN", log_msg)


    @Cog.listener()
    async def on_raw_reaction_remove(self, pl):
        guild = await self.bot.fetch_guild(pl.guild_id)
        reaction = pl.emoji
        user = get(await guild.fetch_members(limit=None).flatten(), id=pl.user_id)
        
        log_code = 20
        log_msg = f"Пользователь @{user.name} убрал роль {reaction.name}."
        try:
            if str(pl.channel_id) != get_cfg()['channels']['roles']: return
            if get(guild.roles, name=revert(get_cfg()['emojies'])[reaction.name]) in user.roles:
                await user.remove_roles(get(guild.roles, name=revert(get_cfg()['emojies'])[reaction.name]))
            else:
                raise Exception()
        except:
            log_code = 40
            log_msg = f"Пользователь @{user.name} не смог убрать роль {reaction.name}."
        await get_logger('roles').add_log(log_code, "ROLE_GAIN", log_msg)


def setup(bot):
    bot.add_cog(RoleGainer(bot))
