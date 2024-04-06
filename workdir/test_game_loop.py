
import unittest
from space_invaders import Game

class TestGameLoop(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_game_state_update(self):
        # Initial state
        initial_player_position = self.game.player.position
        self.game.player.move('right', 50)
        self.game.update_game_state()
        # Verify player position is updated
        self.assertNotEqual(self.game.player.position, initial_player_position)

    def test_collision_detection_bullet_enemy(self):
        # Setup an enemy and fire a bullet towards it
        self.game.enemies.append(Enemy(position=(400, 300)))
        self.game.player.position = 400  # Align player with enemy
        self.game.player.fire_bullet()
        initial_enemy_count = len(self.game.enemies)
        # Simulate game loop until collision is detected
        while len(self.game.bullets) > 0:
            self.game.update_game_state()
        # Verify enemy is removed after being hit
        self.assertEqual(len(self.game.enemies), initial_enemy_count - 1)

    def test_game_ends_when_all_enemies_destroyed(self):
        # Setup a single enemy
        self.game.enemies.append(Enemy(position=(400, 300)))
        self.game.player.position = 400  # Align player with enemy
        self.game.player.fire_bullet()
        # Simulate game loop until all enemies are destroyed
        while len(self.game.enemies) > 0:
            self.game.update_game_state()
        # Verify game ends
        self.assertTrue(self.game.is_game_over())

    def test_game_ends_when_player_hit(self):
        # Assuming an enemy can hit the player directly
        self.game.enemies.append(Enemy(position=(400, 300), bullet=(400, 350)))
        # Simulate game loop until player is hit
        while not self.game.is_game_over():
            self.game.update_game_state()
        # Verify game ends
        self.assertTrue(self.game.is_game_over())

if __name__ == '__main__':
    unittest.main()
