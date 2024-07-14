from screen import Screen


class Scene:
    def run(self, screen: Screen):
        raise NotImplementedError(f"{self.__class__.__qualname__}.run")
