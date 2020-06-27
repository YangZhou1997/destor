import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
from util_plot import *
from util_serilize import *
import glob
import os

# params = {
#     'axes.labelsize': 20,
#     'font.size': 20,
#     'legend.fontsize': 20,
#     'xtick.labelsize': 20,
#     'ytick.labelsize': 20,
# }
# rcParams.update(params)

FIGSIZE=(6, 3.6)

def load(file):
    ratios = []
    overall_ratio = []
    total_size = 0
    stored_size = 0
    lines = open(file, 'r').read().strip('\n').split('\n')
    for line in lines:
        if 'deduplication ratio:' in line:
            splits = line.split()
            dup_ratio = float(splits[2].strip(','))
            ratios.append(dup_ratio)
        if 'total size(B):' in line:
            splits = line.split()
            total_size += float(splits[2])
        if 'stored data size(B):' in line:
            splits = line.split()
            stored_size += float(splits[3])
            overall_ratio.append(1-stored_size/total_size)
    return ratios, overall_ratio

def plot(ratios, taskname, fig_name, y_label):
    N = len(ratios)
    # ind = np.arange(N) * 10 + 10
    fig, ax = plt.subplots()

    xs = [i for i in range(N)]
    ys = ratios

    cnt = 0
    legends = []
    p1, = ax.plot(xs, ys, linestyle = linestyles[cnt], marker = markers[cnt], markersize = markersizes[cnt], color=colors2[cnt], linewidth=3)
    
    legends.append(p1)

    ax.legend(legends, [taskname, ])

    labels = list(map(lambda x: f'{x}', xs[::len(xs)//5]))
    plt.xticks(xs[::len(xs)//5], labels)

    ax.set_xlabel(f'Backup version')
    ax.set_ylabel(y_label)

    fig.set_size_inches(FIGSIZE)
    fig.tight_layout()

    fig.savefig(f'figs/dup_ratio_{fig_name}.pdf', bbox_inches='tight')
    fig.clf()

def plot_all(ratios_list, taskname_list, fig_name, y_label):
    fig, ax = plt.subplots()
    legends = []
    max_N = 0
    for cnt, ratios in enumerate(ratios_list):
        N = len(ratios)
        max_N = max(max_N, N)
        xs = [i for i in range(N)]
        ys = ratios
        p1, = ax.plot(xs, ys, linestyle = linestyles[cnt], marker = markers[cnt], markersize = markersizes[cnt], color=colors2[cnt], linewidth=3)
        legends.append(p1)

    ax.legend(legends, taskname_list)

    xs = [i for i in range(max_N)]
    labels = list(map(lambda x: f'{x}', xs))
    plt.xticks(xs, labels)

    ax.set_xlabel(f'DB tables')
    ax.set_ylabel(y_label)

    fig.set_size_inches(FIGSIZE)
    fig.tight_layout()

    fig.savefig(f'figs/{fig_name}.pdf', bbox_inches='tight')
    fig.clf()

def plot_type(datasets, type):
    ratios_list = []
    overall_ratios_list = []
    taskname_list = []
    for dataset in datasets:
        head, tail = os.path.split(dataset)
        taskname = f'{tail}'.split('.')[0]
        taskname_list.append(taskname.replace('_', '\_'))

        ratios, overall_ratios = load(f'./log/{taskname}.log')
        ratios_list.append(ratios)
        overall_ratios_list.append(overall_ratios)

    if type == 'non-cumu':
        plot_all(ratios_list, taskname_list, f'{type}-per-version', 'Self-redundancy per table')
    elif type == 'cumu':    
        plot_all(overall_ratios_list, taskname_list, f'{type}-over-time', 'Redundancy acorss tables')

if __name__ == "__main__":
    datasets = glob.glob(f'./log/*-perfile.log')
    plot_type(datasets, 'non-cumu')
    datasets2 = glob.glob(f'./log/*.log')
    datasets = list(set(datasets2) - set(datasets))
    plot_type(datasets, 'cumu')