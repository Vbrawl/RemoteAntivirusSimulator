from colorama import Fore


class Screen:
    def __init__(self, error_color: str = Fore.RED,
                 warning_color: str = Fore.YELLOW,
                 success_color: str = Fore.GREEN):
        self.error_color = error_color
        self.warning_color = warning_color
        self.success_color = success_color

    @staticmethod
    def log(*args, **kwargs):
        print(Fore.RESET, *args, **kwargs)

    def error(self, *args, **kwargs):
        print(self.error_color, '[-]', *args, **kwargs)

    def warning(self, *args, **kwargs):
        print(self.warning_color, *args, **kwargs)

    def success(self, *args, **kwargs):
        print(self.success_color, '[+]', *args, **kwargs)

    @staticmethod
    def processing(*args, **kwargs):
        print(Fore.RESET, '[*]', *args, **kwargs)
