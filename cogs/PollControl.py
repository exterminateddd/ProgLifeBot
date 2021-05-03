from discord.ext import commands
from discord.utils import get
from discord import Emoji, Embed, Colour

from emoji import emojize
from main import get_logger


class PollControl(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def create_poll(self, ctx, title, text, var_num: int = None):
        try:
            await ctx.message.delete()
            embed = Embed(color=Colour(16776960))
            embed.add_field(name=title, value=text, inline=False)
            msg = await ctx.send("", embed=embed)
            if var_num:
                for num in range(var_num):
                    await msg.add_reaction(get(ctx.guild.emojis, name=str(num+1)+"_"))
            if not var_num:
                await msg.add_reaction(emojize(':thumbs_up:'))
                await msg.add_reaction(emojize(':thumbs_down:'))
            await get_logger().add_log(20, "POLL_CONTROL", f"Пользователь {ctx.author.mention} создал опрос в канале #{ctx.channel.name}")
        except:
            await get_logger().add_log(40, "POLL_CONTROL", f"Пользователь {ctx.author.mention} не смог создать опрос в канале #{ctx.channel.name}")


def setup(bot):
    bot.add_cog(PollControl(bot))
