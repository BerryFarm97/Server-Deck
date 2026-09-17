import subprocess
from enum import Enum

TIMEOUT = 180


class ShutdownStatus(Enum):
    ALREADY_OFFLINE = "server already not running"
    CLEAN = "shutdown cleanly"
    INVALID_INPUT = "User input is not valid"
    SERVER_LONG_SHUTDOWN = "server still shutting down after timeout"


def start_server(java_executable, server_jar, server_directory):
    # Recieves the java exec path, server JAR path, and server folder path.
    # Launches the server and returns a process object while running.
    return subprocess.Popen(
        [java_executable, "-jar", server_jar, "nogui"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        cwd=server_directory,
        text=True,
    )


def server_shutdown(live_process, user_input):
    if live_process.poll() is not None:
        return ShutdownStatus.ALREADY_OFFLINE

    if not user_input.lower().strip() == "stop":
        return ShutdownStatus.INVALID_INPUT

    if user_input.lower().strip() == "stop":
        live_process.stdin.write("stop\n")
        live_process.stdin.flush()
        live_process.stdin.close()

        try:
            live_process.wait(timeout=TIMEOUT)
        except subprocess.TimeoutExpired:
            return ShutdownStatus.SERVER_LONG_SHUTDOWN

    if live_process.returncode == 0:
        return ShutdownStatus.CLEAN


def server_data_output(server_data):
    while True:
        current_line = server_data.stdout.readline()

        if current_line != "":
            print(current_line, end="")
        else:
            return
