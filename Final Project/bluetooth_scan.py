import subprocess

def getBDevices():
	bluetooth = subprocess.check_output("hcitool scan",shell=True)
	blue_list = bluetooth.split('\n')
	blue_final =[]
	for b in range(1, len(blue_list)-1):
		temp =blue_list[b].split('\t')
		address = temp[1]
		name = temp[2]
		temp = address, name
#		print (temp[0],temp[1])
		blue_final.append(temp)
	return blue_final
#getBDevices()
