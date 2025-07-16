import json
from pathlib import Path
from datetime import datetime

def save_scan_to_json(devices: list, ip_range: str, output_path: str):
    """
    Save scan results to a structured JSON file.
    """
    data = {
        "scan_time": datetime.now().isoformat(),
        # "network_name": ssid,
        "ip_range": ip_range,
        "devices": devices,
    }

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"[✅] Results saved to: {output_path}")
