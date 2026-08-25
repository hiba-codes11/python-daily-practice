def number_pattern(n):

    # 1. Validate
    if not isinstance(n, int):
        return 'Argument must be an integer value.'

    if n < 1:
        return 'Argument must be an integer greater than 0.'

    # 2. Create an empty list
    numbers = []

    # 3. Loop from 1 to n
    for number in range(1, n + 1):

        # 4. Add each number as a string
        numbers.append(str(number))

    # 5. Join them with spaces
    return ' '.join(numbers)

print(number_pattern(4))
print(number_pattern(12))

#   INPUT
#     ↓
#   VALID?
#     ↓
#    YES → continue
#    NO  → return error