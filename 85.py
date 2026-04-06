#command line utility in python
import argparse

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def main():
    parser = argparse.ArgumentParser(
        description="Simple CLI Calculator"
    )

    # Positional arguments
    parser.add_argument("num1", type=float, help="First number")
    parser.add_argument("num2", type=float, help="Second number")

    # Optional argument (operation)
    parser.add_argument(
        "--operation", "-op",
        choices=["add", "sub", "mul", "div"],
        required=True,
        help="Operation to perform"
    )

    args = parser.parse_args()

    if args.operation == "add":
        result = add(args.num1, args.num2)
    elif args.operation == "sub":
        result = subtract(args.num1, args.num2)
    elif args.operation == "mul":
        result = multiply(args.num1, args.num2)
    elif args.operation == "div":
        result = divide(args.num1, args.num2)

    print("Result:", result)

if __name__ == "__main__":
    main()
