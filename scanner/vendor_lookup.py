import requests


def get_vendor(mac: str) -> str:
    try:
        response = requests.get(f"https://api.macvendors.com/{mac}", timeout=5)
        return response.text
    except Exception:
        return "Unknown"
