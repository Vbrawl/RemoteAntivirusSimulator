from screen import Screen
from plot import Plot
from scenes.connection import Connection


if __name__ == "__main__":
    screen = Screen()
    plot = Plot([
        Connection()
    ])
    plot.runAll(screen)
