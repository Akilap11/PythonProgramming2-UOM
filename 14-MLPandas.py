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



print('Dataset Size')
print(dataset.shape)

print('First Five Rows of the Dataset')
print(dataset.head())

print('Summary Statistics of the Dataset') #find min max of a attribute
print(dataset.describe())

print('Data Types and Memmory Usage')
print(dataset.info())

print('classes and the number of examples')
print(dataset['class'].value_counts())

#print(dataset.ndim)
#print(dataset.values)
#print(dataset.axes)
#print(dataset.size)
#print(dataset.size)