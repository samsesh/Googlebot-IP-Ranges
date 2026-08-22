import json
import requests
import os
import csv
from datetime import datetime
from pathlib import Path

# Configuration
SOURCE_URL = "https://raw.githubusercontent.com/aminvakil/google-ip-list/main/googlebot.json"
DATA_DIR = Path("data")
OUTPUT_JSON = DATA_DIR / "googlebot_ips.json"
OUTPUT_CSV = DATA_DIR / "googlebot_ips.csv"
OUTPUT_TXT = DATA_DIR / "googlebot_ips.txt"

def fetch_data(url):
    """Fetch JSON data from the source URL."""
    print(f"Fetching data from {url}...")
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def process_ips(data):
    """Process the JSON data into a flat list of CIDRs."""
    print("Processing IP prefixes...")
    ipv4_prefixes = []
    ipv6_prefixes = []
    
    prefixes = data.get("prefixes", [])
    for item in prefixes:
        if "ipv4Prefix" in item:
            ipv4_prefixes.append(item["ipv4Prefix"])
        elif "ipv6Prefix" in item:
            ipv6_prefixes.append(item["ipv6Prefix"])
            
    return ipv4_prefixes, ipv6_prefixes

def save_data(ipv4, ipv6):
    """Save the processed data in multiple formats."""
    DATA_DIR.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 1. Save JSON
    json_content = {
        "last_updated": timestamp,
        "ipv4": ipv4,
        "ipv6": ipv6,
        "summary": {
            "ipv4_count": len(ipv4),
            "ipv6_count": len(ipv6)
        }
    }
    with open(OUTPUT_JSON, "w") as f:
        json.dump(json_content, f, indent=4)
    print(f"Saved JSON to {OUTPUT_JSON}")

    # 2. Save CSV
    with open(OUTPUT_CSV, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["type", "cidr"])
        for ip in ipv4:
            writer.writerow(["ipv4", ip])
        for ip in ipv6:
            writer.writerow(["ipv6", ip])
    print(f"Saved CSV to {OUTPUT_CSV}")

    # 3. Save TXT (Plain list)
    with open(OUTPUT_TXT, "w") as f:
        f.write(f"# Googlebot IP Ranges\n# Updated: {timestamp}\n\n")
        f.write("## IPv4\n")
        for ip in ipv4:
            f.write(f"{ip}\n")
        f.write("\n## IPv6\n")
        for ip in ipv6:
            f.write(f"{ip}\n")
    print(f"Saved TXT to {OUTPUT_TXT}")

def main():
    try:
        data = fetch_data(SOURCE_URL)
        ipv4, ipv6 = process_ips(data)
        save_data(ipv4, ipv6)
        print("\nSuccess! Googlebot IP list updated.")
    except Exception as e:
        print(f"\nError: {e}")
        exit(1)

if __name__ == "__main__":
    main()
