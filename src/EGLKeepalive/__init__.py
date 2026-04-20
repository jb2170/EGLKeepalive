"""
Keep a GPU from sleeping by nudging an EGL context
""".removeprefix("\n")

__version__ = "0.0.1"

import time
import signal
import argparse

import moderngl as mgl

def get_cli_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description = __doc__)

    parser.add_argument("delay_s", metavar = "DELAY", nargs = "?", type = float, default = 1.0)

    args = parser.parse_args()

    return args

def on_sigterm(*args):
    raise KeyboardInterrupt

def main() -> None:
    args = get_cli_args()

    delay_s: float = args.delay_s

    signal.signal(signal.SIGTERM, on_sigterm)

    print("Acquiring standalone EGL context...", end = " ", flush = True)
    gl = mgl.create_context(standalone = True, backend = "egl")
    print("Ready")

    keepalive_buffer = gl.buffer(reserve = 256)

    try:
        print("Idling")
        while True:
            keepalive_buffer.read()
            gl.finish()
            time.sleep(delay_s)
    except KeyboardInterrupt:
        print("Shutting down")

    gl.release()
