import pandas as pd
import numpy as np

# df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv',)

# 5. Filter 'Manufacturer','Model', 'Type'
rows_of_20 = df[::20]
print(rows_of_20.iloc[:,:3])


# 6. Replace missing values
mean_min = df['Min.Price'].mean()
mean_max = df['Max.Price'].mean()
df['Min.Price'].fillna(mean_min, inplace=True)
df['Max.Price'].fillna(mean_max, inplace=True)
print(df)

# 7. Get rows
df_lst = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))

row_sum = df_lst.sum(axis=1)
filtered_rows = df_lst[row_sum > 100]
print(filtered_rows)