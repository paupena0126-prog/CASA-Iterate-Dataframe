import pandas as pd

df = pd.read_csv("big-mac-full-index.csv").query("index < 20")

for index, row in df.iterrows():
  print(row["name"], row["dollar_price"])

def print_country_price(row):
  print(row["name"], row["dollar_price"])

df.apply(print_country_price, axis=1)
