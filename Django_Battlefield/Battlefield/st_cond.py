# /usr/bin/python3

# MELNIKOV ILYA

from Battlefield.strategy import Random, Weakest, Strongest


SQUADS_PER_ARMY = 3
NAMES = ['Vikings', 'Cossacks', 'Murlocs', 'Orcs', 'Ponies', 'Pirates', 'Knights',
         'Elves', 'Demons', 'Insurers', 'Feminists', 'Cats', 'Babies']
SOLDIERS_PER_SQUAD = 5
VEH_PER_SQUAD = 5
OPERATORS_PER_VEH = 3
VEH_HEALTH = 100
VEH_RECHARGE = 1000
SOLDIER_HEALTH = 30
SOLDIER_RECHARGE = 500
STRATEGIES = [Random, Weakest, Strongest]
