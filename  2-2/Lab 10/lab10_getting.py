import requests
from bs4 import BeautifulSoup

url = "https://www.sc.su.ac.th"
res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")
text = soup.get_text()
print(text)