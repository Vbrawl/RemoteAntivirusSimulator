from scene import Scene
from screen import Screen
import random
import time


class Preparing(Scene):
    def __init__(self, mode_name: str):
        self.mode_name = mode_name

    def run(self, screen: Screen):
        screen.log(f"Executing \"{self.mode_name}\"...")
        delay = random.random() * 1.5 + 0.5
        time.sleep(delay)
