"""
Transforming an Algorithm into a Python Program
Module: Algorithms and Problem Solving using Python
Degree: BSc Computer Science and Digitization

Description:
  Accepts three numbers from the user, finds the minimum using Python's
  built-in min() function, and displays the result inside a coloured
  circle using the Turtle graphics module.

Features:
  - User input handling with float conversion
  - Minimum value detection using min()
  - Turtle graphics visualisation (light blue circle, black border)
  - Error handling with try/except for invalid inputs
"""

import turtle


def get_user_inputs():
    """
    Prompt the user to enter three numbers.
    Returns a tuple (x, y, z) as floats.
    Raises ValueError if input is non-numeric.
    """
    x = float(input("Enter first number (X): "))
    y = float(input("Enter second number (Y): "))
    z = float(input("Enter third number (Z): "))
    return x, y, z


def find_minimum(x, y, z):
    """
    Find and return the minimum of three numbers using Python's min().
    """
    return min(x, y, z)


def draw_result(minimum_value):
    """
    Draw a light blue circle with a black border using Turtle graphics
    and display the minimum value at the centre.
    """
    screen = turtle.Screen()
    screen.title("Minimum Value Finder")
    screen.bgcolor("white")
    screen.setup(width=400, height=400)

    pen = turtle.Turtle()
    pen.speed(5)
    pen.hideturtle()

    # Draw filled circle
    pen.penup()
    pen.goto(0, -150)          # Position turtle so circle is centred
    pen.pendown()

    pen.color("black")
    pen.fillcolor("lightblue")
    pen.begin_fill()
    pen.circle(150)
    pen.end_fill()

    # Display minimum value at centre
    pen.penup()
    pen.goto(0, -20)

    # Format: show as integer if whole number, else show 1 decimal place
    if minimum_value == int(minimum_value):
        display_value = str(int(minimum_value))
    else:
        display_value = f"{minimum_value:.1f}"

    pen.write(
        f"Min: {display_value}",
        align="center",
        font=("Arial", 20, "bold")
    )

    turtle.done()


def main():
    """
    Main program flow:
    1. Get three numbers from the user
    2. Find the minimum value
    3. Display the result inside a circle using turtle graphics
    """
    try:
        x, y, z = get_user_inputs()
        minimum = find_minimum(x, y, z)
        print(f"\nThe minimum value is: {minimum}")
        draw_result(minimum)

    except ValueError:
        print("\nError: Please enter valid numeric values (integers or decimals).")


if __name__ == "__main__":
    main()
