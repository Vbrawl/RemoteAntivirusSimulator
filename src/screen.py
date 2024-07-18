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

    def menu(self, title: str, entries: list[str] = None):
        print(Fore.RED + title, Fore.RESET)
        for i, entry in enumerate(entries):
            print(f'{Fore.GREEN}{i}.{Fore.RESET}{entry}')
        print(Fore.GREEN + "Please select an entry")

        valid_selections = range(0, len(entries))
        selection = self.input_int(valid_selections, ": ")
        while selection is None:
            print(f"{Fore.RED}Only an integer between {valid_selections.start} and {valid_selections.stop}"
                  f" are valid!{Fore.GREEN}")
            selection = self.input_int(valid_selections, ": ")
        return selection

    @staticmethod
    def input_int(valid_range: range, prompt: str = '') -> int | None:
        selection = input(prompt)
        if not selection.isnumeric():
            return None

        selection = int(selection)
        if selection not in valid_range:
            return None
        return selection

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
        return tqdm(total=steps, desc=self.processing_color + description, leave=False)
