
import unittest
from space_invaders_game import Game  # Assuming the main game file is named space_invaders_game.py

class TestSpaceInvaders(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_player_movement(self):
        initial_position = self.game.player.position
        self.game.player.move_left()
        self.assertEqual(self.game.player.position, initial_position - 1, "Player should move left by 1 unit")
        self.game.player.move_right()
        self.game.player.move_right()
        self.assertEqual(self.game.player.position, initial_position + 1, "Player should move right by 2 units and back to initial position + 1")

    def test_shooting_projectiles(self):
        initial_projectiles_count = len(self.game.projectiles)
        self.game.player.shoot()
        self.assertEqual(len(self.game.projectiles), initial_projectiles_count + 1, "Shooting should increase projectiles count by 1")

    def test_enemy_movement(self):
        initial_enemy_position = self.game.enemy.position
        self.game.enemy.move()
        self.assertNotEqual(self.game.enemy.position, initial_enemy_position, "Enemy should move to a new position")

if __name__ == '__main__':
    unittest.main()
