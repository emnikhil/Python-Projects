import requests
from bs4 import BeautifulSoup

username = input('Enter Instagram Username :')

res = requests.get('https://instagram.com/'+username)
soupData = BeautifulSoup(res.text, 'html.parser')
userInfo = soupData.find('meta', property = 'og:description')

print(userInfo.attrs['content'][:44])
