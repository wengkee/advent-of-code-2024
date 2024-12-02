import pandas as pd

df = pd.read_csv("data/d1.data", header=None, names=['x','y'], sep='   ', engine='python')
x = df['x'].to_list()
x.sort()
y = df['y'].to_list()
y.sort()

total, similarity = 0, 0
for i in range(len(x)):
    total += abs(x[i]-y[i])
    cur = x[i]
    ydf = df.loc[df['y'] == cur]
    similarity += cur * ydf.shape[0]
print(total)
print(similarity)