import argparse
import requests
import pandas as pd
import numpy as np

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import geopy
from geopy.geocoders import Nominatim

def get_zipcode(row,geolocator):
    location = geolocator.reverse(f"{row['Lat']}, {row['Lon']}")
    try:
        return location.raw['address']['postcode']
    except:
        return 0

def display_data(data):
    print("Data dimension:{}".format(np.shape(data)))
    print("First few lines of data:")
    print(data.head())

# zipcode(API), 房价（publice dataset）,shooting（网址）
# sample project（zipcode, API）

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--scrape", help="scrape data from Craigslist", action="store_true")
    parser.add_argument(
        "--static", help="display data dimension and head for the shooting csv data", action="store_true")
    args = parser.parse_args()

    if args.scrape:
        print("Scraping Craigslist Housing Data...")
        driver = webdriver.Chrome("chromedriver.exe")
        driver.get("https://losangeles.craigslist.org/search/hhh")

        price_list = []
        size_list = []
        lat_list = []
        lon_list = []
    
        li_elements = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, "//li[contains(@class, 'search-result')]")))
        for li in li_elements:
            try:
                price_element = li.find_element(
                    By.XPATH, ".//span[contains(@class, 'price')]")
                price_list.append(price_element.text)
            except:
                price_list.append(' ')

            try:
                size_element = li.find_element(By.XPATH,
                                               ".//span[contains(@class, 'housing')]/span[@class='post-sqft']")
                size_list.append(size_element.text)
            except:
                size_list.append(' ')

            try:
                location_element = li.find_element(By.XPATH, ".//div[contains(@class, 'meta')]")
                location_text = location_element.text.split('·')[-1]
                geolocator = Nominatim(user_agent="myGeocoder",timeout=10)
                print(location_text)
                location = geolocator.geocode(location_text)
                lat = location.raw['lat']
                lon = location.raw['lon']
                lon_list.append(lon)
                lat_list.append(lat)
                
            except:
                lon_list.append('')
                lat_list.append('')
                continue
            
        driver.quit()

        max_len = max(len(price_list), len(size_list))
        price_list.extend([' '] * (max_len - len(price_list)))
        size_list.extend([' '] * (max_len - len(size_list)))
        lon_list.extend([' '] * (max_len - len(lon_list)))
        lat_list.extend([' '] * (max_len - len(lat_list)))

        craiglist_df = pd.DataFrame(
            np.array([price_list, size_list,lon_list,lat_list]).T, columns=["Price", "Size",'Lon','Lat'])
        print("Craigslist Housing Data")
        display_data(craiglist_df)
    elif args.static:
        file_path = "Sheriff_All_Shootings_-_Incident_Summary_Count_-_2010_to_Present_(Deputy_Shootings).csv"
        shootings_data = pd.read_csv(file_path)
        print("Shooting Data")
        display_data(shootings_data)
    else:
        locator = Nominatim(user_agent="myGeocoder",timeout=10)

        df = pd.read_csv("./house_data.csv") 
        df['ZIP'] = df.apply(get_zipcode, geolocator=locator, axis=1)
        df.to_csv("./house_data_final.csv", index=False)
