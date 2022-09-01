# -*- coding: utf-8 -*-

class Person:

    #attribute
    def __init__ (self, name, age):
        self.name = name
        self.age = age

    def whoAmI(self):
        print("I am Person Class")

    def sining(self, song):
        return "{} {}을 노래합니다.".format(self.name, song)

    def dancing(self):
        return "{} 현재 춤을 춘다.".format(self.name)

class korean(Person):

    def __init__(self, name, age):
        super().__init__(name,age)
        print("korean Class is ready!")

    def whoAmI(self):
        print("I{} am Korean class")

    def study(self):
        print("{}fast runner")

class Japan(Person):

    def __init__(self, name, age):
        super().__init__(name,age)
        print("japan Class is ready!")

    def whoAmI(self):
        print("I am japan class")

    def lie(self):
        print("거짓말장이")



if __name__=="__main__":
    kim = Person("kim",30)
    kim.whoAmI()
    print(kim.dancing())
    print(kim.sining("ㅋㅋㅋ"))

    kor_kim = korean("kor_kim",20)
    print(kor_kim.sining("ooo")) ##상속을 함

    jap_naka = Japan("jap_naka",30)
    #아래 두개는 제팬클래스
    jap_naka.whoAmI()
    jap_naka.lie()
    #상속 클래스python step9.py
    print(jap_naka.dancing()) ##상속을 함