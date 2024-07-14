from screen import Screen
import time

import random


if __name__ == "__main__":
    screen = Screen()
    handle = screen.processing(description="Hello World")
    for i in handle:
        for _ in range(random.randint(1, 10)):
            handle.update(0)
            time.sleep(0.5)
