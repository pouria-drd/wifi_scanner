import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Wi-Fi Device Scanner by Pouria Darandi",
        epilog="Example: python cli/main.py --range 192.168.1.0/24 --ping --output results.json"
    )

    parser.add_argument("-r", "--range", default="192.168.1.0/24", help="IP range to scan (CIDR)")
    parser.add_argument("-p", "--ping", action="store_true", help="Ping devices to check online status")
    parser.add_argument("-o", "--output", type=str, metavar="FILE", help="Save results to JSON file")

    return parser.parse_args()
