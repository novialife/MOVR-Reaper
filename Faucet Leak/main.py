import sys
import subprocess
import time

procs = []
for i in range(20):
    proc = subprocess.Popen([sys.executable, 'FaucetLeak.py'])
    procs.append(proc)
    time.sleep(5)

for proc in procs:
    proc.wait()
