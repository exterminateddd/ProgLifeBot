from discord.ext import commands
from discord.utils import get
from discord import Emoji, Embed, Colour, Guild, Member

import webhook_control
from bot_utils import update_pro_roles
from main import get_logger
from utils import is_pro, get_cfg, revert
from main import get_logger


class AdminCommands(commands.Cog):
    def __init__(self, bot):
        print('inited')
        self.bot = bot

    @commands.command(aliases=['update_pro_roles', 'updateProRoles'])
    @commands.has_permissions(ban_members=True)
    async def update_pro_roles_(self, ctx, user: Member):
        await update_pro_roles(await ctx.guild.fetch_roles(), user)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def tmp(self, ctx):
        pass

    @commands.command(aliases=['update'])
    @commands.is_owner()
    async def update_wh(self, ctx, section):
        log_code = 20
        log_msg = f"Админ @{ctx.author.name} успешно обновил секцию {section}"
        try:
            if section in ['rules', 'roles', 'rolerequests']:
                await getattr(webhook_control, "update_"+section)(self.bot)
            else:
                await ctx.send('Section not found.')
                raise KeyError('')
        except Exception:
            log_code = 40
            log_msg = f"Админ @{ctx.author.name} не смог обновить секцию {section}"
        await get_logger('admin').add_log(log_code, "ADMIN_COMMANDS", log_msg)


def setup(bot):
    bot.add_cog(AdminCommands(bot))
