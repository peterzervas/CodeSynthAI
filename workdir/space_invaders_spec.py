# Space Invaders Clone Technical Specifications

## Core Functionalities

1. **Player Movement**: The player should be able to move left and right along the bottom of the screen. This can be achieved using keyboard inputs (e.g., arrow keys).

2. **Shooting Mechanism**: The player should be able to shoot bullets upwards towards the enemies by pressing a specific key (e.g., spacebar). The bullets will travel vertically up the screen.

3. **Enemy Movement**: A group of enemies will move horizontally across the screen, dropping down and reversing direction upon hitting the screen's edge. This simulates the classic space invaders enemy movement pattern.

4. **Scoring System**: Players will earn points for each enemy they successfully destroy. The score should be displayed on the screen.

## Technical Considerations

- **Python Version**: Use the latest stable version of Python for compatibility and performance reasons.
- **Graphics**: Since external assets are not allowed, use Python's built-in `turtle` module for simple graphics and animations.
- **Game Loop**: Implement a main game loop that continuously updates the game state, checks for user inputs, and redraws the screen.

## Project Structure

- `main.py`: The entry point of the game. Initializes the game and contains the main game loop.
- `player.py`: Defines the player's behavior, including movement and shooting.
- `enemy.py`: Defines the enemy's behavior and movement patterns.
- `bullet.py`: Handles the shooting mechanism and bullet movement.
- `scoreboard.py`: Manages the scoring system and displays the score on the screen.

This specification outlines the basic structure and functionalities required for the simple space invaders clone. Further details and adjustments can be made during the development process based on technical feasibility and user feedback.