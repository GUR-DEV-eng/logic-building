def analyze_list(numbers):
    count = 0
    total = 0
    even = 0
    odd = 0

    # initialize largest and smallest
    largest = numbers[0]
    smallest = numbers[0]

    for num in numbers:
        count += 1
        total += num

        # check largest
        if num > largest:
            largest = num

        # check smallest
        if num < smallest:
            smallest = num

        # even or odd
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

    print("Count:", count)
    print("Sum:", total)
    print("Largest:", largest)
    print("Smallest:", smallest)
    print("Even:", even)
    print("Odd:", odd)


analyze_list([4, 17, 8, 3, 22, 11, 6, 99, 14, 5])