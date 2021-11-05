from bs4 import BeautifulSoup
import requests
def wikipedia(name):
    url = "https://en.wikipedia.org/wiki/" + name
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    return(soup.find_all('p')[1])
