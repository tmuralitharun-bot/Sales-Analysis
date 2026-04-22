#Load Data
import pandas as pd
import matplotlib as plt
df = pd.read_csv(r"C:\Users\tmura\OneDrive\Desktop\Python\Sales Data Analyst.csv")

## Data inspection
print(df.head())
print(df.info())
print(df.describe())

## Data Cleaning
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
df["Month"] = df['Order Date'].dt.month
print(df.groupby('Month')['Sales'].sum())
 
## Month Sale Trend
print(df.groupby('Region')['sales'].sum())
df.groupby('Month')['Sales'].sum().plot(kind='line')
plt.title("Monthly Sales Trend")
plt.show() 

## Region Sales
df.groupby('Region')['Sales'].sum().plot(kind='bar')  
plt.title("Region Sales") 
pt.show()

## Top 10 Products
top10 = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
top10.plot(kind='barh')
plt.title("Top 10 Product")
plt.show()