def calculate_rpn(input):
    numbers = []
    for i in input.split(' '):
        try:
            numbers.append(int(i))
        except ValueError:
            # operator
            if len(numbers) == 2:
                # sastify to do calculate
                result = eval('{}{}{}'.format(numbers[0], i, numbers[1]))
                numbers = [result]
            else:
                # dont know what to do with this
                raise ValueError('Input not correct')

    return numbers[0]

input = '12 1 * 5 -'

result = calculate_rpn(input)
print(result)
