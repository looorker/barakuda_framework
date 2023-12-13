import nmap3
def net_hosts():
    waken_hosts = []
    nmap = nmap3.NmapHostDiscovery()
    scan = nmap.nmap_arp_discovery('192.168.31.0/24', args='')
    print(scan)
    try:
        for i in scan:
            if scan[str(i)]['state']['state'] != 'down':
                waken_hosts.append(i)
    except KeyError:
        pass
    return waken_hosts if len(waken_hosts) > 1   else 0
    print(scan['192.168.31.0']['state']['state'] == 'down')