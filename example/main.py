from src.InputPowertools import input, Mode
from src.InputPowertools import cli


def test_cli(a, b: str, c: list, d: bool = False):
    """
    Some function


    :param a: Is a variable called a
    :param b: Is a variable called b
    :param c: Is a variable called c
    :param d: Is a variable called d
    :return: Some really interesting thing
    """
    print(f'{a=} {b=} {c=} {d=}')


def test_input():
    print(f"Result: {input('Type your name:', Mode.ALPHA, default='Hannes')}")
    print(f"Result: {input('How old are you:', Mode.NUMERIC, confirm=True, domain=lambda x: x % 1 == 0)}")
    print(f"Result: {input('Are you a what kind of person are you?', Mode.OPTIONS, options=['Cat person', 'Dog person', 'Bird person'])}")


if __name__ == '__main__':
    cli.run(test_cli) # run python main.py --a lol --b "this is a value with spaces" --c 4 2 "test123" --d
    test_input()
