# -*- coding: utf-8 -*-
# 상태(state)+행동(action)

class Person:
    """
    사람을 표현하는 클래스

    '''
    Attributes
    ----------- 
    name : str
        name of the person
    age : int
        age of the person

    Methods
    ---------
    info(additional=""):
        Print the person's name, age, and etc
    """    
    
    def __init__(self, name, age):
        """
        constructs all the necessary attributes for the person object

        Parameters
        -----------
            name : str
                name of the person
            age : int
                age of the person
        """
        self.name = name
        self.age =age

    def info(self, additional = None):
        """
        설명..

        Paremeters
        ---------
        addtional : str,
            More information that will be displayed(default is None)

        Returns
        --------
        None
        """

        print(f'My name is {self.name}.I am {self.age}years old')

if __name__ == "__main__":

    # 인스턴스화
    evan = Person("Evan",age = 20)
    print(evan.info())

    a = Person("A",10)
    print(a.info())

    print(Person.__doc__)
    #help(Person)