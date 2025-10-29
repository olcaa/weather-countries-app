import pandas as pd
from pandas import value_counts

df = pd.read_excel("Financial Sample.xlsx")

pd1 = df.head()
pd2 = df.tail(3)
pd3 = df.shape
pd4 = df.columns
pd5 = df.dtypes
pd6 = df.describe()
# print(pd6)

pd7 = df["Profit"].min()
# print(pd7)

pd8 = df[[" Sales", "Profit"]]
# print(pd8)

pd9 = df.loc[20:30]
pd10 = df.loc[20:30, ["Country", "Product", " Sales"]]
# print(pd10)

pd11 = df[df[" Sales"] > 50000]
# print(pd11)

pd12 = df[df["Country"] == "France"]
# print(pd12)

pd13 = df[(df[" Sales"] > 50000) & (df["Country"] == "France")]
# print(pd13)

mask = (df[" Sales"] > 50000) & (df["Country"] == "France")
pd14 = df.loc[mask]
pd15 = df.loc[mask, ["Country","Product"," Sales"]]

# print(pd15)

pd16 = df.sort_values(by=[" Sales"])
## pd17 = df.loc [pd16, ["Country"," Sales"]]
# print(pd16)

pd18 = df.sort_values(by=["Units Sold"], ascending=[False]).head(5)
# print(pd18)

# df["MarginPercent"] = df["Profit"] / df[" Sales"]
# df["Testowa"] = df["MarginPercent"] * df["Units Sold"]
# pd19 = df.loc[0:20, ["Product", "MarginPercent", "Testowa"]]
# # print(pd19)
# df.to_excel("nowy.xlsx")
# pd19.to_excel("nowy2.xlsx")

min_profit = df["Profit"].min()
print(min_profit)

max_profit = df["Profit"].max()
print(max_profit)

top_10_profit = df.sort_values(by=["Profit"]).head(10)
print(top_10_profit)

# df["Today"] = pd.to_datetime(df["Today"]).strftime("%d/%m/%Y")
# today_column = df.loc[0:20, ["Today"]]
# print(today_column)

de = df[df["Country"] == "Germany"]
print(de)

unique_countries = df["Country"].unique()
print(unique_countries)
countries_frequency = df.groupby("Country").size()
print(countries_frequency)

# countries_frequency2 = pd.Series().value_counts()
# print(countries_frequency2)

# cities = [
#     {
#         "name" : "Warszawa",
#         "country" : "Polska"
#     },
#     {
#         "name" : "Berlin",
#         "country" : "Niemcy"}
# ]
#
# df = pd.DataFrame.from_dict(cities)
#
# print(df)
#
# data = {
#  'name': ['Anna', 'Piotr', 'Katarzyna'],
#  'age': [28, 35, 42],
#  'city': ['Warszawa', 'Kraków', 'GdaEsk']
# }
# df2 = pd.DataFrame(data)
# print(df2)