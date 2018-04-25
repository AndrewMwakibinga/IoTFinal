from bt_proximity import BluetoothRSSI 
import time
import sys
import math
from bluetooth_scan import getBDevices

BT_ADDR = ''  # You can put your Bluetooth address here.  E.g: 'a4:70:d6:7d:ee:00' 
NUM_LOOP = 30

def print_usage():
    print "Usage: python test_address.py <bluetooth-address> [number-of-requests]"


def main():
    b_temp = getBDevices()
    b_list = []
    for b in b_temp:
	b_list.append(b[0])
    n=4    #Path loss exponent(n) = 1.5
    c = 0   #Environment constant(C) = 10
    A0 = 1   #Average RSSI value at d0
    actual_dist = 37   #Static distance between transmitter and Receiver in cm
    sum_error = 0
    count = 0
    num = len(b_list)
    for i in range(10):
	btrssi = BluetoothRSSI(addr='AC:EE:9E:D8:89:4E')
        rssi_bt = float(btrssi.get_rssi()) 
        x = float((rssi_bt-A0)/(-10*n)) 
        distance = (math.pow(10,x) * 100) + c
	#print btrssi.get_addr()
	print 'A0:', float(btrssi.get_rssi()) 
        print "Approximate Distance:" + str(distance)
        print "RSSI: " + str(rssi_bt)
        #time.sleep(1)



if __name__ == '__main__':
    main()
