import pandas as pd
import os
import time
import datetime
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from bs4 import BeautifulSoup



def canada_post_postal_code(x):
    search_string = x[1]
    binary = FirefoxBinary('C:/Users/Prince.Atul/AppData/Local/Mozilla Firefox/firefox')
    driver = webdriver.Firefox(firefox_binary=binary)
    map_url = 'https://www.google.ca/maps/'
    driver.get(map_url)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="searchboxinput"]').send_keys(search_string)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="searchboxinput"]').send_keys(u'\ue007')
    time.sleep(3)
    try:
        postal_code = driver.find_element_by_xpath('/html/body/jsl/div[3]/div[9]/div[8]/div/div[1]/div/div/div[2]/div[1]/h2/span').text
        driver.close()
        return(postal_code)
    except:
        driver.close()
        return('No PostalCode')


def add_correction(x):
    x = x.split('-')
    return (x[-1])


def find_postal_code (file_path):
    data = pd.read_csv(file_path)
    data['modified_address'] = 'no_address'
    data['modified_address'] = data['address'].apply(add_correction)
    data['postal_code'] = 'NA'
    data['postal_code'] = data[['postal_code', 'modified_address']].apply(canada_post_postal_code, axis=1)
    # driver.close()
    return(data)


output_df = find_postal_code ('output/toronto.csv')


output_df.to_csv('output/t_2.csv', index=False)

