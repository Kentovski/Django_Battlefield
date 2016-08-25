# /usr/bin/python3

# MELNIKOV ILYA

import random


class AbstractAttackStrategy:

    @classmethod
    def chose_enemy_squad(cls, enemy_army):
        raise NotImplementedError


class Random(AbstractAttackStrategy):

    @classmethod
    def chose_enemy_squad(cls, enemy_army):
        squads = enemy_army.get_alive_squads()
        return random.choice(squads) if squads else None


class Weakest(AbstractAttackStrategy):

    @classmethod
    def chose_enemy_squad(cls, enemy_army):
        weakest_success = None
        weakest_squad = None

        enemy_alive_squads = enemy_army.get_alive_squads()

        for squad in enemy_alive_squads:
            if not weakest_success or squad.get_success_attack() < weakest_success:
                weakest_success = squad.get_success_attack()
                weakest_squad = squad
        return weakest_squad


class Strongest(AbstractAttackStrategy):

    @classmethod
    def chose_enemy_squad(cls, enemy_army):
        strongest_success = None
        strongest_squad = None

        enemy_alive_squads = enemy_army.get_alive_squads()

        for squad in enemy_alive_squads:
            if not strongest_success or squad.get_success_attack() > strongest_success:
                strongest_success = squad.get_success_attack()
                strongest_squad = squad
        return strongest_squad
