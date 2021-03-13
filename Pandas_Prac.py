import pandas as pd
import matplotlib.pyplot as plt
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number

print('Pandas practice document')
print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)

#Creating data to work on - Baby names and corresponding numbers born in 1880
names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]
baby_data = list(zip(names, births))
print(baby_data)

#Creating a dataframe - Object holding the contents of the dataset (Similar to SQL)
df = pd.DataFrame(data = baby_data, columns = ['Names', 'Numbers'])
print(df)

#Creating a .csv file
df.to_csv('births1880.csv',index=False,header=False)

#Reading .csv file
Location = r'/home/mcg33/$User/Coding_practice/Python_practice/births1880.csv'
df = pd.read_csv(Location, names = ['Names', 'Numbers']) #Header = None - numbers the columns

#Checking data types
print(df.dtypes)
print(df.Numbers.dtype)

#Basic analysis
print('Max value of the numbers row: ', df['Numbers'].max()) #Max value of the 'Numbers' row

#Basic graph
MaxValue = df['Numbers'].max()
MaxName = df['Names'][df['Numbers'] == df['Numbers'].max()].values

#Text to display on graph
Text = str(MaxValue) + " - " + MaxName

#Add text to graph
plt.annotate(Text, xy=(1, MaxValue), 
                   xytext=(25, 0), 
                   xycoords=('axes fraction', 'data'), 
                   textcoords='offset points',
                   arrowprops=dict(arrowstyle='-|>'))

print("The most popular name")
df[df['Numbers'] == df['Numbers'].max()]