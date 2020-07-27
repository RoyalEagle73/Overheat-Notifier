import re
import os
temp_details = re.findall(r'([+-]?\d+(\.\d+)*)\s?°([CcFf])',str(os.popen("watch -g sensors").read()))
temperatures = (i[0] for i in temp_details)
print(temperatures, temp_details)
