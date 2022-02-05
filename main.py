from InputPowertools import input, cli, Mode


def test_cli(a, b: str, c: list, d: bool = False):
    print(f'{a=} {b=} {c=} {d=}')


def test_input():
    print(f"Result: {input('Type your name:', Mode.ALPHA)}")
    print(f"Result: {input('How old are you:', Mode.NUMERIC, domain=lambda x: x % 1 == 0)}")
    print(f"Result: {input('Are you a what kind of person are you?', Mode.OPTIONS, options=['Cat person', 'Dog person'])}")


if __name__ == '__main__':
    cli.run(test_cli)
