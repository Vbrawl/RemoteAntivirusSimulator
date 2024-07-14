from screen import Screen
import time

from scenes.connection import Connection

import random


if __name__ == "__main__":
    screen = Screen()
    con = Connection()
    con.run(screen)
