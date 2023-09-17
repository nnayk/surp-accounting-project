# Nakul Nayak
# This script plots CFO extraversion score vs average fee

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score



FILE_PATH = "../data/fee_model.xlsx"
OUTPUT_PATH = "../images/cfo_extra_vs_fee.png"
X_KEY = "CFO_AveExtra"
Y_KEY = "LnAuditfee_w"
X_LABEL = "CFO Extraversion Score"
Y_LABEL = 'Natural log of average fee'

def plot():
    df = pd.read_excel(FILE_PATH)
    df = df[['CFO_AveExtra','LnAuditfee_w']]
    df.dropna(inplace=True)

    # Create a scatterplot between columns X and Y
    plt.scatter(df[X_KEY], df[Y_KEY], color='blue', marker='o')
    plt.xlabel(X_LABEL)
    plt.ylabel(Y_LABEL)
    plt.title('CFO Extraversion vs Average Fee')

    x= df[X_KEY]
    y = df[Y_KEY]

    slope, intercept = np.polyfit(x,y, 1)  # Fit a linear regression line
    y_pred = slope * x + intercept
    r_squared = r2_score(y, y_pred)

    # Annotate the plot with the R-squared value
    plt.text(0.02, 0.95, f'R-squared = {r_squared:.2f}', transform=plt.gca().transAxes, fontsize=12)
    plt.savefig(OUTPUT_PATH)
    plt.show()