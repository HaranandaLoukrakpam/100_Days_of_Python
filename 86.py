#walrus operator in python]
'''
It allows you to assign a value to a variable inside an expression, instead of doing it as a separate statement.
'''
def main():
    print("Enter numbers one by one (type 'done' to finish):")

    numbers = []

    # Using walrus in while loop
    while (user_input := input(">> ")) != "done":
        
        # Validate input using walrus
        if (num := parse_number(user_input)) is not None:
            numbers.append(num)
        else:
            print("Invalid input, please enter a number.")

    if not numbers:
        print("No valid numbers entered.")
        return

    # Using walrus to avoid recomputation
    if (count := len(numbers)) > 0:
        total = sum(numbers)
        average = total / count

    # Using walrus in list comprehension
    squared_filtered = [sq for n in numbers if (sq := n**2) > 10]

    print("\n--- Results ---")
    print(f"Numbers entered: {numbers}")
    print(f"Count: {count}")
    print(f"Sum: {total}")
    print(f"Average: {average:.2f}")
    print(f"Squares > 10: {squared_filtered}")


def parse_number(value):
    """Try converting input to float"""
    try:
        return float(value)
    except ValueError:
        return None


if __name__ == "__main__":
    main()
