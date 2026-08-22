# Googlebot IP Ranges Repository

This repository provides an automated, machine-readable collection of official Googlebot IP address ranges (IPv4 and IPv6).

## 🚀 Purpose
To provide webmasters, firewall administrators, and security engineers with a reliable, up-to-date source of Googlebot CIDR blocks for whitelisting or traffic analysis.

## 📊 Data Formats
The data is automatically refreshed daily and available in the `/data` directory:

- `googlebot_ips.json`: Structured JSON with metadata and counts.
- `googlebot_ips.csv`: Simple CSV for spreadsheet import.
- `googlebot_ips.txt`: Plain text list for easy copy-pasting into firewall configs.

## 🛠 Automation
The repository uses **GitHub Actions** to fetch the latest data from official Google-related sources every day at 02:00 UTC.

## 📂 Repository Structure
- `data/`: Contains the generated IP list files.
- `scripts/`: Python automation scripts.
- `.github/workflows/`: GitHub Actions workflow definitions.
- `tests/`: Unit tests for parsing and validation.

## 🛠 Development
To run the update script locally:

1. Clone the repository.
2. Create a virtual environment: `python3 -m venv venv`
3. Install dependencies: `./venv/bin/pip install requests`
4. Run the script: `./venv/bin/python3 scripts/fetch_googlebot_ips.py`

## 📜 License
MIT
