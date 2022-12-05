from bs4 import BeautifulSoup
import requests
site='site_link'
details=requests.get(site)
content=details.text # get details in text format
savein=BeautifulSoup(content,'html')
print(savein)
