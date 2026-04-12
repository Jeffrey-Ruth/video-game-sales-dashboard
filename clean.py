import pandas as pd

df = pd.read_csv(r'C:/Portfolio Projects\data-analytics/video-game-sales/vgsales.csv')

#drop rows w/ missing year or publisher
df = df.dropna(subset=['Year', 'Publisher'])

#convert year to int
df['Year'] = df['Year'].astype(int)

df = df[df['Year'] <= 2016]

print(df.shape)
print(df['Year'].unique())

df.to_csv(r'C:/Portfolio Projects\data-analytics/video-game-sales/vgsales_clean.csv', index=False)
print("Saved!")