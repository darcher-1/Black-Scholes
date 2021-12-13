from bs4 import BeautifulSoup 
import requests 

def import_data(link: str):
    page = requests.get(link)
    result = BeautifulSoup(page.text, "html.parser")
    option_price = result.find("has_scrolled")
    print(option_price)