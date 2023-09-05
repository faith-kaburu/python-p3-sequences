def print_fibonacci(length):
    first_numbers = [0, 1]

    if length == 0:
        print([])
    elif length == 1:
        print([0])
    elif length == 2:
        print(first_numbers)
    else:
        for i in range(2, length):
            first_numbers.append(first_numbers[i - 1] + first_numbers[i - 2])
        print(first_numbers)