from typing import Any
from screen import Screen
from plot import Plot
from scenes.preparing import Preparing
from scenes.connection import Connection
from scenes.malware_scan import MalwareScan
from scenes.generating_report import GeneratingReport


if __name__ == "__main__":
    screen = Screen()

    scan_modes = {
        "Quick Scan": {
            "MalwareScan": {},
            "GeneratingReport": {
                "filepath": "Report.docx"
            }
        },
        "Full Scan": {
            "MalwareScan": {
                "execution_time": 8 * 60,
                "scan_multiplier": 0.05,
                "maximum_scan_duration": 10,
                "minimum_scan_duration": 0.05
            },
            "GeneratingReport": {
                "filepath": "Report.docx"
            }
        }
    }

    mode_index = screen.menu("Remote Antivirus", list(scan_modes.keys()))
    mode = scan_modes[mode_index]

    # noinspection PyBroadException
    try:
        plot = Plot([
            Preparing(mode_index),
            Connection(),
            MalwareScan(**(mode["MalwareScan"])),
            GeneratingReport(**(mode["GeneratingReport"]))
        ])
        plot.runAll(screen)
    except Exception as e:
        screen.error("An unexpected error happened!")
