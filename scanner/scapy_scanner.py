import re
import scapy.all as scapy
from utils import get_hostname
from rich.console import Console


console = Console()



import scapy.all as scapy
import socket
import re
from rich.console import Console

console = Console()

def scapy_scan(ip_range: str):
    ip_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]+$")
    if not ip_pattern.match(ip_range):
        console.print(f"[red]Invalid IP range: {ip_range}[/red]")
        return []

    try:
        answered, _ = scapy.arping(ip_range, verbose=False)
    except Exception as e:
        console.print(f"[red]ARP Scan Error: {e}[/red]")
        return []

    devices = []
    for _, recv in answered:
        ip = recv.psrc
        mac = recv.hwsrc
        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except:
            hostname = "Unknown"
        devices.append({"ip": ip, "mac": mac, "hostname": hostname})
    return devices


def scapy_scan(ip_range: str):
    """
    Scan the network using ARP requests via scapy.
    The ip_range must be in CIDR format, e.g., "192.168.1.0/24".
    Returns a list of dictionaries with 'ip' and 'mac'.
    """
    ip_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]+$")
    if not ip_pattern.match(ip_range):
        console.print(
            f"[red]Invalid IP range: {ip_range}. Please use CIDR format like 192.168.1.0/24[/red]"
        )
        return []

    # console.print(f"📡 Starting ARP scan on IP range: [cyan]{ip_range}[/cyan]")

    try:
        answered, _ = scapy.arping(ip_range, verbose=False)  # type: ignore
    except PermissionError:
        console.print(
            "[red]Error: Administrator/root privileges are required to run scapy ARP scan![/red]"
        )
        return []
    except Exception as e:
        console.print(f"[red]Error running scapy ARP scan: {e}[/red]")
        return []

    devices = []
    for sent_pkt, received_pkt in answered:
        ip = received_pkt.psrc
        mac = received_pkt.hwsrc
        hostname = get_hostname(ip)

        devices.append(
            {
                "ip": ip,
                "mac": mac,
                "hostname": hostname,
            }
        )
    return devices
