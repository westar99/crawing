from bs4 import BeautifulSoup

# index.html을 불러와서
soup = BeautifulSoup(open("index.html",encoding="utf-8"),
                     "html.parser")
#print(soup)
soup = soup.find('div',class_="computer")
#print(soup)
soup = soup.find('p')
#print(soup)

final_text = soup.get_text()
print(final_text)