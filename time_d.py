import time
from datetime import datetime
with open(r"/home/sompalli/work/orchestrator.txt",'r') as file:
   for line in file:
        pass
line=line[1:9]
now = str(datetime.now())
now=now[11:19]
FMT = '%H:%M:%S'
tdelta = datetime.strptime(now, FMT) - datetime.strptime(line, FMT)
print(tdelta)
