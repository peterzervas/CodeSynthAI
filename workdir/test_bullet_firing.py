
import unittest
from space_invaders import Game

class TestBulletFiring(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_bullet_creation_on_fire(self):
        # Assuming initial bullet count is 0
        initial_bullet_count = len(self.game.bullets)
        self.game.player.fire_bullet()
        # Verify that bullet count increases by 1 after firing
        self.assertEqual(len(self.game.bullets), initial_bullet_count + 1)

    def test_bullet_movement(self):
        # Fire a bullet and get its initial position
        self.game.player.fire_bullet()
        initial_bullet_position = self.game.bullets[-1].position
        # Assuming game loop updates bullet position
        self.game.update_game_state()
        # Check if bullet has moved from its initial position
        self.assertNotEqual(self.game.bullets[-1].position, initial_bullet_position)

    def test_bullet_limit(self):
        # Assuming bullet limit is 5
        for _ in range(6): # Try to fire 6 bullets
            self.game.player.fire_bullet()
        # Verify that bullet count does not exceed 5
        self.assertEqual(len(self.game.bullets), 5)

    def test_bullet_removal_after_hit(self):
        # Setup an enemy at a specific position
        enemy_position = (400, 300)
        self.game.enemies.append(Enemy(position=enemy_position))
        # Fire a bullet towards the enemy
        self.game.player.position = 400 # Align player with enemy
        self.game.player.fire_bullet()
        # Simulate game loop until bullet hits enemy
        while len(self.game.enemies) > 0:
            self.game.update_game_state()
        # Verify that the enemy has been removed
        self.assertEqual(len(self.game.enemies), 0)

if __name__ == '__main__':
    unittest.main()
