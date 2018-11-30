import pandas as pd
import sys
import matplotlib.pyplot as plt
import numpy as np

sorted_data=sys.argv[1]

df= pd.read_csv(sorted_data,delimiter='\t',header=None)

print(df)

x=df.iloc[:,7].apply(np.log)
y=df.iloc[:,4]
langs=df.iloc[:,0]



plt.bar(x,y, width=1/5)
plt.xticks(x, langs)
plt.xlabel("LOG( Number of clips in TRAIN set )")
plt.ylabel("Improvement of Transfer, aka (Best Transfer CER - Baseline CER)")
plt.show()
