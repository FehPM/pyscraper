# # import csv
# # import json
# # from bs4 import BeautifulSoup
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
 
# # option = webdriver.ChromeOptions()
# # option.add_argument('--headless')
# # option.add_argument('--no-sandbox')
# # option.add_argument('--disable-dev-sh-usage')
# # executable = "C:\chromedriver.exe"
# # driver = webdriver.Chrome(executable, options=option)

# # page = driver.get('https://www.imdb.com/chart/top/') # Getting page HTML through request
# # soup = BeautifulSoup(driver.page_source, 'html.parser') # Parsing content using beautifulsoup

# # totalScrapedInfo = [] # In this list we will save all the information we scrape
# # links = soup.select("table tbody tr td.titleColumn a") # Selecting all of the anchors with titles
# # first10 = links[:10] # Keep only the first 10 anchors
# # for anchor in first10:
# #     driver.get('https://www.imdb.com/' + anchor['href']) # Access the movie’s page 
#     infolist = driver.find_elements_by_css_selector('.ipc-inline-list')[0] # Find the first element with class ‘ipc-inline-list’
# #     informations = infolist.find_elements_by_css_selector("[role='presentation']") # Find all elements with role=’presentation’ from the first element with class ‘ipc-inline-list’
# #     scrapedInfo = {
# #         "title": anchor.text,
# #         "year": informations[0].text,
# #         "duration": informations[2].text,
# #     } # Save all the scraped information in a dictionary
# #     WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='firstListCardGroup-editorial']")))  # We are waiting for 5 seconds for our element with the attribute data-testid set as `firstListCardGroup-editorial`
# #     listElements = driver.find_elements_by_css_selector("[data-testid='firstListCardGroup-editorial'] .listName") # Extracting the editorial lists elements
# #     listNames = [] # Creating an empty list and then appending only the elements texts
# #     for el in listElements:
# #         listNames.append(el.text)
# #     scrapedInfo['editorial-list'] = listNames # Adding the editorial list names to our scrapedInfo dictionary
# #     totalScrapedInfo.append(scrapedInfo) # Append the dictionary to the totalScrapedInformation list
    
# # print(totalScrapedInfo) # Display the list with all the information we scraped







from types import NoneType
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from bs4 import BeautifulSoup

url = "https://pokemondb.net/pokedex/game/red-blue-yellow"
s = Service("C:\scrapdrivers\geckodriver.exe")
driver = webdriver.Firefox(service=s)
driver.implicitly_wait(30)
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser') 


list_pkm = []
pkms = soup.find_all("div", class_="infocard")

first10 = pkms[:10]
for pkm in pkms:
    
    print([pkm])

# ("https://youtu.be/XVv6mJpFOb0?t=2865")