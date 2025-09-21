# /// script
# dependencies = ["matplotlib"]
# ///

import matplotlib.pyplot as plt

# Data for the box and whisker plot
stats = [
    {
        'label': 'CPU (WASM)',
        'med': 18.9,
        'q1': 17.8,
        'q3': 19.0,
        'whislo': 11.8,
        'whishi': 19.2,
        'fliers': [],
    },
    {
        'label': 'WebGPU',
        'med': 177.0,
        'q1': 149.0,
        'q3': 272.1,
        'whislo': 45.5,
        'whishi': 344.8,
        'fliers': [],
    },
    {
        'label': 'WebNN-NPU',
        'med': 1250.0,
        'q1': 1120.3,
        'q3': 1495.1,
        'whislo': 908.3,
        'whishi': 1666.7,
        'fliers': [],
    },
]

fig, ax = plt.subplots(figsize=(10, 8))

# Create the boxplot from stats
bp = ax.bxp(stats, patch_artist=True)

# --- Customization for a "beautiful black and red" plot ---

# Colors
box_color = 'red'
whisker_color = 'black'
median_color = 'black'
cap_color = 'black'

for box in bp['boxes']:
    # change outline color
    box.set(color=whisker_color, linewidth=2)
    # change fill color
    box.set(facecolor=box_color)

# Change color and linewidth of the whiskers
for whisker in bp['whiskers']:
    whisker.set(color=whisker_color, linewidth=2)

# Change color and linewidth of the caps
for cap in bp['caps']:
    cap.set(color=cap_color, linewidth=2)

# Change color and linewidth of the medians
for median in bp['medians']:
    median.set(color=median_color, linewidth=2)

# --- Labels, Title, and Grid ---
ax.set_ylabel('Frames Per Second (FPS)', fontsize=14)

# Set y-axis to a logarithmic scale for better visualization
#ax.set_yscale('log')

# Customize ticks
ax.tick_params(axis='both', which='major', labelsize=12)
ax.set_xticklabels([s['label'] for s in stats])

# Add a grid
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=.5)

# Remove top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# --- Save the figure ---
plt.tight_layout()
plt.savefig('black_and_red_boxplot.png', dpi=300)
