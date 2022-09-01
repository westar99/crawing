from bs4 import BeautifulSoup

def main(url):
    print("Hello")
    # index.html 파일을 불러와서 
    soup = BeautifulSoup(open(url, encoding="utf-8"), 
                     "html.parser")
    final_text = soup.find('div', class_ = "human").find('p').get_text()    
    return final_text

if __name__ == "__main__":
    url = "index.html"
    text = main(url)
    print(text)