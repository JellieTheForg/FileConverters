import pandas as pd
import numpy as np

data = np.arange(1, 10001).reshape(100, 100)

df = pd.DataFrame(data)

df.to_csv('increasing_values.csv', index=False)
