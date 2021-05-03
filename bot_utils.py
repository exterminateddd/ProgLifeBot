from discord.utils import get
from discord.member import Member

from mongo_control import add_pro_role, remove_pro_role, user_has_role, get_user_data
from utils import get_cfg, revert, is_pro


async def update_pro_roles(guild_roles, user):
    roles = get_user_data(user.id)['proRoles']
    for role in roles:
        cur_role = get(guild_roles, name='✓'+revert(get_cfg()['emojies'])[role])
        if not cur_role: continue
        if cur_role not in user.roles:
            await user.add_roles(cur_role)
    for role in user.roles:
        if not is_pro(role.name): continue
        if get_cfg()['emojies'][role.name[1:]] not in roles:
            await user.remove_roles(role)


async def can_user_give_role(user: Member, role) -> bool:
    pass
