import os
data = os.popen("sensors").read()
with open("testFile.txt",'w') as test:
	test.write(data)
