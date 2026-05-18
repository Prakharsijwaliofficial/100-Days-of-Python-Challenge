"""
Day 13 of 100 Days of Code Challenge.
This script contains three classic coding exercises:
1. Odd or Even Checker
2. Leap Year Validator
3. FizzBuzz Game
"""

def odd_or_even(number):
    """Checks if a given number is odd or even."""
    if number % 2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."


def is_leap(year):
    """Determines whether a given year is a leap year."""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def fizz_buzz(target):
    """Counts up to a target number, printing Fizz, Buzz, or FizzBuzz."""
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)


def main():
    """Interactive CLI menu to run any of the day's functions."""
    print("--- Day 13 Challenge Dashboard ---")
    print("1. Run Odd or Even Checker")
    print("2. Run Leap Year Validator")
    print("3. Run FizzBuzz")
    
    choice = input("\nChoose a challenge to test (1-3): ")
    
    if choice == "1":
        num = int(input("Enter a number to check: "))
        print(odd_or_even(num))
        
    elif choice == "2":
        yr = int(input("Enter a year to check: "))
        if is_leap(yr):
            print(f"{yr} is a leap year!")
        else:
            print(f"{yr} is NOT a leap year.")
            
    elif choice == "3":
        limit = int(input("Enter target number for FizzBuzz: "))
        fizz_buzz(limit)
        
    else:
        print("Invalid option selected.")

if __name__ == "__main__":
    main()
