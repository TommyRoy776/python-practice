import pandas as pd
import numpy as np

# #dataframe example
# df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], columns=["A","B","C"])
# print(df.describe())
# print(df.head(n=2))

# Show all columns
pd.set_option('display.max_columns', None)
# Optional: set full width for wider consoles
pd.set_option('display.width', None)

#Read csv
df = pd.read_csv('./dataset/NYC_Weather_2016_2022.csv', sep=',')
# get rows 
# print(df.head())
# print(df.tail())
# print(df.sample(5))

#get exact specific row(s)
print(df.columns)
#label based 
print(df.loc[0:2,["time","temperature_2m (°C)","winddirection_10m (°)"]])
#index based 
print(df.iloc[0:2,[0,1,9]])

# print(df.iloc[0:10,:])

arr = np.array(range(10))
