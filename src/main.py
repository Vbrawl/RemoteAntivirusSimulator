from screen import Screen
from plot import Plot
from scenes.connection import Connection
from scenes.malware_scan import MalwareScan


if __name__ == "__main__":
    screen = Screen()

    plot = Plot([
        Connection(),
        MalwareScan()
    ])
    plot.runAll(screen)
