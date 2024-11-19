import pandas as pd

df = pd.read_csv('cus_data.csv')
df['CustomerID'] = ['Jabyer' + str(i) for i in range(1, len(df) + 1)]
df['Gender'] = 'Secret'
df['Income'] = 'WanMilyon'
df.to_csv('mydats.csv', index=False)
