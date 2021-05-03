from discord import TextChannel, Embed, Colour


levels = {
    40: {
        "color": Colour.red,
        "name": "error"
        },
    30: {
        "color": Colour.gold,
        "name": "warning"
        },
    20: {
        "color": Colour.blue,
        "name": "info"
        }
}


class ChannelLogger:
    def __init__(self, channel: TextChannel, loguru_logger):
        self.logger = loguru_logger
        self.channel = channel
    
    async def add_log(self, level: int, log_mark: str,  msg: str):
        getattr(self.logger, levels[level]['name'])(msg)
        
        embed = Embed(color=Colour.red())
        embed.color = levels[level]['color']()
        embed.add_field(name=f"*[{levels[level]['name']}] ({log_mark.upper()})*", value=msg)
        
        await self.channel.send("", embed=embed)
