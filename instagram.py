#import requests and bs4 from pip
import requests
from bs4 import BeautifulSoup as bs
#input in terminal
instagram_user = input("Input Instagram user: ")
#get the url defined
url = "https://instagram.com/" +instagram_user
#request library using to get the url
r = requests.get(url)
#BeautifulSOup library gets the request and we give it a condition of request content and use the html parser
soup = bs(r.content, 'html.parser')
#we are getting the profile pic using the img tag and specifying which image by the alt tag in html page, receiving back the src tag
profile_pic = soup.find('img', {'alt' : ""}) ['src']
#print the src tag we saved in the profile_pic variable
print(profile_pic)