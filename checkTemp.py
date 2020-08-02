import os
import re
from playsound import playsound

def FtoC(temp):
        temp = temp - 32
        temp *= (5/9)
        return temp

def program():
	ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
	data = [ ansi_escape.sub('', i).split(' ')[0].split(':')[1] for i in os.popen("watch -g -t sensors").read().split('\n') if "°" in ansi_escape.sub('', i)]

	temperatures = []
	for i in data:
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
		if temp>=70:
			playsound('sound.mp3')
