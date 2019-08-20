import os
command =  'ipconfig /all'
output = os.popen(command)
info = output.readlines()
for line in info:
 print (line.decode('gbk').strip('\r\n'))