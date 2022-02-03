import re
from colorama import Style
from .default_config import default_config
from .Input import Input

std_input = input


def numeric_input_handler(question: str, domain: callable, config):
    for _ in range(config['number of allowed errors']):
        str_value = std_input(config['color schema']['question']['normal'] + question + Style.RESET_ALL + (
            ' ' if config['add space after question'] else ''))
        if re.fullmatch(r'[+|-]?\d+(.\d+)?', str_value):
            value = int(str_value) if not '.' in str_value else float(str_value)
            if domain(value):
                return value
            else:
                print(
                    f"{config['color schema']['error']}🛑 Please enter a value that fits the answers domain...{Style.RESET_ALL}")
        else:
            print(f"{config['color schema']['error']}🛑 Please enter a number...{Style.RESET_ALL}")
    print(
        f"{config['color schema']['error']}🛑 Terminated after {config['number f allowed errors']} errors! {Style.RESET_ALL}")
    return


# TODO: make it switchable with \x08 
def options_input_handler(question: str, options, config):
    print(config['color schema']['question']['normal'] + question + Style.RESET_ALL + (' ' if config['add space after question'] else ''))
    for i, option in enumerate(options):
        print(f"{config['color schema']['options']['index']}{i + 1}{Style.RESET_ALL} {'-' * int(len(str(len(options))) - len(str(i + 1)))}-> {config['color schema']['options']['answer']}{option}{Style.RESET_ALL}")

    option_config = config
    option_config['color schema']['question']['normal'] = option_config['color schema']['question']['option']
    index = input(f"Select option {config['color schema']['options']['index']}[1-{len(options)}]{Style.RESET_ALL}:", Input.NUMERIC, domain=lambda x: x in range(1, 1 + len(options)), config=option_config) - 1
    return options[index], index


def alpha_input_handler(question: str, config):
    for _ in range(config['number of allowed errors']):
        value = std_input(config['color schema']['question']['normal'] + question + Style.RESET_ALL + (
            ' ' if config['add space after question'] else ''))
        if value.isalpha():
            return value
        else:
            print(
                f"{config['color schema']['error']}🛑 Please enter a value that is completely alphabetic (no punctuation, numbers or emojis)...{Style.RESET_ALL}")
    print(
        f"{config['color schema']['error']}🛑 Terminated after {config['number f allowed errors']} errors! {Style.RESET_ALL}")
    return


def input(question: str, type: Input = Input.NORMAL, options=None, domain: callable = lambda x: True, config=None):
    # initialize config
    if config is None:
        config = default_config

    # for numeric
    if type == Input.NUMERIC:
        return numeric_input_handler(question, domain, config)

    # for options
    if type == Input.OPTIONS:
        return options_input_handler(question, options, config)

    # for alpha
    if type == Input.ALPHA:
        return alpha_input_handler(question, config)

    return std_input(config['color schema']['question']['normal'] + question + Style.RESET_ALL + (
        ' ' if config['add space after question'] else ''))
