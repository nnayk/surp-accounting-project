import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

AUDITOR_FEE_MODEL = "fee_model.xlsx"
# AUDITOR_GCO_MODEL = "gco_model.xlsx"

# # Read in the data
df_fee = pd.read_excel(AUDITOR_FEE_MODEL)
df = pd.read_excel(AUDITOR_FEE_MODEL)

# df_fee = df_fee[(df_fee['Gender'] == 0) | (df_fee['Gender'] == 1)]

# average_fee_by_gender = df_fee.groupby('Gender')['LnAuditfee_w'].mean().reset_index()

# print(average_fee_by_gender)

# # Create the bar chart
# plt.figure(figsize=(8, 5))  # Adjust the figure size as needed
# plt.bar(average_fee_by_gender['Gender'], average_fee_by_gender['LnAuditfee_w'], color=['skyblue', 'pink'])

# # Add labels and a title
# plt.xlabel('Gender')
# plt.ylabel('Natural log of average fee (dollars)')
# plt.title('Average Fee by Gender')

# # Show the plot
# plt.tight_layout()
# plt.show()
# df = pd.DataFrame(data)

# Filter the DataFrame for BigN=1
df_bign_1 = df[df['BigN'] == 1]

# Filter the DataFrame for BigN=0
df_bign_0 = df[df['BigN'] == 0]

# Calculate the average fee for each gender in both subsets
avg_fee_bign_1 = df_bign_1.groupby('Gender')['LnAuditfee_w'].mean().reset_index()
avg_fee_bign_0 = df_bign_0.groupby('Gender')['LnAuditfee_w'].mean().reset_index()

# Create subplots for the two bar charts
fig, axes = plt.subplots(1, 2, figsize=(12, 5))  # 1 row, 2 columns for two subplots

# Plot the bar chart for BigN=1
axes[0].bar(avg_fee_bign_1['Gender'], avg_fee_bign_1['LnAuditfee_w'], color=['pink','skyblue'])
axes[0].set_xlabel('Gender')
axes[0].set_ylabel('Natural log of average fee')
axes[0].set_title('Auditor Gender vs Average Fee (BigN auditing firms)')
axes[0].set_xticks(avg_fee_bign_1.index)
axes[0].set_xticklabels(['Female', 'Male'])  # Modify the x-axis labels

# Plot the bar chart for BigN=0
axes[1].bar(avg_fee_bign_0['Gender'], avg_fee_bign_0['LnAuditfee_w'], color=['pink','skyblue'])
axes[1].set_xlabel('Gender')
axes[1].set_ylabel('Natural log of average fee')
axes[1].set_title('Auditor Gender vs Average Fee (Non-BigN auditing firms)')

# Adjust spacing between subplots
plt.tight_layout()

# Show the plots
plt.xticks([0, 1], ['Female', 'Male'])

plt.savefig('gender_vs_fee.png')
plt.show()