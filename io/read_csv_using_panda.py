import pandas as pd

df = pd.read_csv("output.csv")

# print (df['url'])

link = ['https://mydramalist.com/38301-romantic-doctor-teacher-kim-2']

if link[0] in df.values: 
    print ("weee")