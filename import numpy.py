import numpy as np
import pandas as pd
marks = np.array([75,82,91,68,88,99])
print("Marks :",marks)
print(type(marks))
emp = np.array([
    [5,600,82],
    [7,72000,91],
    [3,48000,76],
])
print("Employee Data:\n")
print(emp)
print(marks.shape)
print(emp.shape)

print(marks.ndim)
print(emp.ndim)
print(marks+5000)
print(marks-5000)
print(marks*5000)
print(marks/2)
print(marks <80)
print(marks[0])
print(marks[-1])
print(marks[1:5])
print(marks[1:5:2])

print(emp)
print(emp[0][1])
print(emp[:,0]) #first column
print(emp[:,:1]) #first column
print(emp[:,:2]) #first two column

print(np.mean(marks))
print(np.max(marks))
print(np.min(marks))
print(np.median(marks))
print(np.std(marks))

scores = pd.Series([78,85,91,67,88],
                index=["Alice","Bob","Charlie","Sushma","Ramanad"])
print(scores)
print(scores["Alice"])
print(scores[scores > 80])

data = {
    "Name":["Alice","Bob","Charlie","Sushma","Ramanad"],
    "Age":[25,26,34,56,78],
    "Salary":[55000,65000,65500,7200,48000],
    "Department":["IT","Finance","HR","ASDC","Army"]
}
print(data)
df=pd.DataFrame(data)
print(df)
print(df.iloc[2])
print(df.iloc[2,0])
print(df["Name"])


df1 = pd.read_csv(".\\data\\module2_numpy_pandas_demo_data.csv")
print(df1)
print(df1.head())
print(df1.head(12)) #12 rows
print(df1.tail()) # Last 5 data
print(df1.tail(12)) # Last 12 data
print(df1.shape) # give counts of rows and column
print(df1.columns) # give column name
print(df1.dtypes)
print(df1.info())
print(df1.describe())
print(df1.describe(include="object"))
print(df1.describe(include="all"))
print(df1.isnull().sum())
print(df1.isnull().mean()*100) # % 
print(df1[df1.isnull().any(axis=1)])

# df1["Monthly_Salary"]=df1["Monthly_Salary"].fillna(df1["Monthly_Salary"].mean())
print(df.head)
print(df1.iloc[17])
df1["Performance_Score"]=df1["Performance_Score"].fillna(df1["Performance_Score"].mean())
print(df1.iloc[8])
print(df1.iloc[24])
print(df1.isnull().sum())
