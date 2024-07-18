from scene import Scene
from screen import Screen
import subprocess
import random
import time
import sys
import os


class GeneratingReport(Scene):
    def __init__(self, filepath: str):
        self.filepath = filepath

    def run(self, screen: Screen):
        screen.log(f"Generating \"{self.filepath}\"...")
        screen.warning("This may take some time")

        delay = random.randint(10, 30)
        waiting = 0
        processing_handle = screen.processing(100, "Generating Report")
        while delay > waiting:
            step = random.randint(2, 5)
            time.sleep(step)
            waiting += step
            processing_handle.n = min(int(waiting / delay * 100), 100)
            processing_handle.update(0)
        processing_handle.close()

        screen.success(f"Report generated at {self.filepath}")
        time.sleep(1)

        if sys.platform == "win32":
            os.startfile(self.filepath)
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, self.filepath])
