# -*- coding: utf-8 -*-
# fun_class./data

def main():
    print("파일 불러오기 시작")
    with open("data/fun.txt",encoding="utf=8")as file:
        text = file.read()

    print("파일 불러오기 완료")

    n = 0
    for word in text.split():
        if word in ['개인정보','메타가']:
            n +=1
    print("단어의 갯수=",n)

if __name__ == "__main__":
   main()   
   
