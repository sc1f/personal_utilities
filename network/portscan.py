import argparse, socket
args = argparse.ArgumentParser()
args.add_argument("tgthost", type=str, help="the hostname to scan")
args.add_argument("tgtport", type=str,  help="the port(s) to scan")
input = args.parse_args()

def scanConnection(host, port, info):
    try:
        sock = socket.socket(info[0], info[1], info[2])
        sock.connect(info[4])
        print("[+] %d/tcp open" % port)
        sock.close()
    except:
        print("[-] %d/tcp closed" % port)

def scanPort(host, ports):
    target_info = socket.getaddrinfo(str(host),80) 
    try: 
        target_ip = target_info[4][0]
        print('___Scan results for %s___' % str(target_ip))
    except:
        print("Cannot resolve %s" % host)
        return
    socket.setdefaulttimeout(1)
    for port in ports:
        print("scanning port: " + port)
        scanConnection(host, int(port), target_info)

def main():
    tgtports = str(input.tgtport).replace(' ','').split(',')
    tgtports = map(int, tgtports)
    print(input.tgthost)
    print(tgtports)
    scanPort(input.tgthost, tgtports)

if __name__ == '__main__':
    main()
