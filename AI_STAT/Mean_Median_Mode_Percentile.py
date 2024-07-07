# Mean, Median, Mode, and Percentile
# Outlier is a datapoint that is very different than the rest of the data points
# Median is the 50th percentile of values in a dataset
# The range between 25th and 75th percentile is called Interquartile Range IQR
# Percentile is used to find outlier in data science
# Mode is the highest value in the list of values
# Average is dividing sum of values by the total count of values to find the average value
"""
finding quantile or percentile with weighted mean i.e when the mean is between two values:
Rank = percentile(e.g 0.25)/100 * (number of items + 1)
weighted mean = (percentile*(higher value - lower value)) + lower value
"""
f = open("D:\\AI Engineering\\Python\My_Projects\\Project1\\AI_STAT\\income.csv", "w")
f.write(
    "\nname, income, \nRob, 5000, \nRafiq, 6000,\nNine, 4000, \nSofia, 7500, \nMohan, 8000, \nTao, 7000, \nElon Musk, 1000000")
f.close()

import pandas as pd
import numpy as np

df = pd.DataFrame(
    {"name": ["Rob", "Rafiq", "Nine", "Sofia", "Mohan", "Tao", "Elon Musk"],
     "income": [5000, 6000, 4000, 7500, 8000, 7000, 10000000]
     })

d = pd.read_csv("income.csv")
print(df)

print(df.describe())

print(f"\n10th percentile: \n{df.income.quantile(0.10)}")
print(f"25th percentile: \n{df.income.quantile(0.25)}")
print(f"50th percentile: \n{df.income.quantile(0.50)}")
print(f"75th percentile: \n{df.income.quantile(0.75)}")

# To select lower or higher percentile
print(f"\n25th percentile lower interpolation: \n{df.income.quantile(0.25, interpolation='lower')}")
print(f"25th percentile higher interpolation: \n{df.income.quantile(0.25, interpolation='higher')}")
print(f"75th percentile lower interpolation: \n{df.income.quantile(0.75, interpolation='lower')}")


# To remove outlier
percentile_99 = df.income.quantile(0.99)
print(f"\npercentile 99: {percentile_99}")
print(f"\n")
outlier = df[df.income > percentile_99]
print(f"outlier: \n{outlier}")

df_new = df[df.income <= percentile_99]

print(f"\n")
print(df_new)

# Filling missing value

df['income'][3] = np.NaN  # create a missing value
print(df)

df_clean = df.fillna(df.income.median())

print(f"\nclean df")
print(df_clean)


