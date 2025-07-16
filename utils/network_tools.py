import platform
import threading
import subprocess


def ping_ip(ip: str):
    try:
        count = "1"
        command = (
            ["ping", "-n", count, ip]
            if platform.system() == "Windows"
            else ["ping", "-c", count, ip]
        )
        subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        pass


def ping_sweep(base_ip: str = "192.168.1", start: int = 1, end: int = 254):
    threads = []

    for i in range(start, end + 1):
        ip = f"{base_ip}.{i}"
        t = threading.Thread(target=ping_ip, args=(ip,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
