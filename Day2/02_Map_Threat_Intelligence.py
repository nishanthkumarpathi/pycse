threat_intel = {
    "192.0.2.123": "Botnet",
    "203.0.113.204": "Phishing",
    "198.51.100.42": "Malware C2"
}

ip = "192.0.2.123"
print(threat_intel[ip])  # Outputs: Botnet