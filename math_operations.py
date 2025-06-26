def basic_math(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else "Cannot divide by zero"
    modulus = a % b if b != 0 else "Cannot compute modulus with zero"
    floor_division = a // b if b != 0 else "Cannot compute floor division with zero"
    
    return {
        "addition": f"{addition:.2f}",
        "subtraction": f"{subtraction:.2f}",
        "multiplication": f"{multiplication:.2f}",
        "division": division if isinstance(division, str) else f"{division:.2f}",
        "modulus": modulus if isinstance(modulus, str) else f"{modulus:.2f}",
        "floor_division": floor_division if isinstance(floor_division, str) else f"{floor_division:.2f}"
    }

if __name__ == "__main__":
    num1 = 10
    num2 = 5
    results = basic_math(num1, num2)
    print(f"Number 1: {num1}")
    print(f"Number 2: {num2}")
    print(f"Results: {results}")