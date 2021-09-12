from contextlib import contextmanager


@contextmanager
def context_manager_open_file(name, param):
    print(f'Work with {name} file!')
    f = open(name, param)
    try:
        yield f
    except RuntimeError:
        print('error: ', RuntimeError)
    finally:
        print(f'The {name} file is closed.')
        f.close()
