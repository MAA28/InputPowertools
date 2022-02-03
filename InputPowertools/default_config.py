from colorama import Fore

default_config = {
    'add space after question': True,
    'number of allowed errors': 10,
    'color schema': {
        'error': Fore.RED,
        'question': {
            'normal': Fore.GREEN,
            'option': Fore.YELLOW
        },
        'options': {
            'index': Fore.CYAN,
            'answer': Fore.BLUE
        }
    }
}
