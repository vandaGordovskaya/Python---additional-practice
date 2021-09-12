def countup_generator(iterations):
    """ Generates a sum of nums.

    User provides number and function calculates the sum from 0 to final number(iterations).
    It's one type of Generator as Function

    """
    a = 0
    while a <= iterations:
        yield a
        a += 1


my_list = ['h', 'i', ' ', 'W', 'o', 'r', 'l', 'd']

generator_obj = (x for x in my_list)
