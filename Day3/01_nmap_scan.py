import nmap

def run_nmap_scan(targetip):
    nm = nmap.PortScanner()
    nm.scan(targetip, '22-443')
    return nm.all_hosts()

print(run_nmap_scan('10.1.60.55'))