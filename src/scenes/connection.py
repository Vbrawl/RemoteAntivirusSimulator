from scene import Scene
from screen import Screen
import random
import time


class Connection(Scene):
    def run(self, screen: Screen):
        screen.log("Connecting through cable")
        messages = ["Cable found!", "Endpoint found!", "Connected!"]
        process_handle = screen.processing(len(messages), "Connecting through cable")

        for i in range(len(messages)):
            process_handle.update(0)
            for _ in range(random.randint(1, 3)):
                time.sleep(1)
                process_handle.update(0)
            process_handle.clear()
            screen.success(messages[i])
            process_handle.update(1)
            process_handle.refresh()
        time.sleep(2)
        process_handle.close()
