from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import geopy
from geopy.geocoders import Nominatim


driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://losangeles.craigslist.org/search/hhh")

price_list = []
size_list = []
lat_list = []
lon_list = []

file  = open('house_data.csv', 'w', newline='')
writer = csv.writer(file)
writer.writerow(['Price', 'Size','Lon','Lat'])
        

li_elements = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "//li[contains(@class, 'search-result')]")))
# print(f'The number of li elements: {len(li_elements)}')
for li in li_elements:
    try:
        price_element = li.find_element(By.XPATH, ".//span[contains(@class, 'price')]")
        price_list.append(price_element.text)
    except:
        price_list.append('')
        continue
    try:
        size_element = li.find_element(By.XPATH, ".//span[contains(@class, 'housing')]/span[@class='post-sqft']")
        size_list.append(size_element.text)
    except:
        size_list.append('')
        continue

    
    # try:
    if True:
        location_element = li.find_element(By.XPATH, ".//div[contains(@class, 'meta')]")
        location_text = location_element.text.split('·')[-1]
        # locations_list.append(location_text)
        geolocator = Nominatim(user_agent="myGeocoder",timeout=10)
        print(location_text)
        # if True:
        try:
            location = geolocator.geocode(location_text)
        
            lat = location.raw['lat']
            lon = location.raw['lon']
            lon_list.append(lon)
            lat_list.append(lat)
        except:
            lon_list.append('')
            lat_list.append('')
            continue
            
    writer.writerow([price_list[-1], size_list[-1],lon_list[-1],lat_list[-1]])

   

