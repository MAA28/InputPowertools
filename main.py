from InputPowertools import input, Mode, cli


def main(a, d: bool, b: str, c: int = 2):
    """
    HI
    Iashuiahsufi
    :param a: Has some thing to do with art
    :param b:
    :param c: lol
    :return: Nothing
    """
    print(a, b * c)
    print(f"Result: {input('Type your name:', Mode.ALPHA)}")
    print(f"Result: {input('How old are you:', Mode.NUMERIC, domain=lambda x: x % 1 == 0)}")
    print(f"Result: {input('Are you a what kind of person are you?', Mode.OPTIONS, options=['Cat person', 'Dog person'])}")
    # print("HI\x08\x08")


if __name__ == '__main__':
    cli.run(main)
