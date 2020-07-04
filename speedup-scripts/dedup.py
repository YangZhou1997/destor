import os
import signal
import sys
import time
import subprocess
import glob

cmd_kv = {
    'clean_working_set': 'cd ~/destor && unbuffer ./rebuild {working_dir}',
    'clean': 'cd ~/destor && unbuffer ./rebuild {working_dir} && > ~/destor/speedup-scripts/log/{task_name}.log',
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

# a set of files as time goes by.
def do_dedup(backups, task_name, working_dir, config_path, config_line):
    blocking_run(cmd_kv['clean'].format(
        working_dir=working_dir, task_name=task_name))
    file_num = len(backups)
    for i, dedup_file in enumerate(backups):
        print(f'dedup - {i}/{file_num}: {dedup_file}')
        blocking_run(cmd_kv['dedup'].format(config_path=config_path,
                                            dedup_file=dedup_file, config_line=config_line, task_name=task_name))

def do_dedup_per_file(backups, task_name, working_dir, config_path, config_line):
    blocking_run(cmd_kv['clean'].format(
        working_dir=working_dir, task_name=task_name))
    file_num = len(backups)
    for i, dedup_file in enumerate(backups):
        blocking_run(cmd_kv['clean_working_set'].format(
            working_dir=working_dir))
        print(f'dedup - {i}/{file_num}: {dedup_file}')
        blocking_run(cmd_kv['dedup'].format(config_path=config_path,
                                            dedup_file=dedup_file, config_line=config_line, task_name=task_name))


if __name__ == "__main__":
    working_dir = '/home/administrator/working'
    config_path = '/home/administrator/destor/speedup-scripts/config/destor.config'
    config_line = f'working-directory "{working_dir}"'

    # datasets = glob.glob(f'/home/administrator/datasets/*')
    # for dataset in datasets:
    #     head, tail = os.path.split(dataset)
    #     task_name = f'{tail}'
    #     if task_name in ['macos', 'fslhomes']:
    #         config_path = '/home/administrator/destor/speedup-scripts/config/destor_fsl.config'
    #         backups = glob.glob(f'{dataset}/*/*.32kb.hash.anon')
    #     else:
    #         config_path = '/home/administrator/destor/speedup-scripts/config/destor.config'
    #         backups = glob.glob(f'{dataset}/*')
    #     backups.sort()
    #     print(task_name, backups)
    #     # do_dedup(backups, task_name, working_dir, config_path, config_line)
    #     do_dedup_per_file(backups, f'{task_name}-perfile', working_dir, config_path, config_line)

    
    # for scale in [2, 5, 10, 100]:
    #     backups = glob.glob(f'/home/administrator/dedup-data/warehouse/tpcds_bin_partitioned_orc_{scale}.db/*')
    #     task_name=f'tpcds{scale}'
    #     do_dedup(backups, task_name, working_dir, config_path, config_line)
    #     do_dedup_per_file(backups, f'{task_name}-perfile', working_dir, config_path, config_line)

    # for scale in [2, 5, 10, 100]:
    #     backups = glob.glob(f'/home/administrator/dedup-data/warehouse/tpch_flat_orc_{scale}.db/*')
    #     task_name=f'tpch{scale}'
    #     do_dedup(backups, task_name, working_dir, config_path, config_line)
    #     do_dedup_per_file(backups, f'{task_name}-perfile', working_dir, config_path, config_line)


    # backups = list(map(lambda x: f'/home/administrator/dedup-data/warehouse/tpcds_bin_partitioned_orc_{x}.db', [2, 5, 10, 100]))
    # task_name='tpcds'
    # do_dedup(backups, task_name, working_dir, config_path, config_line)
    # do_dedup_per_file(backups, f'{task_name}-perfile', working_dir, config_path, config_line)

    # backups = list(map(lambda x: f'/home/administrator/dedup-data/warehouse/tpch_flat_orc_{x}.db', [2, 5, 10, 100]))
    # task_name='tpch'
    # do_dedup(backups, task_name, working_dir, config_path, config_line)
    # do_dedup_per_file(backups, f'{task_name}-perfile', working_dir, config_path, config_line)


    # backups = glob.glob(f'/home/administrator/dedup-data/warehouse/tpcds_bin_partitioned_orc_2.db/*')
    # task_name=f'tpcds2'
    # do_dedup(backups, task_name, working_dir, config_path, config_line)
    # do_dedup_per_file(backups, f'{task_name}-perfile', working_dir, config_path, config_line)

    # backups = glob.glob(f'/home/administrator/dedup-data/warehouse/tpcds_bin_partitioned_parquet_2.db/*')
    # task_name=f'tpcds2_parquet'
    # do_dedup(backups, task_name, working_dir, config_path, config_line)
    # do_dedup_per_file(backups, f'{task_name}-perfile', working_dir, config_path, config_line)


    # backups =[f'/home/administrator/dedup-data/warehouse/tpcds_bin_partitioned_parquet_2.db', f'/home/administrator/dedup-data/warehouse/tpcds_bin_partitioned_parquet_2_2.db']
    # task_name = f'tpcds2_parquet_two_db'
    # do_dedup(backups, task_name, working_dir, config_path, config_line)
    # do_dedup_per_file(backups, f'{task_name}-perfile', working_dir, config_path, config_line)


    backups = glob.glob(f'/home/administrator/shuffle_log/*')
    backups.sort()
    task_name=f'shuffle_data'
    do_dedup(backups, task_name, working_dir, config_path, config_line)
    # do_dedup_per_file(backups, f'{task_name}-perfile', working_dir, config_path, config_line)

