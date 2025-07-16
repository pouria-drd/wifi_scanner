import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from rich.console import Console
from rich.table import Table

from scanner import scapy_scan
from utils import ping, save_scan_to_json
from parse_arguments import parse_arguments


def main():
    console = Console()
    args = parse_arguments()

    console.print(f"[bold green]🔍 Wi-Fi Device Scanner By Pouria Darandi[/bold green]")
    console.print(f"📡 Starting scan on IP range: [cyan]{args.range}[/cyan]\n")

    devices = scapy_scan(args.range)

    for device in devices:
        device["online"] = "Yes" if args.ping and ping(device["ip"]) else "Unknown"

    table = Table(title="Connected Devices")
    table.add_column("IP", style="cyan")
    table.add_column("MAC", style="magenta")
    table.add_column("Hostname", style="green")
    table.add_column("Online", style="yellow")

    for d in devices:
        table.add_row(d["ip"], d["mac"], d.get("hostname", "Unknown"), d["online"])

    console.print(table)

    if args.output and args.output.endswith(".json"):
        save_scan_to_json(devices, args.range, args.output)


if __name__ == "__main__":
    main()
