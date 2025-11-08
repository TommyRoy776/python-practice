import pandas as pd
import numpy as np

# Show all columns
pd.set_option('display.max_columns', None)

# Optional: set full width for wider consoles
pd.set_option('display.width', None)

df = pd.read_csv('./dataset/NYC_Weather_2016_2022.csv', sep=';')
# Print only the first 10 columns (all rows)
print(df.iloc[:10,:])
print(df.dtypes)

arr = np.array(range(10))
