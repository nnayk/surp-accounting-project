# Nakul Nayak
# This script plots auditor gender vs average fee for BigN and non-BigN auditing firms

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

FILE_PATH = "../data/gco_model.xlsx"
OUTPUT_PATH = "../images/gender_vs_gco.png"
X_KEY = "Gender"
Y_KEY = "GCO"
X_LABEL = X_KEY
Y_LABEL = 'Number of GCOs issued'
BAR_LABELS = ['Female','Male']
BAR_COLORS = ['pink','skyblue']

# # Read in the data
df_fee = pd.read_excel(FILE_PATH)
df = pd.read_excel(FILE_PATH)

# Filter the DataFrame for BigN=1
df_bign_1 = df[df['BigN'] == 1]

# Filter the DataFrame for BigN=0
df_bign_0 = df[df['BigN'] == 0]

# Calculate the average fee for each gender in both subsets
avg_fee_bign_1 = df_bign_1.groupby(X_KEY)[Y_KEY].mean().reset_index()
avg_fee_bign_0 = df_bign_0.groupby(X_KEY)[Y_KEY].mean().reset_index()

# Create subplots for the two bar charts
fig, axes = plt.subplots(1, 2, figsize=(12, 5))  # 1 row, 2 columns for two subplots

# Plot the bar chart for BigN=1
axes[0].bar(avg_fee_bign_1[X_KEY], avg_fee_bign_1[Y_KEY], color=['pink','skyblue'])
axes[0].set_xlabel(X_KEY)
axes[0].set_ylabel(Y_LABEL)
axes[0].set_title('Auditor Gender vs GCO Count (BigN auditing firms)')
axes[0].set_xticks(avg_fee_bign_1.index)
axes[0].set_xticklabels(['Female', 'Male'])  # Modify the x-axis labels

# Plot the bar chart for BigN=0
axes[1].bar(avg_fee_bign_0[X_KEY], avg_fee_bign_0[Y_KEY], color=['pink','skyblue'])
axes[1].set_xlabel(X_KEY)
axes[1].set_ylabel(Y_LABEL)
axes[1].set_title('Auditor Gender vs GCO Count (Non-BigN auditing firms)')

# Adjust spacing between subplots
plt.tight_layout()

# Show the plots
plt.xticks([0, 1], BAR_LABELS)

plt.savefig(OUTPUT_PATH)
plt.show()