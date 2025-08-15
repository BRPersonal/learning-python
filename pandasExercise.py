import pandas as pd

# Sample data
data = {"Score": [10, 20, 40, 50, 70, 80, 90, 100]}
df = pd.DataFrame(data)

#define bins and labels
bins = [0,50,75,90,100]
labels = ["<=50","<=75","<=90","<=100"]

df['Bucket'] = pd.cut(df['Score'], bins=bins, labels=labels, right=True)
cumulative_percentage = df['Bucket'].value_counts(normalize=True).sort_index().cumsum() * 100
print(f"cumulative_percentage:\n{cumulative_percentage}")