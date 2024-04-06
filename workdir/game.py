def move_up(position):
    x, y = position
    return (x, y+1)

# Test Scenario
initial_position = (0, 0)
new_position = move_up(initial_position)
print(new_position)