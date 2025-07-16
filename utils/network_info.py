import platform
import subprocess


def get_ssid() -> str:
    system = platform.system()

    try:
        if system == "Windows":
            result = subprocess.run(
                'netsh wlan show interfaces',
                capture_output=True, text=True, shell=True
            )
            for line in result.stdout.split('\n'):
                if 'SSID' in line and 'BSSID' not in line:
                    return line.split(':')[1].strip()

        elif system == "Linux":
            result = subprocess.run(
                'iwgetid -r',
                capture_output=True, text=True, shell=True
            )
            return result.stdout.strip()

        elif system == "Darwin":  # macOS
            result = subprocess.run(
                '/usr/sbin/networksetup -getairportnetwork en0',
                capture_output=True, text=True, shell=True
            )
            return result.stdout.strip().split(": ")[1]

    except Exception:
        pass

    return "Unknown"
