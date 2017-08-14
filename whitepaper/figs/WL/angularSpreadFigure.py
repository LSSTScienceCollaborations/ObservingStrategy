import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import FigureCanvasPdf
from matplotlib.patches import Ellipse

# position angles
thetas = [0.1, 0.4, 1.5]

fig = plt.Figure(figsize=(6, 3))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

length = 0.8
xbar = ybar = 0.0
colors = ['#377eb8', '#ff7f00', '#4daf4a']
for th, c in zip(thetas, colors):
    beta = 2*th #  shear phase
    ax1.arrow(0.0, 0.0, length*np.cos(th), length*np.sin(th), width=0.02, head_width=0.02, length_includes_head=True, color=c)
    ax1.arrow(0.0, 0.0, -length*np.cos(th), -length*np.sin(th), width=0.02, head_width=0.02, length_includes_head=True, color=c)
    ax2.arrow(0.0, 0.0, length*np.cos(beta), length*np.sin(beta), width=0.02, head_width=0.1, length_includes_head=True, color=c)
    xbar += np.cos(beta)
    ybar += np.sin(beta)

xbar /= len(thetas)
ybar /= len(thetas)

ax2.arrow(0.0, 0.0, length*xbar, length*ybar, width=0.02, head_width=0.1, color='k')

for ax in [ax1, ax2]:
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.axhline(0.0, c='k', lw=0.5)
    ax.axvline(0.0, c='k', lw=0.5)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.add_patch(Ellipse((0.0, 0.0), 2*length, 2*length, fill=False, ec='k'))

ax1.set_title("Headless position angles")
ax2.set_title("Shear phases")

canvas = FigureCanvasPdf(fig)
fig.set_tight_layout(True)
canvas.print_figure("angularSpread.pdf", dpi=100)
