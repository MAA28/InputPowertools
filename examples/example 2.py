from src.InputPowertools import input, Mode


def test_input():
    print(f"Result: {input('Type your name:', Mode.ALPHA, default='Hannes')}")
    print(f"Result: {input('How old are you:', Mode.NUMERIC, confirm=True, domain=lambda x: x % 1 == 0)}")
    print(f"Result: {input('Are you a what kind of person are you?', Mode.OPTIONS, options=['Cat person', 'Dog person', 'Bird person'])}")


if __name__ == '__main__':
    test_input()
