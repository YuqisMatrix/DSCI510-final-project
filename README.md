# HM5.py Readme

## Description
HM4.py is a Python script that scrapes housing data from Craigslist, displays data dimensions and head for the shooting csv data, and reads a CSV file containing house data and adds a new column with the corresponding zip code for each house.

Dataset access
1. Sheriff All Shootings - Incident Summary Count - 2010 to Present (Deputy Shootings)(https://data.lacounty.gov/datasets/lacounty::sheriff-all-shootings-incident-summary-count-2010-to-present-deputy-shootings/about)
2. House Prices in Los Angeles(https://losangeles.craigslist.org/search/hhh)
3. Zipcode API: We obtain the zip code given longitude and latitude by importing the geopy module. 


## Requirements
To run HM4.py, you will need to have the following installed:
- Python 3.x
- pandas
- selenium
- geopy
- numpy
- requests

You will also need to have a Chrome driver installed and in your PATH.
Notice! ! ! Before the code is executed, I used the Selenium library in Python when crawling data, which crawls data by simulating the behavior of users using a browser. A browser driver needs to be installed here. Since the Chrome browser driver is needed here, the driver name is "chromedriver.exe". This driver is already in the folder, but this driver can only be used for users whose Chrome browser version is "101.0.4951.XX". If your Chrome browser version is another version, please go to https://chromedriver.chromium.org/downloads website to download the corresponding driver and put it in this folder, then it can run successfully!

## Code Execution
HM4.py can be run in three different modes: static mode, crawl mode, and default mode.

### Static Mode (running time is about 1 seconds)
To run HM4.py in static mode, use the following command:

python HM4.py --static
This will display the data dimensions and head for the shooting csv data.

### Crawl Mode (running time is about 600 seconds)
To run HM4.py in crawl mode, use the following command:

python HM4.py --scrape
This will scrape housing data from Craigslist and display the resulting data in a pandas DataFrame.
We will scrape the Craigslist dataset, extract location information, and obtain latitude and longitude information for each house.

### Default Mode (running time is about 15 seconds)
To run HM4.py in default mode, use the following command:

python HM4.py 
This will read a CSV file containing house data and add a new column with the corresponding zip code for each house. The resulting DataFrame will be saved to a new CSV file.


## Data Sources
The data sources used in HM4.py are:
- Craigslist (for housing data)
- SheriffAllShootings-IncidentSummaryCount-2010toPresent(DeputyShootings).csv (for shooting data)
- house_data.csv (for house data)

## Shooting Data processing
python3 pre_shooting.py
The purpose of this program is to read a CSV file named "Sheriff_All_Shootings_-Incident_Summary_Count-2010_to_Present(Deputy_Shootings).csv", which contains information on police shooting incidents in the Los Angeles area. The program counts the number of shooting incidents that occurred in Los Angeles and adds the result to the end of each row. The program then saves the modified data into a new CSV file named "los_angeles_shootings.csv".

## Merge Data
python3 merge_data.py

The purpose of this program is to read in two CSV files, one containing information on houses and the other containing information on shooting incidents. The program merges the two data frames based on the "ZIP" field and increments the "shooting_num" column by the number of duplicates minus one for each "ZIP" that has multiple entries. The program then drops the duplicate entries based on the "ZIP" field and saves the merged data frame as a new CSV file named "los_angeles_house_shooting.csv".


## Analysis
python3 analysis.py

The purpose of this program is to read a CSV file named "los_angeles_house_shooting.csv", which contains data on rental prices and shooting incidents in the Los Angeles area. The program then calculates the Pearson correlation coefficient between rental prices and shooting incidents, and plots a scatter plot with a linear regression line to demonstrate the relationship between these two variables. Finally, the program saves the scatter plot as a file named "scatter_plot.png".

## Code extensibility:

1. The real estate data sources of other cities can be added. Now the code only covers the real estate data of Los Angeles, but if we want to expand to other cities, we need to modify the code to support the data sources of the city. It can also be parameterized, allowing the user to choose which cities to scrape.
2. Support data input and output formats. Now the code only supports input in CSV format. If you want to support other formats, the code needs to be extended. Different input and output formats can be supported by adding handlers for more input and output formats. These handlers can be format-specific file types or different API interfaces.
3. Can support custom functions. Sometimes users need to customize modules or functions for processing data or requesting data, and the code can be extended to support custom functions by adding modules or functions for data processing and requesting data. This will allow users to customize data processing and collection modules without modifying or extending the main program code.

## Code maintainability:

1. Change the data source or API key. In certain cases, the data source or API key may change, and if the code is not updated, incorrect data or request failures may occur. API keys and data sources can be defined as constants or configurations, and when needed, they are updated from a unified place.
2. Change the format and structure of the results returned by the API. If the format and structure of the API's return results changes, the code may fail to recognize the data and fail to execute. By establishing data input validation and data format validation methods, you can ensure that the correct data format is passed in and output, which will provide assurance when making sure the data is available.
3. Add, delete or change data. If the data changes, such as new rows are added, rows are removed, or the data format is changed, code execution may be affected. In this case, you can avoid problems by adding data validation to ensure that the data is loaded correctly, and increasing the flexibility of data query in the code.
4. Problems caused by package manager and dependent library version upgrades. Code may fail to execute or have unexpected issues when dependent libraries or packages are updated or upgraded. This can produce inconsistent and erroneous results when the code is run across different computers or servers. Virtual environments can be used to easily manage dependencies between different environments.

