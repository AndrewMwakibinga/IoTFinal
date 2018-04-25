from bt_proximity import BluetoothRSSI 
import time
import sys
import math
from bluetooth_scan import getBDevices

def main():
    b_list = getBDevices()
    n=4     #Path loss exponent(n) = 1.5
    c = 10   #Environment constant(C) = 10
    A0 =-5   #Average RSSI value at d0
    num = len(b_list)
    data_list = []
    for i in range(num):
	btrssi = BluetoothRSSI(addr=b_list[i][0])
	avg_distance = float(0)
	for j in range(3):
	       #btrssi = BluetoothRSSI(addr='AC:EE:9E:D8:89:4E')
        	if(i==0 and j==0):
			time.sleep(10)
		rssi_bt = float(btrssi.get_rssi())
		while(rssi_bt == 0):
			rssi_bt = float(btrssi.get_rssi())		 
		x = float((rssi_bt-A0)/(-10*n)) 
        	distance = (math.pow(10,x) * 100) + c
               # print rssi_bt
		avg_distance+=distance
	avg_distance/=300
	temp = b_list[i][1],avg_distance
	data_list.append(temp)
   #for d in data_list:
#	print(d[0], d[1])
#    print 
    d2_list = data_list
    final_list = []
    for x in range(len(data_list)):
	for y in range(len(d2_list)):
		if(data_list[x][0]==data_list[y][0]):
			continue
		diff = data_list[x][1]-d2_list[y][1]
		diff = math.fabs(diff)
		temp = data_list[x][0],d2_list[y][0],diff
		final_list.append(temp)
    for d2 in final_list:
	print(d2[0],d2[1],d2[2])
    return final_list		
if __name__ == '__main__':
    main()
