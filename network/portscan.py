import argparse, socket
args = argparse.ArgumentParser()
args.add_argument("tgthost", type=str, help="the hostname to scan")
args.add_argument("tgtport", type=str,  help="the port(s) to scan")
input = args.parse_args()

def scanConnection(host, port, info):
    try:
        sock = socket.socket(info[0][0], info[0][1], info[0][2])
        sock.connect(info[0][4])
        sock.send(str.encode('TestString\r\n'))
        res = sock.recv(4096)
        print("[+] %d/tcp open" % port)
        print("--- " + str(res) + " ---")
        sock.close()
    except:
        print("[-] %d/tcp closed" % port)

def scanPort(host, ports):
    target_info = socket.getaddrinfo(str(host),80) 
    try: 
        target_ip = target_info[0][4]
        print('___Scan results for %s___' % str(target_ip))
    except:
        print("Cannot resolve %s" % host)
        return
    socket.setdefaulttimeout(1)
    for port in ports:
        print("scanning port: " + str(port))
        scanConnection(host, int(port), target_info)

def main():
    tgtports = str(input.tgtport).replace(' ','').split(',')
    tgtports = map(int, tgtports)
    scanPort(input.tgthost, tgtports)

if __name__ == '__main__':
    main()
