# Function to analyze a list of numbers and calculate various statistics
# This function demonstrates the use of loops, conditionals, and basic arithmetic operations
def analyze_list(numbers):
    # Initialize counters and accumulators
    count = 0  # To count the total number of elements in the list
    total = 0  # To accumulate the sum of all numbers
    even = 0   # Counter for even numbers
    odd = 0    # Counter for odd numbers

    # Initialize largest and smallest with the first element of the list
    # This assumes the list is not empty; in a real application, you'd check for empty lists
    largest = numbers[0]
    smallest = numbers[0]

    # Loop through each number in the list to perform calculations
    for num in numbers:
        count += 1  # Increment the count for each number processed
        total += num  # Add the current number to the running total

        # Check if the current number is larger than the current largest
        if num > largest:
            largest = num  # Update largest if a bigger number is found

        # Check if the current number is smaller than the current smallest
        if num < smallest:
            smallest = num  # Update smallest if a smaller number is found

        # Determine if the number is even or odd using modulo operator
        if num % 2 == 0:
            even += 1  # Increment even counter
        else:
            odd += 1   # Increment odd counter

    # Display the calculated statistics
    print("Count:", count)      # Total number of elements
    print("Sum:", total)        # Sum of all numbers
    print("Largest:", largest)  # The largest number in the list
    print("Smallest:", smallest) # The smallest number in the list
    print("Even:", even)        # Count of even numbers
    print("Odd:", odd)          # Count of odd numbers


# Example usage: Analyze a sample list of numbers
# This demonstrates how to call the function with a list of integers
analyze_list([4, 17, 8, 3, 22, 11, 6, 99, 14, 5])