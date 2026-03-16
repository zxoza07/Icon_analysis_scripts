import matplotlib.pyplot as plt
import seaborn as sns

def load_rcParams():
    sns.set_style('darkgrid')
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.style'] = 'normal'
    plt.rcParams['font.size'] = 14
    plt.rcParams['axes.labelsize'] = 16
    plt.rcParams['axes.titlesize'] = 16
    plt.rcParams['legend.fontsize'] = 14
    plt.rcParams['font.weight'] = 'light'
    plt.rcParams['mathtext.default'] = 'regular'
    plt.rcParams['lines.markersize'] = 1
    plt.rcParams['lines.markeredgewidth'] = 0
    plt.rcParams['axes.grid'] = True
    plt.rcParams['grid.alpha'] = 0.8
    plt.rcParams['grid.linewidth'] = 0.8
    plt.rcParams['xtick.labelsize'] = 12
    plt.rcParams['ytick.labelsize'] = 12