import re
import sys
import inspect
from colorama import Fore, Style
from docstring_parser import parse

default_config = {
    'color schema': {
        'short docstring': Fore.LIGHTGREEN_EX,
        'long docstring': Fore.GREEN,
        'return': Fore.LIGHTRED_EX,
        'command': Fore.BLUE,
        'description': Fore.MAGENTA,
        'key': Fore.CYAN,
        'type': Fore.RED,
        'default': Fore.YELLOW,
        'error': Fore.RED
    },
    'prefix': {
        'short description': '',
        'long description': ' ',
        'return': 'Return: ',
        'options': '\t',
        'option': '\t\t',
        'option description': '\t\t\t',
        'flags': '\t\t\t '
    }
}


def run(function: callable, config=None):
    if config is None:
        config = default_config

    function_parameters = inspect.signature(function).parameters

    if len(function_parameters) == 0:
        # function doesn't take any parameters, so I just run the function
        function()
    else:
        if len(sys.argv) == 1:
            print(f"For more information: {config['color schema']['command']}{sys.argv[0]} --help{Style.RESET_ALL}")
        elif sys.argv[1] == '--help':
            docstring = None
            if function.__doc__:
                docstring = parse(function.__doc__)
                print(config['prefix']['short description'] + config['color schema']['short docstring'] + docstring.short_description + Style.RESET_ALL)
                if docstring.long_description:
                    print(f"{config['prefix']['long description']}{config['color schema']['long docstring']} {docstring.long_description + Style.RESET_ALL}")
                if docstring.meta[-1].args[0] == 'return':
                    print(f"{config['prefix']['return']}{config['color schema']['return']}{docstring.meta[-1].description}{Style.RESET_ALL}")

            print(f"{config['prefix']['options']}Options:")
            print(f"{config['prefix']['option']}{config['color schema']['command']}--help{Style.RESET_ALL}")
            print(f"{config['prefix']['option description']}{config['color schema']['description']}Prints out information about the program.{Style.RESET_ALL}")
            print(f"{config['prefix']['flags']}{config['color schema']['key']}Type:    {config['color schema']['type']}bool{Style.RESET_ALL}")
            print(f"{config['prefix']['flags']}{config['color schema']['key']}Default: {config['color schema']['default']}False{Style.RESET_ALL}")

            parameter_descriptions = dict([
                (meta.args[1], meta.description)
                for meta in docstring.meta if meta.args[0] != 'return' and meta.description != ''
            ]) if docstring is not None else {}

            for key in function_parameters.keys():
                parameter = function_parameters[key]
                print(f"{config['prefix']['option']}{config['color schema']['command']}--{parameter.name}{Style.RESET_ALL}")

                if parameter.name in parameter_descriptions:
                    print(f"{config['prefix']['option description']}{config['color schema']['description']}{parameter_descriptions[parameter.name]}{Style.RESET_ALL}")

                if parameter.annotation.__name__ != '_empty':
                    print(f"{config['prefix']['flags']}{config['color schema']['key']}Type:    {config['color schema']['type'] + parameter.annotation.__name__}{Style.RESET_ALL}")

                if parameter.default != parameter.empty:
                    print(f"{config['prefix']['flags']}{config['color schema']['key']}Default: {config['color schema']['default']}{parameter.default}{Style.RESET_ALL}")
        else:
            # parse args
            parameters = dict([
                (
                    (split_parameter := parameter.split(' '))[0],
                    True if len(split_parameter) == 1 else
                    (
                        split_parameter[1] if len(split_parameter) == 2 else split_parameter[1:]
                    )
                )
                for parameter in ' '.join(sys.argv).split(' --')[1:] if parameter != ''
            ])
            for parameter in parameters:
                value = parameters[parameter]
                if isinstance(value, str):
                    if re.fullmatch(r'[+|-]?\d+(.\d+)?', value):
                        float_val = float(value)
                        if float_val % 1 == 0:
                            parameters[parameter] = int(float_val)
                            continue
                        parameters[parameter] = float_val

            # TODO: Parse str with space properly

            # do type check
            for key in parameters:
                if key not in function_parameters.keys():
                    raise KeyError(f'\'{key}\' is not requested!')

                parameter = function_parameters[key]

                if not (parameter.annotation.__name__ == "_empty" or isinstance(parameters[key], parameter.annotation)):
                    raise TypeError(f'{key} expected {parameter.annotation.__name__} but was given {parameters[key]}')

            function(**parameters)