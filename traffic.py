import socket
import json

class IPTest():
    def __init__(self,srcaddr, srcport, dstaddr, dstport, name="Test"):
        self.name = name

        # Test if the IP Address we received is a valid IP Address
        try:
            socket.inet_aton(srcaddr)
            socket.inet_aton(dstaddr)
            self.srcAddr = srcaddr
            self.dstAddr = dstaddr
        except socket.error as msg:
            print(msg)

        #Verify if port numbers are within range
        if self.verifyPort(srcport):
            self.srcPort = srcport
        if self.verifyPort(dstport):
            self.dstPort = dstport
    def verifyPort(self, num):
        if (int(num) > 0 and int(num) < 65536):
            return True
        else:
            return False
    def tojson(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class UDPTest(IPTest):
    def __init__(self,srcaddr, srcport, dstaddr, dstport, name="UDPTest"):
        IPTest.__init__(self,srcaddr, srcport, dstaddr, dstport,name="UDPTest")



test = UDPTest("192.168.122.9","1001","192.168.122.8","1001")
print(test.tojson())


