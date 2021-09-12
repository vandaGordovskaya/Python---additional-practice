from myIterator import MyIterator
from decorator import func_decorator, p_of_rectangle
from generator import countup_generator, generator_obj
from contextManager import context_manager_open_file


def main():
    print("_" * 10)

    # Example of using class as Iterator
    my_iter = MyIterator(4)
    print("It's my Iterator:")
    for i in my_iter:
        print(i)
    print("_" * 10)

    # Example of using Context Manager
    print("It's my Context Manager:")
    with context_manager_open_file("testFile.txt", "a") as file:
        file.write('Hello World \n')

    with context_manager_open_file("testFile.txt", "r") as file:
        print(file.read())
    print("_" * 10)

    # Example of using Generator
    print("It's my function Generator:")
    print(countup_generator(4))
    calc = 1
    for i in countup_generator(4):
        print(f'The calculation #{calc} = {i}')
        calc += 1
    print("_" * 10)

    print("It's my one-line Generator:")
    print(generator_obj)
    char_num = 1
    for val in generator_obj:
        print(f'Getting symbol #{char_num} = {val}')
        char_num += 1
    print("_" * 10)


if __name__ == '__main__':
    main()
