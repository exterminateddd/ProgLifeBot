from json import load

def get_cfg():
    return load(open('config.json', "r+", encoding='utf-8'))


def revert(dict_):
    return {v:k for k,v in dict_.items()}


def is_pro(role_name: str) -> bool:
    return role_name.startswith('✓')
