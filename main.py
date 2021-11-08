import SRC.cleaning_functions as fc

df = fc.load_csv()
#print(df)

df['Customer_loyalty'] = df['Prior_purchases'].apply(fc.loyal_customer)
#print(df['Customer_loyalty'].unique())

df['Customer_rating_range'] = df['Customer_rating'].apply(fc.customer_rating)
#print(df['Customer_rating_range'].unique())

df['Discount_%_range'] = df['Discount_offered'].apply(fc.percentage_range)
#print(df['Discount_%_range'].unique())

df.to_csv("data/full.csv")