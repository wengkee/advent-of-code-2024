from data_file import DataFile
import pandas as pd

# data_file = DataFile("data/d1.test")
df = pd.read_csv("data/d1.data", header=None, names=['x','y'], sep='   ', engine='python')
x = df['x'].to_list()
# x.sort()
y = df['y'].to_list()
# y.sort()
# print(x)
# print(y)

total = 0 
# for i in range(len(x)):
#     total += abs(x[i]-y[i])

# print(total)
similarity = 0
for i in range(len(x)):
    # total += abs(x[i]-y[i])
    cur = x[i]
    # print("x", cur)
    ydf = df.loc[df['y'] == cur]
    similarity += cur * ydf.shape[0]
    # print(ydf.shape[0])
    # print("====")
print(similarity)