import requests
from bs4 import BeautifulSoup as bs

github_user=input("Input github user : ")
url = 'https://github.com/'+github_user
r = requests.get(url)
soup = bs(r.content,'html.parser')#returns the html page of our code

profie_image = soup.find('img',{'alt':'Avatar'})['src']
print(profie_image)