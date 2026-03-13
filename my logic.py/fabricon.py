# Palindrome Number Checker
# This program checks if a given number is a palindrome
# A palindrome number reads the same forwards and backwards (e.g., 121, 3443)

# Get user input and convert it to an integer
num = int(input("Enter a number: "))

# Store the original number for comparison later
original = num

# Initialize reverse to 0; this will store the reversed number
reverse = 0

# Use a while loop to reverse the number digit by digit
# Continue until num becomes 0 (no more digits to process)
while num > 0:
    # Extract the last digit of the number using modulo operator
    digit = num % 10

    # Build the reversed number by shifting digits left (multiplying by 10) and adding the new digit
    reverse = reverse * 10 + digit

    # Remove the last digit from the original number using integer division
    num = num // 10

# Compare the original number with the reversed number
if original == reverse:
    # If they are equal, it's a palindrome
    print("Palindrome number")
else:
    # If they are not equal, it's not a palindrome
    print("Not a palindrome number")