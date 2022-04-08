from re import T
import pandas as pd
import numpy as np
df = pd.read_csv('testkey.txt', delimiter="\n") 
df2= np.unique(df)
print(df2)
###

###
#Have to delete the space between ;i, and add the title by yourself in the end and replace $ by 7 spaaces.