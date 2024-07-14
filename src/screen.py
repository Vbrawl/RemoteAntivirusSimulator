from colorama import Fore
from tqdm import tqdm


class Screen:
    PROGRESS_MAX = 10

    def __init__(self, error_color: str = Fore.RED,
                 warning_color: str = Fore.YELLOW,
                 success_color: str = Fore.GREEN,
                 processing_color: str = Fore.BLUE):
        self.error_color = error_color
        self.warning_color = warning_color
        self.success_color = success_color
        self.processing_color = processing_color

    @staticmethod
    def log(*args, **kwargs):
        print(Fore.RESET, *args, **kwargs)

    def error(self, *args, **kwargs):
        print(self.error_color, '[-]', *args, **kwargs)

    def warning(self, *args, **kwargs):
        print(self.warning_color, *args, **kwargs)

    def success(self, *args, **kwargs):
        print(self.success_color, '[+]', *args, **kwargs)

    def processing(self, steps: int = PROGRESS_MAX, description: str = ""):
        return tqdm(range(steps), desc=self.processing_color + description)
