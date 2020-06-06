import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
from util_plot import *
from util_serilize import *

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

def plot(ratios, name, y_label):
    N = len(ratios)
    # ind = np.arange(N) * 10 + 10
    fig, ax = plt.subplots()

    xs = [i for i in range(N)]
    ys = ratios

    legends = []
    p1, = ax.plot(xs, ys, color=colors[0], linewidth=1, linestyle=linestyles[0])
    legends.append(p1)

    ax.legend(legends, ['MacOS server',])

    labels = list(map(lambda x: f'{x}', xs[::20]))
    plt.xticks(xs[::20], labels)

    ax.set_xlabel(f'Snapshot version')
    ax.set_ylabel(y_label)

    fig.set_size_inches(FIGSIZE)
    fig.tight_layout()

    fig.savefig(f'figs/dup_ratio_{name}.pdf', bbox_inches='tight')
    fig.clf()

if __name__ == "__main__":

    ratios, overall_ratio = load('./log/macos-4kb.log')
    plot(ratios, 'macos-4kb', 'Per-snapshot dupliation ratio')
    plot(overall_ratio, 'macos-4kb-overall', 'Overall dupliation ratio')