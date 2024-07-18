from typing import Any
from screen import Screen
from plot import Plot
from scenes.preparing import Preparing
from scenes.connection import Connection
from scenes.malware_scan import MalwareScan


if __name__ == "__main__":
    screen = Screen()

    # The dictionary holds parameters for the MalwareScan
    scan_modes:list[tuple[str, dict[str, Any]]] = [
        ("Quick Scan", {}),
        ("Full Scan", {
            "execution_time": 8 * 60,
            "scan_multiplier": 0.05,
            "maximum_scan_duration": 10,
            "minimum_scan_duration": 0.05
        })
    ]
    mode_index = screen.menu("Remote Antivirus", list(map(lambda x: x[0], scan_modes)))
    mode: tuple[str, dict[str, Any], dict[str, Any]] = scan_modes[mode_index]

    plot = Plot([
        Preparing(mode[0]),
        Connection(),
        MalwareScan(**mode[1])
    ])
    plot.runAll(screen)
