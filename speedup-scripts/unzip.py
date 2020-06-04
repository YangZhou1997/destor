import os
import signal
import sys
import time
import subprocess
import glob
def signal_handler(sig, frame):
	print('kill all servers and clients')
	for h in hosts:
		print(f'kill {h}')
		ret = os.popen(Cmds['kill'].format(user=user, host=h)).read()
	sys.exit(0)

# non-blocking or blocking actually depends on whether cmd is bg or fg
def blocking_run(cmd):
	ret = subprocess.check_output(['/bin/bash', '-c', cmd])	
	return ret

# always non-blocking, as it is running in a subprocess. 
def non_blocking_run(cmd):
    subprocess.Popen(['/bin/bash', '-c', cmd])

def unzip_folder(folder):
    files = glob.glob(f'{folder}/*.tar.bz2')
    for file in files:
        head, tail = os.path.split(file)
        cmd = f'cd {head} && tar -xvjf {tail} && rm {tail}'
        print(cmd)
        blocking_run(cmd)

if __name__ == "__main__":	
    signal.signal(signal.SIGINT, signal_handler)
    unzip_folder("/users/yangzhou/data/macos/2012")
    unzip_folder("/users/yangzhou/data/sdb/fslhomes/2012")
    