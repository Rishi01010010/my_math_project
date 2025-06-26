def basic_math(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return "Inputs must be numbers"
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else "Cannot divide by zero"
    modulus = a % b if b != 0 else "Cannot compute modulus with zero"
    power = a ** b
    
    return {
        "addition": addition,
        "subtraction": subtraction,
        "multiplication": multiplication,
        "division": division,
        "modulus": modulus,
        "power": power
    }

if __name__ == "__main__":
    num1 = 10
    num2 = 5
    results = basic_math(num1, num2)
    print(f"Number 1: {num1}")
    print(f"Number 2: {num2}")
    print(f"Results: {results}")