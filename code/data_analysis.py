import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option("display.max_rows", 500)
pd.set_option("display.max_columns", 100)

# reading data files in a dataframe
data_df = pd.read_csv('output/t_2.csv')


# keeping only needed columns
data_df = data_df[['postal_code', 'bedrooms', 'bathrooms', 'price']]



# plotting count of each postal code
temp_df = pd.DataFrame(data_df['postal_code'].value_counts()).reset_index(drop=False)
fig = sns.barplot(x = temp_df['index'], y = temp_df['postal_code'], color="blue", palette = 'bright')
plt.xlabel("Postal Code")
plt.ylabel("No of listings")
plt.show()

# as we can see there are too many codes with 1 listings so lets filter them out
fig = sns.barplot(x = temp_df.loc[temp_df['postal_code'] > 2, 'index'], y = temp_df.loc[temp_df['postal_code'] > 2, 'postal_code'], color="blue", palette = 'bright')
plt.xticks(rotation='vertical')
plt.xlabel("Postal Code")
plt.ylabel("No of listings")
plt.show(fig)



# removing some of the error values from postal code
error_postal_code = ['No PostalCode','Toronto, ON','1 King St W','103 The Queensway','2 Rean Dr','North York, ON','541 Blackthorn Ave','33 Charles St E']
data_df = data_df.loc[~(data_df['postal_code'].isin(error_postal_code))]
data_df = data_df.loc[~(data_df['postal_code'].isnull())]

# lets separate postal code in 2 parts for separating area and postal code
data_df['city_area']='No_name'
data_df['city_area'] = data_df['postal_code'].apply(lambda x:str(x).split(',')[0])
data_df['city_area'].unique()

# keeping just postal code in postal_code columns
data_df['postal_code'] = data_df['postal_code'].apply(lambda x:str(x).split(',')[1])
data_df['postal_code'] = data_df['postal_code'].apply(lambda x:x.replace('ON','').strip())

# lets take a look into no of bedrooms 

data_df['bedrooms'].value_counts()
'''
Instead of removing 0 bedrooms and 0 bathrooms listings we will use it to calculate price on area level but filter it out if we are looking at pincode level and bedroom and bathroom specific
'''

data_df['upper_bedrooms'] = data_df['bedrooms'].apply(lambda x: str(x).split('+')[0])

data_df['upper_bedrooms'] = data_df['upper_bedrooms'].astype('int')

x = data_df['upper_bedrooms'].value_counts().index
y = data_df['upper_bedrooms'].value_counts().values
fig = sns.barplot(x = x, y = y, palette='bright', order=[0,1,2,3,4])
plt.xlabel("No of Bedrooms")
plt.ylabel("Number of Listings")
plt.show()

# working with bathrooms column - changing data type and plotting it
data_df.loc[data_df['bathrooms'].isnull(), 'bathrooms'] = 0
data_df['bathrooms'] = data_df['bathrooms'].astype('int')
fig = sns.barplot(x = data_df['bathrooms'].value_counts().index,
    y = data_df['bathrooms'].value_counts().values,
    palette='bright')
plt.xlabel("No of Bathrooms")
plt.ylabel("No of Listings")
plt.show()
  
# lets work with price column
data_df['price'] = data_df['price'].apply(lambda x: str(x).replace('$','').replace(',','').strip())
data_df['price'] = data_df['price'].astype('int')

# histogram of price
sns.distplot(data_df['price'],bins=50, kde=False, rug=True)
plt.xlabel('Price Points')
plt.ylabel('Number of Listings')
plt.show()

# from the graph and it looks like 100000 and less are either mistake or outlier
# removing these values
data_df = data_df.loc[data_df['price']>=100000]

# rearranging the columns
data_df = data_df[['city_area','postal_code','bedrooms','upper_bedrooms','bathrooms','price']]

# city wise prices for different bedrooms
sns.catplot(x='city_area',y='upper_bedrooms',kind='swarm',hue='bathrooms', data=data_df)
plt.yticks([0,1,2,3,4,5])
plt.show()


sns.barplot(x='city_area',y='price',estimator=np.mean,data=data_df)
plt.show()
    
sns.catplot(x="city_area", y="price", hue="upper_bedrooms", kind="bar", estimator=np.mean,data=data_df)
plt.show()


data_df.to_csv('data_sample.csv', index=False)

##################################################
