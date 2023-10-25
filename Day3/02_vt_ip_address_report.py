import requests
url = "https://www.virustotal.com/api/v3/ip_addresses/220.77.232.234"
headers = {
    "accept": "application/json",
    "x-apikey": "9c0a5015075f6d4d3c9395a870041c65263b5f4c1bfcbfbb91ab19d945f0ba8c"
}
response = requests.get(url, headers=headers)

print(response.text)