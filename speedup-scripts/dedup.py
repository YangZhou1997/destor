import os
import signal
import sys
import time
import subprocess
import glob

cmd_kv = {
	'clean': 'cd ~/destor && unbuffer ./rebuild {working_dir} && rm ~/destor/speedup-scripts/log/{task_name}.log', 
	'dedup': 'cd ~/destor && unbuffer ./destor -c"{config_path}" {dedup_file} -p"{config_line}" &>> ~/destor/speedup-scripts/log/{task_name}.log',
}

def signal_handler(sig, frame):
	sys.exit(0)

# non-blocking or blocking actually depends on whether cmd is bg or fg
def blocking_run(cmd):
	ret = subprocess.check_output(['/bin/bash', '-c', cmd])	
	return ret

# always non-blocking, as it is running in a subprocess. 
def non_blocking_run(cmd):
    subprocess.Popen(['/bin/bash', '-c', cmd])

# this folder contains multiple macos/fslhomes-date sub-folders
def extract_fileset(folder, chunk_size):
	splits = folder.split('/')
	data_type = splits[-2]
	year = splits[-1]
	fileset = glob.glob(f'{folder}/{data_type}-*/{data_type}-*.{chunk_size}.hash.anon')
	fileset.sort()
	return fileset

# a set of files as time goes by. 
def do_dedup(fileset, task_name, working_dir, config_path, config_line):
	blocking_run(cmd_kv['clean'].format(working_dir=working_dir, task_name=task_name))
	file_num = len(fileset)
	for i, dedup_file in enumerate(fileset):
		print(f'dedup - {i}/{file_num}: {dedup_file}')
		blocking_run(cmd_kv['dedup'].format(config_path=config_path, dedup_file=dedup_file, config_line=config_line, task_name=task_name))

if __name__ == "__main__":	
	fileset = extract_fileset('/users/yangzhou/datasets/macos/2012', '4kb')
	# print(fileset, len(fileset))

	task_name = 'macos-4kb'
	working_dir = '/users/yangzhou/working'
	config_path = '/users/yangzhou/destor/destor.config'
	config_line = f'working-directory "{working_dir}"'
	do_dedup(fileset, task_name, working_dir, config_path, config_line)
    