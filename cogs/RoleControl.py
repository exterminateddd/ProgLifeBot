from discord.ext import commands
from discord.utils import get
from discord import Member

from mongo_control import add_pro_role, remove_pro_role, get_user_data, user_has_role
from utils import get_cfg, revert
from bot_utils import update_pro_roles
from main import get_logger


class RoleControl(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=['adv', 'pro', 'setpro', 'set_pro'])
    @commands.has_permissions(ban_members=True)
    async def set_pro_role(self, ctx, user: Member, role: str):
        msg = ''
        
        log_code = 20
        log_msg = f"Проверяющий @{ctx.author.name} выдал про-роль *{role}* пользователю @{user.name}"
        try:
            msg = f'Про-роль {role} успешно выдана пользователю {user.mention}.'
            if not add_pro_role(user.id, role):
                msg = f'Не удалось выдать про-роль {role} пользователю {user.mention}.'
            else: await update_pro_roles(await ctx.guild.fetch_roles(), user)
        except:
            log_msg = f"Проверяющий @{user.name} не смог выдать про-роль *{role}* пользователю @{user.name}"
            log_code = 40
        await ctx.send(msg)
        await get_logger('proroles').add_log(log_code, 'ROLE_CONTROL', log_msg)
    
    @commands.command(aliases=['disadv', 'unpro', 'unsetpro', 'unset_pro'])
    @commands.has_permissions(ban_members=True)
    async def unset_pro_role(self, ctx, user: Member, role: str):
        msg = f'Про-роль {role} успешно убрана у пользователя {user.mention}.'
        
        log_code = 20
        log_msg = f"Проверяющий @{ctx.author.name} выдал про-роль *{role}* пользователю @{user.name}"
        try:
            if not user_has_role(user.id, role) or not remove_pro_role(user.id, role):
                raise Exception('')
            await update_pro_roles(await ctx.guild.fetch_roles(), user)
        except:
            msg = f'Не удалось забрать про-роль {role} у пользователя {user.mention}.'
            log_code = 40
            log_msg = f"Пользователь @{ctx.author.name} не смог забрать про-роль *{role}* у пользователя @{user.name}"
        await ctx.send(msg)
        await get_logger('proroles').add_log(log_code, 'ROLE_CONTROL', log_msg)


def setup(bot):
    bot.add_cog(RoleControl(bot))
