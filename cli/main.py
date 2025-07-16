import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from rich.table import Table
from rich.console import Console
from scanner.vendor_lookup import get_vendor
from scanner.network_scanner import get_arp_table


def main():
    console = Console()
    console.print("[bold green]🔍 Wi-Fi Device Scanner[/bold green]")

    devices = get_arp_table()

    table = Table(title="Connected Devices")
    table.add_column("IP", style="cyan")
    table.add_column("MAC", style="magenta")
    table.add_column("Vendor", style="green")

    for device in devices:
        mac = device["mac"]
        vendor = get_vendor(mac)
        table.add_row(device["ip"], mac, vendor)

    console.print(table)


if __name__ == "__main__":
    main()
