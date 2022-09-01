import requests
from bs4 import BeautifulSoup
import pandas as pd

def crawling(soup): # 크롤링할 클래스 명을 찾아서 넣으면 됨
  div = soup.find("div",class_ = "list_issue")
  #print(div)
  result = []

  for a in div.find_all("a"):
    #print(a.get_text())
    result.append(a.get_text())

  links = []
  for a in div.find_all("a"):
    #print(a['href'])
    links.append(a['href'])

  #print(result)
  #print(links)
  new_list = pd.DataFrame({'제목': result,'링크': links})
  print(new_list) 
  

def main():
  print("Main")

  url ="https://www.naver.com/"
  req = requests.get(url)
  soup = BeautifulSoup(req.text,"html.parser")

  crawling(soup)


if __name__ == "__main__":
  main()