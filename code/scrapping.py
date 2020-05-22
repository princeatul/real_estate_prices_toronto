# loading required packages
import pandas as pd
import os
import time
import datetime
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from bs4 import BeautifulSoup

# initializing needed variables
realtor_url = 'https://www.realtor.ca/on/toronto/real-estate-for-sale'
click_next_button = "/html/body/form/div[5]/div[2]/span/div/div[4]/div[3]/span/span/div/a[3]"

# launching forefox webdriver
binary = FirefoxBinary('C:/Users/Prince.Atul/AppData/Local/Mozilla Firefox/firefox')
driver = webdriver.Firefox(firefox_binary=binary)


def scrapping_function(current_url, click_next_button):
    driver.get(current_url)
    i = 1
    next_page_true = True
    while next_page_true:
        page = driver.page_source
        file_ = open('saved_pages/toronto/page_{}.html'.format(i), 'w')
        file_.write(page)
        file_.close()
        page_url = driver.current_url
        elem = driver.find_element_by_xpath(click_next_button)
        elem.click()
        time.sleep(2)
        page_url_next = driver.current_url
        if page_url == page_url_next:
            next_page_true = False
        else:
            i += 1

# calling scrapping function
scrapping_function(realtor_url, click_next_button)
driver.close()

# getting data from each pages

toronto_df = pd.DataFrame()
for file in os.listdir('saved_pages/toronto'):
    html_file = 'saved_pages/toronto/{}'.format(file)
    soup = BeautifulSoup(open(html_file), "html.parser")
    data = soup.find_all(class_="cardCon")

    for i, elem in enumerate(data):
        price = data[i].find(class_="listingCardPrice").get_text()
        address = data[i].find(class_="listingCardAddress").get_text()
        rooms = data[i].find_all(class_="listingCardIconNum")
        bedrooms = rooms[0].get_text()
        bathrooms = rooms[1].get_text()
        try:
            row_df = pd.DataFrame({'price': [price],
                        'address': [address],
                        'bedrooms': [bedrooms],
                        'bathrooms': [bathrooms],
                        'page': [file]})
            toronto_df = pd.concat([toronto_df, row_df])
            del row_df
        except:
            print("Error in record_{}".format(i))


# cleaning dataframe 
def cleaning_address(x):
    return (x.replace("\n", "").strip())

toronto_df['address'] = toronto_df['address'].apply(cleaning_address)
    

# saving data file 
toronto_df.to_csv('output/toronto.csv', index=False)



    


