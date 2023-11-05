# SurvivalX
Sender requests for SurvivalX game.

# Run script
```

python3 window.py

```
or
```

python3 -i main.py

```

# Usage
For use ```main.py``` you can write:
```python

# Use class
player = Player("player_id_from_game")

```

# API
```python

player.score           # ----> Show saved score after update player information.
player._update_score() # ----> Get player score by id and save to self.score.
player._get_pcid()     # ----> Get player pcid from score.

```

### player.set_score(*`money`=0, `vip`=0, `admin`=0, `license`=0, `ban`=0, `gametime`=420, `item_slot`="", `item_count`="", `hero_status`="", `gm_arena`=0, `gm_camp`=0, `gm_summer`=0, `hash`=""*)
> [!WARNING]
> Not inforamtioan about all
