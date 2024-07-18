from scene import Scene
from screen import Screen
import time


class Preparing(Scene):
    def __init__(self, mode_name: str):
        self.mode_name = mode_name

    def run(self, screen: Screen):
        screen.log(f"Executing \"{self.mode_name}\"...")
        time.sleep(3)
