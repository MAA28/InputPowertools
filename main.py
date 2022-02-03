from InputPowertools import input, Input


def main():
    print(f"Result: {input('Type your name:', Input.ALPHA)}")
    print(f"Result: {input('How old are you:', Input.NUMERIC, domain=lambda x: x % 1 == 0)}")
    print(f"Result: {input('Are you a what kind of person are you?', Input.OPTIONS, options=['Cat person', 'Dog person'])}")
    # print("HI\x08\x08")


if __name__ == '__main__':
    main()
