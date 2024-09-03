def print_diamond(n):
    # Upper part of the diamond
    for i in range(1, n + 1):
        # Print spaces
        print(' ' * (n - i), end='')
        # Print numbers
        for j in range(1, i + 1):
            print(j, end=' ')
        print()

    # Lower part of the diamond
    for i in range(n - 1, 0, -1):
        # Print spaces
        print(' ' * (n - i), end='')
        # Print numbers
        for j in range(1, i + 1):
            print(j, end=' ')
        print()

# Test the diamond pattern with n = 5
n = 5
print_diamond(n)
