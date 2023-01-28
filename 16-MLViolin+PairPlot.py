#importing libraries
#pip install numpy, pandas etc in the terminal
import numpy as np
import pandas as pd
import seaborn as sns
sns.set_palette('husl')
import matplotlib.pyplot as plt
# %matplotlib inline      
#this command isnt valid here. try google collab
#but codes work fine without it ;)


#Load The Data
url='https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv' 
col_name = ['sepal-length','sepal-width','petal-length','petal-width','class']
dataset = pd.read_csv(url,names = col_name)

# Violin Plot
sns.violinplot(y='class', x='sepal-length', data=dataset, inner='quartile')
plt.show()

# Pair Plot
sns.pairplot(dataset, hue='class', markers='+')
plt.show()