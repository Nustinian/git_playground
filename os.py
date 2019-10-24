import os

myCmd = 'ls -la'
output = os.system(myCmd)

os.system("echo ", output, ">> output.txt")
