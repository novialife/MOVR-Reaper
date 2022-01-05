import subprocess
import sys
import time
import timeit


def main():
    procs = []
    for i in range(100):
        proc = subprocess.Popen([sys.executable, 'FaucetLeak.py'])
        proc2 = subprocess.Popen([sys.executable, 'FaucetLeak.py'])
        proc3 = subprocess.Popen([sys.executable, 'FaucetLeak.py'])
        # proc4 = subprocess.Popen([sys.executable, 'FaucetLeak.py'])
        # proc5 = subprocess.Popen([sys.executable, 'FaucetLeak.py'])
        # proc6 = subprocess.Popen([sys.executable, 'FaucetLeak.py'])

        procs.append(proc)
        procs.append(proc2)
        procs.append(proc3)
        # procs.append(proc4)
        # procs.append(proc5)
        # procs.append(proc6)

        time.sleep(10)

    for proc in procs:
        proc.wait()


print(timeit.timeit(main(), number=1))
