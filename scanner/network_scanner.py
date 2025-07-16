import subprocess
from typing import List, Dict


def get_arp_table() -> List[Dict[str, str]]:
    result = subprocess.run(["arp", "-a"], capture_output=True, text=True, shell=True)
    devices = []

    for line in result.stdout.splitlines():
        if "-" in line or "Interface:" in line or line.strip() == "":
            continue
        parts = line.split()
        if len(parts) >= 2:
            devices.append(
                {
                    "ip": parts[0],
                    "mac": parts[1],
                    "type": parts[2] if len(parts) > 2 else "unknown",
                }
            )
    return devices
