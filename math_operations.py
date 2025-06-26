def basic_math(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else "Cannot divide by zero"
    modulus = a % b if b != 0 else "Cannot compute modulus with zero"
    square_a = a ** 2
    
    return {
        "addition": addition,
        "subtraction": subtraction,
        "multiplication": multiplication,
        "division": division,
        "modulus": modulus,
        "square_a": square_a
    }

if __name__ == "__main__":
    num1 = 10
    num2 = 5
    results = basic_math(num1, num2)
    print(f"Number 1: {num1}")
    print(f"Number 2: {num2}")
    print(f"Results: {results}")