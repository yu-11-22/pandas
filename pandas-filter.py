# 載入 pandas 模組
import pandas as pd
data=pd.Series([30,15,20])
condition=data>18
filtereData=data[condition]
print(filtereData)

data=pd.Series(["您好","Python","Pandas"])
condition=data.str.contains("P")
filtereData=data[condition]
print(filtereData)

# 篩選練習 - DataFrame
data=pd.DataFrame({
    "name":["Amy","Bob","Charles"],
    "salary":[30000,50000,40000]
})
print(data)
condition=data["salary"]>=40000
filtereData=data[condition]
print(filtereData)