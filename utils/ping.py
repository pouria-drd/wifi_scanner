import platform
import subprocess


def ping(ip: str, timeout: int = 2000) -> bool:
    """
    Ping an IP address.
    Returns True if host responds, False otherwise.
    `timeout` is in milliseconds.
    """
    param = "-n" if platform.system().lower() == "windows" else "-c"
    timeout_param = "-w" if platform.system().lower() == "windows" else "-W"

    command = ["ping", param, "1", timeout_param, str(timeout), ip]

    try:
        output = subprocess.run(
            command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
        return output.returncode == 0
    except Exception:
        return False
