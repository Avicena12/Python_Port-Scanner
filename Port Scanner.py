from socket import *
def conScan(targetHost, targerPort):
    try:
        connskt = socket(AF_INET, SOCK_STREAM)
        connskt.connect((targetHost, targerPort))
        print('[+]%d/tcp open'% targerPort)
        connskt.close()
    except:
        print('[+]%d/tcp closed'% targerPort)

def portScan(targetHost, targetPorts):
    try:
        targetIP = gethostbyname(targetHost)
    except:
        print('[-] Cannot resolve %s '% targetHost)
        return
    try:
        targetName = gethostbyaddr(targetIP)
        print('\n[+] Scan result of; %s ' % targetName[0])
    except:
        print('\n[+] Scan result of; %d ' % targetIP)
    setdefaulttimeout(1)
    for targetPort in targetPorts:
        print('Scanning Port: %d'% targetPort)
        conScan(targetHost, int(targetPort))

if __name__ == '__main__':
    portScan('www.google.com' , [80, 22])