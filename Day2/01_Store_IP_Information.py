import sys

ip_info = {
    "8.8.8.8": {
        "domain": "google-public-dns-a.google.com",
        "country": "US",
    },
    "1.1.1.1": {
        "domain": "cloudflare-dns.com",
        "country": "AU",
    },
}

ip = sys.argv[1]
print(f"Country for provided ip {ip} is >>>",ip_info[ip]["country"])
