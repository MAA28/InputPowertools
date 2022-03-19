from typing import List

from src.InputPowertools import cli


def test_cli(a, b: str, c: List[str], d: bool = False):
    """
    Some function


    :param a: Is a variable called a
    :param b: Is a variable called b
    :param c: Is a variable called c
    :param d: Is a variable called d
    :return: Some fascinating thing
    """
    print(f'{a=} {b=} {c=} {d=}')


if __name__ == '__main__':
    cli.run(test_cli)  # run python cli.py --a lol --b "this is a value with spaces" --c 4 2 "test123" --d