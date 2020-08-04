import os
import re
from playsound import playsound

def FtoC(temp):
	temp = temp - 32
	temp *= (5/9)
	return temp

def program():
	lines = [i for i in os.popen("sensors").read().split('\n') if "temp1" and "°" in i]
	temperatures = []
	for line in lines:
		for i in line.split('('):
			if 'temp' in i:
				temperatures.append(i)
	final_temp = []
	for temp in temperatures:
		temp = [final_temp.append(i) for i in temp.split(' ') if "°" in i]
	temperatures = []
	for i in final_temp:
		type = i[-1]
		pos = i[0]
		val = i[1:-2]
		val = int(float(val))
		if pos=='-':
			val *= -1
		if type == 'F' or type == 'f':
			val = FtoC(val)
		temperatures.append(val)
	for temp in temperatures:
		if temp>=50:
			playsound('sound.mp3')
