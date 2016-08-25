# /usr/bin/python3

# MELNIKOV ILYA

from Battlefield.st_cond import *
from Battlefield.units import *

import random


class Factory:

    def create_soldier(self):
        return Soldier(SOLDIER_HEALTH, SOLDIER_RECHARGE)

    def create_vehicle(self):
        operators = [self.create_soldier() for i in range(OPERATORS_PER_VEH)]
        health = (OPERATORS_PER_VEH * SOLDIER_HEALTH + VEH_HEALTH) / (OPERATORS_PER_VEH + 1)
        return Vehicle(health, operators, VEH_RECHARGE, VEH_HEALTH)

    def create_squad(self):
        soldiers = [self.create_soldier() for i in range(SOLDIERS_PER_SQUAD)]
        vehicles = [self.create_vehicle() for i in range(VEH_PER_SQUAD)]
        units = soldiers + vehicles
        return Squad(units)

    def create_army(self):
        strategy = random.choice(STRATEGIES)
        squads = [self.create_squad() for i in range(SQUADS_PER_ARMY)]
        name = random.choice(NAMES)
        return Army(squads, strategy, name)

    def create_battlefield(self, armies_num):
        armies = [self.create_army() for i in range(armies_num)]
        return Battlefield(armies)
