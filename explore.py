import pandas as pd

df = pd.read_csv(r'C:/Portfolio Projects\data-analytics/video-game-sales/vgsales.csv')

print(df.head())
print(df.shape)
print(df.info())