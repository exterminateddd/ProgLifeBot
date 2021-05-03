from discord.ext.commands import Bot
from discord.ext import commands
from discord.utils import get
from discord import Intents, Guild
from os import listdir
from loguru import logger
from os import system
from asyncio import sleep
from atexit import register

from utils import get_cfg, is_pro
from mongo_control import *
from classes.ChannelLogger import ChannelLogger

system('clear')

intents = Intents.default()
intents.members = True

revert = {v:k for k,v in get_cfg()['emojies'].items()}

bot = Bot(command_prefix="-", intents=intents)
logger_dict = {
    "roles": 0,
    "rolereqs": 0,
    "admin": 0,
    "proroles": 0
}
role_logger = 0


def get_logger(section):
    return logger_dict[section]


for filename in listdir('./cogs'):
    if filename.endswith('.py'):
        try:
            bot.load_extension(f'cogs.{filename[:-3]}')
            logger.info('SUCCESSFULLY Loaded Module '+filename[:-3])
        except Exception as e:
            logger.error('FAILED to Load Module '+filename[:-3])
            raise e


@bot.event
async def on_ready():
    logger_dict['roles'] = ChannelLogger(get(bot.guilds[0].text_channels, id=get_cfg()['channels']['log']['rolegain']), logger)
    logger_dict['admin'] = ChannelLogger(get(bot.guilds[0].text_channels, id=get_cfg()['channels']['log']['admin']), logger)
    logger_dict['rolereqs'] = ChannelLogger(get(bot.guilds[0].text_channels, id=get_cfg()['channels']['log']['rolereqs']), logger)
    logger_dict['proroles'] = ChannelLogger(get(bot.guilds[0].text_channels, id=get_cfg()['channels']['log']['prorole']), logger)
    print('='*100)


@bot.event
async def on_member_join(member):
    if not get_user_data(member):
        add_user(member.id)


bot.run(get_cfg()['token'])
