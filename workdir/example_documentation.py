"""Example module to demonstrate documentation in Python.

This module contains an example of how to document classes and functions using docstrings.
"""

class Enemy:
    """Represents an enemy in a game.

    Attributes:
        name (str): The name of the enemy.
        health (int): The health points of the enemy.

    """
    def __init__(self, name, health):
        """Initialize a new enemy with a name and health.

        Args:
            name (str): The name of the enemy.
            health (int): The health points of the enemy.
        """
        self.name = name
        self.health = health

    def take_damage(self, damage):
        """Reduces the enemy's health by the damage amount.

        Args:
            damage (int): The amount of damage to inflict.
        """
        self.health -= damage

# Example of a function outside a class
def calculate_score(points):
    """Calculates and returns the score based on points.

    Args:
        points (int): The points earned.

    Returns:
        int: The calculated score.
    """
    return points * 10
