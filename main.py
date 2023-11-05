import requests, json

headers={'User-Agent': 'UnityPlayer/4.7.2f1 (http://unity3d.com)', 'Host': 'a0880316.xsph.ru'}

try:
    with open('users_log.json', 'r') as file:
        LOG_BASE = json.loads(file.read())

except:
    with open('users_log.json', 'w') as file:
        LOG_BASE = {}

# NORMAL CODE

class Player:
    '''Class "Player" for add or remove permission and money for player in game "SurvivalX".'''

    def __init__(self, ID):
        '''Input player id for change player states.'''
        self.id = ID
        self.work_id = True

        if not self._update_score():
            del self
            return None

        self._get_pcid()

    def _update_score(self):
        '''Get player score by id and save to self.score.'''
        self.score = requests.get(f'http://a0880316.xsph.ru/SurvivalBD/display.php?viewer_id={self.id}', headers=headers).text

        if len(str(self.score)) <= 3:
            print(F'Player width ID ({self.id}) - Not found!')
            self.work_id = False
            return False
        
        LOG_BASE[str(self.id)] = self.score
        with open('users_log.json', 'w') as file:
            json.dump(LOG_BASE, file)

        return True
            

    def _get_pcid(self):
        '''Get player pcid from score.'''
        self.pcid = self.score.split('\t')[6]

    def set_score(self, money=0, vip=0, admin=0, license=0, ban=0, gametime=420, item_slot='', item_count='', hero_status='', gm_arena=0, gm_camp=0, gm_summer=0, hash=''):
        parameters = {
            "viewer_id": self.id,
            "pcid": self.pcid,
            "money": money,
            "vip": vip,
            "admin": admin,
            "license": license,
            "ban": ban,
            "gametime": gametime,
            "item_slot": item_slot,
            "item_count": item_count,
            "hero_status": hero_status,
            "gm_arena": gm_arena,
            "gm_camp": gm_camp,
            "gm_summer": gm_summer,
            "hash": hash
        }

        requests.get(f'http://a0880316.xsph.ru/SurvivalBD/updatescore.php', params=parameters, headers=headers)
        self._update_score()

if __name__ == '__main__':
    # FOR Maori ADD ALL
    # Maori = Player('1837840')
    # Maori.set_score(vip=3, admin=1, money=5000, license=1)

    pass