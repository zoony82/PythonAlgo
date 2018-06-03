import pandas as pd
import numpy as np

print("pandas tst")

s = pd.Series(np.random.randn(50))
s.head()

df = pd.DataFrame(np.random.randn(50, 4), columns=list('ABCD'))
print(df.head())