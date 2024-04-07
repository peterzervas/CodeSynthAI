import turtle
import koch_curve_snowflake

# Test case 1: Default parameters
try:
    turtle.reset()
    koch_curve_snowflake.koch_curve_snowflake(turtle.Turtle(), 4, 300)
    print('Test case 1 passed')
except Exception as e:
    print('Test case 1 failed:', str(e))

# Test case 2: Edge case with order 0
try:
    turtle.reset()
    koch_curve_snowflake.koch_curve_snowflake(turtle.Turtle(), 0, 300)
    print('Test case 2 passed')
except Exception as e:
    print('Test case 2 failed:', str(e))

# Test case 3: Large order (potential performance issue)
try:
    turtle.reset()
    koch_curve_snowflake.koch_curve_snowflake(turtle.Turtle(), 6, 300)
    print('Test case 3 passed')
except Exception as e:
    print('Test case 3 failed:', str(e))

# Test case 4: Negative size (invalid input)
try:
    turtle.reset()
    koch_curve_snowflake.koch_curve_snowflake(turtle.Turtle(), 4, -300)
    print('Test case 4 passed')
except Exception as e:
    print('Test case 4 failed:', str(e))

# Test case 5: Negative order (invalid input)
try:
    turtle.reset()
    koch_curve_snowflake.koch_curve_snowflake(turtle.Turtle(), -1, 300)
    print('Test case 5 passed')
except Exception as e:
    print('Test case 5 failed:', str(e))

# Ensure turtle window closes after tests
turtle.bye()
