from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def get_web_page(address):
	html = urlopen(address)
	page = html.read()
	return(page)

url = "https://www.lyricsondemand.com/s/smashingpumpkinslyrics/cherubrocklyrics.html"

a = get_web_page(url)

soup = BeautifulSoup(a,"html.parser")

links = soup.find_all('div', class_= "lcontent")



a = []
for link in links:
	a.append(link.get_text().replace("\n"," ").strip())

print(a)



#
#b = []
#for i in a:
#	b.append(i.replace("\n"," ").strip())

#print(b)







#soup = BeautifulSoup(a, "html.parser")

#soup.prettify

#tables = soup.find_all('a')

#for table in tables:
#	print(table)

