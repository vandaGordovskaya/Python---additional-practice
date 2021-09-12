def func_decorator(function):

    print(f'Your figure is rectangle 5x4.')
    function()
    print('* ' * 5)
    print('* ' + '      ' + '*')
    print('* ' + '      ' + '*')
    print('* ' * 5)


def p_of_rectangle():
    p = 5 * 4
    print(f'Perimeter of rectangle 5x4 is {p}.')


func_decorator(p_of_rectangle)
