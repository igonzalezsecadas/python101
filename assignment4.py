# ASSIGNMENT 4: SPAGHETTI TO REFACTOR
# Objective: Modularize this mess!
import math


def main():
    print("--- WELCOME TO THE GEOMETRY TOOL ---")
    shape = input("Enter shape (circle or rectangle): ").lower()
    match shape:
        case "rectangle":
            height, width = rectangle_input()
            rectangle = calculate_rectangle(height, width)
            print(f"Area: {rectangle[0]} | Perimeter: {rectangle[1]}")
        case "circle":
            radius = circle_input()
            circle = calculate_circle(radius)
            print(f"Area: {circle[0]} | Perimeter: {circle[1]}")


def calculate_circle(radius: float) -> tuple[float, float]:
    area = float(math.pi * (radius ** 2))
    perimeter = float(2 * math.pi * radius)
    return area, perimeter


def calculate_rectangle(height: float, width: float) -> tuple[float, float]:
    area = height * width
    perimeter = height * 2 + width * 2
    return area, perimeter


def rectangle_input() -> tuple[float, float]:
    height = 0
    width = 0
    while height <= 0 or width <= 0:
        try:
            height = float(input("Enter the height: "))
            width = float(input("Enter the width: "))
            if height <= 0 or width <= 0:
                raise UserWarning("Height and width have to be positive")
        except ValueError as e:
            print("You have to input numbers for height and width")
        except UserWarning as e:
            print(e)

    return height, width


def circle_input() -> float:
    radius = 0
    while radius <= 0:
        try:
            radius = float(input("Enter the radius: "))
            if radius <= 0:
                raise UserWarning("Radius has to be positive")
        except ValueError as e:
            print("You have to input a number for the radius")
        except UserWarning as e:
            print(e)
    return radius


if __name__ == "__main__":
    main()