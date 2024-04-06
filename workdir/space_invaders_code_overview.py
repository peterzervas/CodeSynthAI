# Space Invaders Game Code Overview

## Player Movement
- The player should be able to move left and right within the boundaries of the game screen.
- There should be a limit to how far the player can move in either direction.

## Bullet Firing
- The player can fire a bullet to destroy enemies.
- There should be a limit on the number of bullets on the screen at any one time.
- Bullets that hit enemies should remove the enemy from the game.

## Game Loop
- The game loop continuously updates the game state, including player position, bullet positions, and enemy positions.
- The game loop should handle collisions between bullets and enemies.
- The game should end when all enemies are destroyed or the player is hit by an enemy.

# Test Cases to Develop
1. Test player movement within screen boundaries.
2. Test player cannot move beyond screen boundaries.
3. Test bullet firing mechanism.
4. Test bullet limit on the screen.
5. Test collision detection between bullet and enemies.
6. Test game loop updates game state correctly.
7. Test game ends correctly when all enemies are destroyed or player is hit.