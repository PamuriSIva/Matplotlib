# -*- coding: utf-8 -*-
"""Assessment2B.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vid2f0CSHZPwClCVlbiKu2z6eyhIIviv

###### Assessment

###### I am going to provide two .csv files , you are supposed to work on them and have to provide solutions to the following problems

###### import necessary libraries
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""###### merge those two csv files (after getting as dataframes, get them as a single dataframe)"""

import pandas as pd
  
# merging two csv files
df = pd.concat(
    map(pd.read_csv, ['college_1.csv', 'college_2.csv']), ignore_index=True)
print(df.to_string())

"""###### Take each csv file , split that csv file into multiple categories (example csv files are added in the repo)

###### consider if the codekata score exceeds 15000 points(present week) then make a csv on those observations as Exceeded expectations.csv

###### if  10000<codekata score<15000   (Reached_expectations.csv)

###### if  7000<codekata score<10000   (Needs_Improvement.csv)

###### if  codekate score < 7000        (Unsatisfactory.csv)
"""

df = pd.concat(
    map(pd.read_csv, ['college_1.csv', 'college_2.csv']), ignore_index=True)
if



"""###### Average of previous week geekions vs this week geekions (i.e Previous Geekions vs CodeKata Score)"""

avg = ['Previous Geekions', 'CodeKata Score']

df[avg].mean()

"""###### No of students participated """

df_no_of_students = df.set_index(['Name'])
print(len(df_no_of_students))

print(len(df))

"""###### #Average completion of python course or my_sql or python english or computational thinking"""

avg = ['', 'CodeKata Score']

df[avg].mean()

"""###### rising star of the week (top 3 candidate who performed well in that particular week)"""

df['Rising'].nlargest(n=3)

"""###### Shining stars of the week (top 3 candidates who has highest geekions)"""

df['CodeKata Score'].nlargest(n=3)

"""###### Department wise codekata performence (pie chart)"""

df = pd.concat(
    map(pd.read_csv, ['college_1.csv', 'college_2.csv']), ignore_index=True)
Dept=df["Department"]
Perf=df["CodeKata Score"]
colors=["#1f77b4", "#ff7f0e"]
plt.pie(Perf,labels=Dept,colors=colors,autopct='%1.1f%%',shadow=True,startangle=50)
plt.title = ('Dept Wise Performacne')
plt.show()

"""###### Department wise toppers (horizantal bar graph or any visual representations of your choice)"""

# reading the database
df = pd.concat(
    map(pd.read_csv, ['college_1.csv', 'college_2.csv']), ignore_index=True)
plt.bar(df['Department'], df['CodeKata Score'])
plt.xlabel('Department')
plt.ylabel('CodeKata Score')
plt.show()

import matplotlib.pyplot as plt
x  = np.array["Department"]
y = np.array["CodeKata"]
plt.barh(x,y)
plt.show()





