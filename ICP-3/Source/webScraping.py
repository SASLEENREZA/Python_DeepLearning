from bs4 import BeautifulSoup
import urllib.request
import requests

url = "https://en.wikipedia.org/wiki/Deep_learning" #define the url for the web scraping
source_code = urllib.request.urlopen(url)    #request the wiki url using url lib
plain_text = source_code   #assign the value
soup = BeautifulSoup(plain_text, "html.parser") #call the Beautifulsoup method for parsing wiki page html file
print("Title is: ",soup.title.string) #print the Title of the page
results = soup.find_all('a') #find the hyper links of wiki html page
for link in results:  #loop each hyper links
    print(link.get('href')) #print the links value
