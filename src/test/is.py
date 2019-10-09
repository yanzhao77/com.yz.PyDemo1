import os

cmd='ipconfig'
output=os.popen(cmd)
print(output.read())