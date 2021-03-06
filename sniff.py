"""
Created on Wed Aug 01  11:15:15 2018

@author: mshaik
"""


from struct import *
import pcapy
import sys
import socket
import time



def main(argv):
    #list all devices
    devices = pcapy.findalldevs()
    print devices
     
    #ask user to enter device name to sniff
    print "Available devices are :"
    for d in devices :
        print d
     
    dev = raw_input("[\Device\NPF_{9A5C7571-B7BD-443F-978B-F7581156E9CE}] : ") or "\Device\NPF_{9A5C7571-B7BD-443F-978B-F7581156E9CE}"

     
    print "Sniffing device " + dev



     
    '''
    open device
    # Arguments here are:
    #   device
    #   snaplen (maximum number of bytes to capture _per_packet_)
    #   promiscious mode (1 for true)
    #   timeout (in milliseconds)
    '''
    cap = pcapy.open_live(dev	, 256, 1 , 0)
 
    #start sniffing packets
    while(1) :
        (header, packet) = cap.next()
        #print ('%s: captured %d bytes, truncated to %d bytes' %(datetime.datetime.now(), header.getlen(), header.getcaplen()))
        parse_packet(packet)
 
#Convert a string of 6 characters of ethernet address into a dash separated hex string
def eth_addr (a) :
    b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(a[0]) , ord(a[1]) , ord(a[2]), ord(a[3]), ord(a[4]) , ord(a[5]))
    return b
 
#function to parse a packet
def parse_packet(packet) :
     
    #parse ethernet header
    eth_length = 14
     
    eth_header = packet[:eth_length]
    eth = unpack('!6s6sH' , eth_header)
    eth_protocol = socket.ntohs(eth[2])
    print 'Destination MAC : ' + eth_addr(packet[0:6]) + ' Source MAC : ' + eth_addr(packet[6:12]) + ' Protocol : ' + str(eth_protocol)
 
    #Parse IP packets, IP Protocol number = 8
    if eth_protocol == 8 :
        #Parse IP header
        #take first 20 characters for the ip header
        ip_header = packet[eth_length:20+eth_length]

        #now unpack them :)
        iph = unpack('!BBHHHBBH4s4s' , ip_header)
 
        version_ihl = iph[0]
        version = version_ihl >> 4
        ihl = version_ihl & 0xF

 
        iph_length = ihl * 4
 
        ttl = iph[5]
        protocol = iph[6]
        s_addr = socket.inet_ntoa(iph[8]);
        d_addr = socket.inet_ntoa(iph[9]);

 
        print 'Version : ' + str(version) + ' IP Header Length : ' + str(ihl) + ' TTL : ' + str(ttl) + ' Protocol : ' + str(protocol) + ' Source Address : ' + str(s_addr) + ' Destination Address : ' + str(d_addr)


        #UDP packets
        if protocol == 17 :
            u = iph_length + eth_length
            udph_length = 8
            udp_header = packet[u:u+8]
 
            #now unpack them :)
            udph = unpack('!HHHH' , udp_header)
             
            source_port = udph[0]
            dest_port = udph[1]
            length = udph[2]
            checksum = udph[3]
            #ts = datetime.datetime.now().timestamp()
             
            print 'Source Port : ' + str(source_port) + ' Dest Port : ' + str(dest_port) + ' Length : ' + str(length) + ' Checksum : ' + str(checksum)
             
            h_size = eth_length + iph_length + udph_length
            data_size = len(packet) - h_size

            #get data from the packet
            sutphData = packet[h_size:h_size+24]
            sutph = unpack('>Q8H', sutphData)

            Timestamp = sutph[0]
            Mnumber = sutph[1]
            Sequencenumber = sutph[2]
            Scanner_ID = sutph[3]
            Datatype_ID = sutph[4]
            Firmware_Version = sutph[5]
            Scan_Number = sutph[6]
            Fragments_Total = sutph[7]
            Fragments_Number = sutph[8]

            print 'Timestamp:' + str(Timestamp)
            print 'Mnumber: ' + hex(Mnumber)
            print 'Sequencenumber:' + str(Sequencenumber)
            print 'ScanID:' + str(Scanner_ID)
            print 'DatatypeID:' + hex(Datatype_ID)
            print 'Firmware Version :' + str(Firmware_Version)
            print 'Scan Number :' + str(Scan_Number)
            print 'Fragments Total :' + str(Fragments_Total)
            print 'Fragment Number :' + str(Fragments_Number)





            sutpPayload = packet[h_size + 24:]








        #some other IP packet like IGMP
        else :
            print 'Protocol other than UDP'
             
        print


 
if __name__ == "__main__":
  main(sys.argv)
