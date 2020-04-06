import numpy as np
import pandas as pd

mat = np.arange(0, 50).reshape(5, 10)
print(mat)

# with pandas we do like this and give column and rows beside the matrics
df = pd.DataFrame(data=mat)
print(df)

# we can also label our dataframe by adding column label index by adding index to data frame
