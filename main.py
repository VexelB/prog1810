"""
Лабораторная работа 18.10
Войтин Е.В.
"""


def main(*args):
    return sorted(args)


print(main(1, 8, 3, 5, 7, 1.5))

if __name__ == '__main__':
    assert main(3, 1, 2) == [1, 2, 3], "Что-то неверно"
