import re
from collections import Counter

def extract_ips_from_logs(log_file):
    with open(log_file, "r") as file:
        log_data = file.read()
    ip_address = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", log_data)
    return ip_address

iparray = extract_ips_from_logs("Linux_2k.log")

ip_counts = Counter(iparray)

high = ip_counts.most_common(5)

print(high)

# for ip, count in ip_counts.items():
#     print(f"IP Address {ip} occurred {count} times.")