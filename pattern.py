def number_pattern(n):

    numbers = []
    for number in number_pattern:
        numbers = n.range()


        


        if not isinstance(n,int):
            return 'Argument must be an integer value'

        if n < 1:
            return 'Argument must be an integer greater than 0'


print(number_pattern(4))
print(number_pattern(12))