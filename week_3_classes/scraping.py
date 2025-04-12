import requests
from bs4 import BeautifulSoup

url= "https://www.microsoft.com/en-us/"
response=requests.get(url)
print(response)

if response.status_code==200:
    print("Request succesful")
else:
    print("Request not successful")


