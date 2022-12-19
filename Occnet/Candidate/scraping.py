import requests
from bs4 import BeautifulSoup

url = "https://www.linkedin.com/jobs/"
r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent,'html.parser')
para = soup.get_text()


print(para)