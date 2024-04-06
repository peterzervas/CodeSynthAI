
import unittest
from space_invaders import Game

class TestPlayerMovement(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_player_moves_within_boundaries(self):
        # Assuming screen width is 800 pixels and player starts at 400 (center)
        self.game.player.position = 400
        self.game.player.move('left', 50) # Move player left by 50 pixels
        self.assertEqual(self.game.player.position, 350)
        self.game.player.move('right', 100) # Move player right by 100 pixels
        self.assertEqual(self.game.player.position, 450)

    def test_player_cannot_move_beyond_boundaries(self):
        # Assuming screen width is 800 pixels
        self.game.player.position = 0
        self.game.player.move('left', 10) # Attempt to move player left beyond boundary
        self.assertEqual(self.game.player.position, 0) # Position should not change
        self.game.player.position = 800
        self.game.player.move('right', 10) # Attempt to move player right beyond boundary
        self.assertEqual(self.game.player.position, 800) # Position should not change

if __name__ == '__main__':
    unittest.main()
