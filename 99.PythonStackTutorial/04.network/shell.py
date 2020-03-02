#__author:jack
#date 2020-01-14 13:55

import subprocess

result = subprocess.Popen("ls",shell=True,stdout=subprocess.PIPE)

print(str(result.stdout.read(),'utf-8'))

print('Over!')