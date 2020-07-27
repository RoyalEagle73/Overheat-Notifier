import re
import os

def FtoC(temp):
	temp = temp - 32
	temp *= (5/9)
	return temp

temp_details = re.findall(r'([+-]?\d+(\.\d+)*)\s?°([CcFf])',str(os.popen("watch -g sensors").read()))
temperatures = [str(i[0])+i[2] for i in temp_details]
finalTemperatures = [] 
for i in temperatures:
	type = i[-1]
	posCheck = i[0]
	final_temperature = i[1:-1]
	if(posCheck == '-'):
		final_temperature *= 1
	if(type == 'F' or type == 'f'):
		final_temperature = FtoC(int(final_temperature))
	finalTemperatures.append(final_temperature)
print(finalTemperatures)
