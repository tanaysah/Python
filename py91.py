# Replace NaN with 0
df_filled = df.fillna(0)
print(df_filled)

# OR drop rows with missing values
df_dropped = df.dropna()
print(df_dropped)