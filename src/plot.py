from typing import Optional
from scene import Scene
from screen import Screen


class Plot:
    def __init__(self, scenes: Optional[list[Scene]] = None):
        self.scenes = scenes if scenes is not None else []

    def runAll(self, screen: Screen):
        for scene in self.scenes:
            scene.run(screen)
