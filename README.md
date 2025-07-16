# Wi-Fi Device Scanner (CLI)

A Python tool to scan and list all devices connected to the current Wi-Fi network. The program provides details such as IP address, MAC address, and vendor information, with future plans for hostname resolution and GUI integration.

## 🚀 Features

-   Scan local network for connected devices
-   Extract IP and MAC addresses using ARP
-   Identify device manufacturers (vendors) via MAC lookup
-   Colorful CLI output using `rich`
-   Clean code structure with modular design
-   Professional logging system

## 📦 Technologies Used

-   Python 3.x
-   subprocess, socket
-   rich
-   requests
-   Windows native tools (ARP)

## 📁 Project Structure

```
wifi_scanner/
├── scanner/
│   ├── network_scanner.py
│   ├── arp_scanner.py
│   └── vendor_lookup.py
├── cli/
│   └── main.py
├── utils/
│   ├── logger.py
│   └── network_tools.py
├── requirements.txt
└── README.md
```

## ✅ Requirements

-   Python 3.x
-   pip
-   Windows OS

## 🔧 Installation

```bash
git clone https://github.com/yourusername/wifi-scanner.git
cd wifi-scanner
pip install -r requirements.txt
```

## 🧪 Usage

```bash
python -m cli.main
```

> 💡 Tip: To improve detection, ping your subnet range before scanning:

```cmd
for /L %i in (1,1,254) do @ping -n 1 -w 1 192.168.1.%i > nul
```

## 📝 License

MIT License

## 🛠️ To-Do (Planned Improvements)

-   Add GUI

---

Crafted with ❤️ for developers who want full control over their network visibility.
