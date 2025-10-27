import os

import numpy as np
import pickle
import matplotlib.pyplot as plt

# one single one directly on the track
N_obs = 1
obstacles = []
obstacles.append((np.array([3.0, 1.0]), 0.5))
xg = np.array([6.0, 1.0])


run_name = 'temp_single_obstacle_Unicycle'

with open(os.path.join(run_name, 'FITS.pkl'), 'rb') as file:
    # Load the content
    FITS = pickle.load(file)

with open(os.path.join(run_name, 'CBF1.pkl'), 'rb') as file:
    # Load the content
    CBF = pickle.load(file)

with open(os.path.join(run_name, 'MPC1.pkl'), 'rb') as file:
    # Load the content
    MPC = pickle.load(file)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

fig, ax = plt.subplots(figsize=(8, 2.5))

for obs, r in obstacles:
    circle = plt.Circle(obs, r, facecolor=(220/255, 33/255, 77/255, 0.5), edgecolor=(220/255, 33/255, 77/255))
    ax.add_patch(circle)
plt.scatter(xg[0], xg[1], marker='*', s=200, color=(0, 140/255, 0))

plt.plot(CBF['trajs_data'][:,0], CBF['trajs_data'][:, 1], color='darkorange', linewidth=2, label='CBF')
plt.plot(FITS['trajs_data'][:,0], FITS['trajs_data'][:, 1], color=(0, 100/255, 222/255), label='FITS')
plt.plot(MPC['trajs_data'][:,0], MPC['trajs_data'][:, 1], linestyle='dashed', color=(0, 140/255, 0/255), linewidth=2, label='NMPC')

ax.set_xlim(-0.5, 7.0)
ax.set_ylim(0.5, 1.8)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 0.99), ncol=3)

# Set labels with LaTeX formatting
ax.set_xlabel(r'$p_x$\textrm{ in [m]}', fontsize=18)
ax.set_ylabel(r'$p_y$\textrm{ in [m]}', fontsize=18)
plt.tight_layout()
plt.subplots_adjust(bottom=0.19)

plt.savefig(run_name + '.png', dpi=300)
# plt.show()

