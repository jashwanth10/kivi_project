import unittest
from src.entity.entity import Entity
from src.constants.constants import ACTION_DICT


class TestEntity(unittest.TestCase):
    def test_fight_rock_paper(self):
        player_1 = Entity("player_1", ACTION_DICT["R"])
        player_2 = Entity("player_2", ACTION_DICT["P"])
        player_1.fight(player_2)
        self.assertEqual(player_2.points, 1)
        self.assertEqual(player_1.points, 0)


    def test_fight_rock_scissor(self):
        player_1 = Entity("player_1", ACTION_DICT["R"])
        player_2 = Entity("player_2", ACTION_DICT["S"])
        player_1.fight(player_2)
        self.assertEqual(player_1.points, 1)
        self.assertEqual(player_2.points, 0)

    def test_fight_paper_scissor(self):
        player_1 = Entity("player_1", ACTION_DICT["P"])
        player_2 = Entity("player_2", ACTION_DICT["S"])
        player_1.fight(player_2)
        self.assertEqual(player_1.points, 0)
        self.assertEqual(player_2.points, 1)

    def test_fight_paper_paper(self):
        player_1 = Entity("player_1", ACTION_DICT["P"])
        player_2 = Entity("player_2", ACTION_DICT["P"])
        player_1.fight(player_2)
        self.assertEqual(player_1.points, 0)
        self.assertEqual(player_2.points, 0)

    def test_fight_rock_rock(self):
        player_1 = Entity("player_1", ACTION_DICT["R"])
        player_2 = Entity("player_2", ACTION_DICT["R"])
        player_1.fight(player_2)
        self.assertEqual(player_1.points, 0)
        self.assertEqual(player_2.points, 0)

    def test_fight_scissor_scissor(self):
        player_1 = Entity("player_1", ACTION_DICT["S"])
        player_2 = Entity("player_2", ACTION_DICT["S"])
        player_1.fight(player_2)
        self.assertEqual(player_1.points, 0)
        self.assertEqual(player_2.points, 0)
