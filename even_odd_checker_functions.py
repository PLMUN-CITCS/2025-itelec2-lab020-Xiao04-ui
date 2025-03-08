def get_integer_input() -> int:
    """
    Asks the user for an integer.
    Repeats until the user enters a valid integer.
    
    If the input is not a number, it shows an error and asks again.
    """
    while True:
        try:
            # Ask the user to enter an integer and try to convert the input
            return int(input("Enter an integer: "))
        except ValueError:
            # If the user doesn't enter a valid integer, prompt again
            print("Invalid input. Please enter a valid integer.")

def check_even_odd(number: int) -> str:
    """
    Determines if a given number is even or odd.
    
    This function checks if the number is divisible by 2 (even) or not (odd). 
    It uses the modulus operator (%) to perform this check.

    Args:
        number (int): The integer to check.
    
    Returns:
        str: A formatted string indicating whether the number is even or odd.
        Example: "5 is an Odd number."
    """
    # Check if the number is even or odd using modulus operator
    return f"{number} is an {'Even' if number % 2 == 0 else 'Odd'} number."

def main() -> None:
    """
    Main program flow to get input, check even/odd status, and display the result.
    """
    number = get_integer_input()  # Get valid integer input from the user
    result = check_even_odd(number)  # Determine if the number is even or odd
    print(result)  # Display the result to the user

if __name__ == "__main__":
    main()
