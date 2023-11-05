import json

DEFAULT_ARGS = ['', 0, 0, 0, 0, 0, '', '', '']

def save_info(*args):
    # player_id, money, vip, admin, license, ban, item_slot, item_count, hero_status
    with open('settings_panel.json', 'w') as file:
        json.dump(args, file)

    return DEFAULT_ARGS

def load_save():
    try:
        with open('settings_panel.json', 'r') as file:
            return json.loads(file.read())

    except:
        return save_info(DEFAULT_ARGS)
