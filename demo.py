def print_three_things(first, second, third):
    print(first)
    print(second)
    print(third)


print_three_things(1, 2, 3)


def demo_args(*args):
    print(args)


demo_args(1)  # output (1)
demo_args(2, 3, 4, 2)  # output (2, 3, 4, 2)


def demo_kwargs(**kwargs):
    print(kwargs)


demo_kwargs(a=1, b=2, c=3)  # output {a = 1, b = 2, c = 3}
demo_kwargs()  # output {}


def print_three_things(a, b, c):
    print(a)
    print(b)
    print(c)


three_things = [1, 2, 3]
print_three_things(*three_things)  # output 1 2 3


def print_two_things_with_kwargs(first_param=1, second_param=2):
    print(first_param)
    print(second_param)


two_things = {'first_param': 1000, 'second_param': 2000}
print_two_things_with_kwargs(**two_things)  # output 1000 2000
