import os
import signal
import sys
import time
import subprocess
import glob
import multiprocessing
import threading
from multiprocessing.dummy import Pool as ThreadPool

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

def run_cmd_prompt(cmd_line):
    try:
        print(f'{threading.currentThread().getName()} running: {cmd_line}', flush=True)
        blocking_run(cmd_line)
        print(f'{threading.currentThread().getName()} okay: {cmd_line}', flush=True)
        return f'okay: {cmd_line}'
    except Exception:
        print(f'{threading.currentThread().getName()} fails: {cmd_line}', flush=True)
        return f'fails: {cmd_line}'

def run_cmd_parallel(commands):
    # 1 thread is left.
    core_num = multiprocessing.cpu_count()
    print(core_num)
    pool = ThreadPool(core_num - 1)
    results = pool.map(run_cmd_prompt, commands)
    pool.close()
    pool.join()
    for res in results:
        print(res)

def unzip_folder(folder):
    files = glob.glob(f'{folder}/*.tar.bz2')
    cmds = []
    for file in files:
        head, tail = os.path.split(file)
        cmd = f'cd {head} && tar -xvjf {tail} && rm {tail}'
        print(cmd)
        cmds.append(cmd)
    return cmds

if __name__ == "__main__":	
    signal.signal(signal.SIGINT, signal_handler)
    cmds = []
    cmds.extend(unzip_folder("/users/yangzhou/datasets/macos/2012"))
    cmds.extend(unzip_folder("/users/yangzhou/datasets/fslhomes/2012"))
    # print(cmds)
    run_cmd_parallel(cmds)
