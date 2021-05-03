from discord import Webhook, RequestsWebhookAdapter, Embed, Message, Colour
from discord.utils import get

from utils import get_cfg, revert


async def update_roles(bot):
    print('updating roles')
    webhook = Webhook.from_url(
        "https://discord.com/api/webhooks/834812481452507217/NWJT9K037s79hU_WtGcKVYuHtygUJFKKgL8y5rc4iuhodDdeQyvrd5iQ0caW-YpZuJzx",
        adapter=RequestsWebhookAdapter()
        )
    emojies = get_cfg()['emojies']
    channel = get(bot.guilds[0].text_channels, id=get_cfg()['channels']['roles'])
    embed = Embed()
    embed.add_field(
        name="Получение ролей", 
        value="Здесь можно получить роли по языкам, которые вы знаете или учите.", 
        inline=False
        )
    for em in emojies:
        em_ = get(channel.guild.emojis, name=emojies[em])
        embed.add_field(
            name=f"{em_}{em}", 
            value=em, 
            inline=False
            )
    for msg in await channel.history(limit=100).flatten():
        await msg.delete()
    webhook_msg = webhook.send("", embed=embed, wait=True)
    msg = get(await channel.history(limit=100).flatten(), id=webhook_msg.id)
    for em in emojies:
        await msg.add_reaction(emoji=get(channel.guild.emojis, name=emojies[em]))


async def update_rules(bot):
    print('updating rules')
    webhook = Webhook.from_url(
        "https://discord.com/api/webhooks/835210527848267796/Nhs1MOpneDWIEn4NkkATl0IPGK8TrKDiG3-o_J_eT33OVcGgnb3JVSe1BRQHYUYygKiw",
        adapter=RequestsWebhookAdapter()
        )
    channel = get(bot.guilds[0].text_channels, id=get_cfg()['channels']['rules'])
    rule_msgs = await channel.history(limit=10).flatten()
    for msg in rule_msgs:
        await msg.delete()
    embed_header = Embed(color=Colour(12745742))
    embed = Embed(color=Colour(15844367))
    embed_header.add_field(
        name="Правила *ProgLife*,", 
        value="обязательные для соблюдения всеми участниками сервера.", 
        inline=False
        )
    for rule in get_cfg()['rules']:
        embed.add_field(
            name=rule['title'], 
            value=rule['add']+" [ "+rule['fine']+" ]", 
            inline=False
            )
    webhook.send("", embeds=[embed_header, embed])


async def update_rolerequests(bot):
    print('updating rolereqs')
    webhook = Webhook.from_url(
        "https://discord.com/api/webhooks/835525089381449798/AVFr4D_tAdonMTyCsbpg9XsXF_bYuAhBfwg4rD-AXnFQgyQSUH7YntlmU6V_u-slBtob",
        adapter=RequestsWebhookAdapter()
        )
    channel = get(bot.guilds[0].text_channels, id=get_cfg()['channels']['role-request'])
    req_msgs = await channel.history(limit=10).flatten()
    for msg in req_msgs:
        await msg.delete()
    embed_header = Embed(color=Colour(12745742))
    embed_header.add_field(
        name="Запрос про-ролей", 
        value="Вставьте сюда ссылку на свой GitHub, чтобы запросить про-роль по любому языку.",
        inline=False)
    webhook.send("", embed=embed_header)
