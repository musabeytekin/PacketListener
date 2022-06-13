import scapy.all as scapy
from scapy_http import http
import optparse

def get_inputs():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest = 'interface', help = 'Enter interface to packet listening')
    inputs = parser.parse_args()[0]
    if not inputs.interface:
        print('Please enter a interface')
    return inputs
def listen(interface):
    scapy.sniff(iface = interface, store = False, prn = analyze)


def analyze(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            print(packet[scapy.Raw].load)


inputs = get_inputs()

listen(str(inputs.interface))


