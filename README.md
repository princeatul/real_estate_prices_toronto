# real_estate_prices_toronto

### Objective

This project was to craete an end to end data pipeline for getting real estate price points in toronto area and visualizing it. 

### Steps involved in this projects are:-
  1. Scrapping realtor.ca for starting data points
  2. Data Enrichment by adding postal codes for each address. I did this by scrapping search results on Google Map. 
  3. Data transformation and analysis 
  4. Visualizing the price points

### Part of this projects can be used for following exercises:-
  1. Scraping realtor.ca using python (Selenium and BeautifulSoup)
  2. Scraping seach result for pincodes on Google Map using Python (Selenium and BeautifulSoup)
  
### List of most relevant packages:- 
  1. Pandas
  2. Selenium
  3. BeautifulSoup
  4. Seaborn
  5. Folium
  
### References
I used code from this repo for drawing Choropleth map for Toronto. GeoJSon file for Toronto is not readily available so huge thanks to **A Gordon**. Relevant links are:-
  1. Medium post explaining this - [medium post](https://medium.com/dataexplorations/generating-geojson-file-for-toronto-fsas-9b478a059f04)
  2. GitHub Repo - [github_choropleth](https://github.com/ag2816/Visualizations/blob/master/OntarioFoliumMap.ipynb)
  Please check above links.
  
### Some of the created graphs are 
  ![no of listings by bedroom](https://github.com/princeatul/real_estate_prices_toronto/blob/master/graphs/bedrooms_number%20of%20listings.png)
  
  Looked into no of listings by no of bedrooms. 1 bedrooms apartment are the most common in Toronto area.
  
  ![no of listings by bathrooms](https://github.com/princeatul/real_estate_prices_toronto/blob/master/graphs/bathrooms_number%20of%20listings.png)
  
  No of lsitings by no of bathrooms. 1 bathrooms apartment are the most common. 
  
  ![Real estate price and number of listings](https://github.com/princeatul/real_estate_prices_toronto/blob/master/graphs/Price%20point_histogram.png)
  Created a histogram of price points. We can see that it is right skewed. One of the reason for thsi graph is the presence of all types of houses i.e. 2 bedrooms, 3 bedrooms and 4 bedrooms etc.
  
  
  ![Postal Code wise Listings](https://github.com/princeatul/real_estate_prices_toronto/blob/master/graphs/postal_code_frequency_more%20than%202.png)
In this graph, we can see no of listings for different postal code. I put a filter of no of listings more than 2 to focus more on high frequency postal code. It also helped in hightlighting some of the error in postal codes. 

  ![City_area_mean_price](https://github.com/princeatul/real_estate_prices_toronto/blob/master/graphs/city_area_price_bedrooms.png)
Drew mean price points for different area of toronto by no of bedrooms. 

  ![geo_json toronto all](https://github.com/princeatul/real_estate_prices_toronto/blob/master/graphs/geojson_all.PNG)
Choropleth map for toronto for all the listings

  ![geo_json toronto 2 bhk](https://github.com/princeatul/real_estate_prices_toronto/blob/master/graphs/geojson_2bhk.PNG)
Choropleth map for toronto for all the 2 bedrooms real estate listings

  ![geo_json toronto 3bhk](https://github.com/princeatul/real_estate_prices_toronto/blob/master/graphs/geojson_3bhk.PNG)
Choropleth map for toronto for all the 3 bedrooms real estate listings


I have also posted this project [here](https://yoursdata.net/project-from-scratch-scrapping-real-estate-prices-visualizing-it/)
