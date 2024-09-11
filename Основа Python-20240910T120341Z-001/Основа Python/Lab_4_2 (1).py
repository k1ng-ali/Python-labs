
members = {}
class remember(cls):
    members = {}
    obj = cls
    if obj in members:
        print("Обьект уже сушествует")
    else:
        members[obj]=1
        return cls

@remember        
class test:
    
    def __init__(self, name, n):
        self.__name = name
        self.__n=n
        
    @property
    def n(self):
        return self.__n

    @n.setter
    def n(self, n):
        if n > 0:
            self.__n = n
            obj = self.__name
            members[obj]=n
        else:
            print("Введите положительное число")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self,x):
        if x>0:
            self.__n = self.__n*x
        else:
            print("Введите положительное число")
            

       

    def display_info(self):
        print(self.__name, "Существует", self.__n, "штук")

class myclass(test):
    def __init__(self, name, x):
        self.__x = x
        super().__init__(name)

    def  __mul__(self,other):        
        self.n = self.__x * other
        print(self.__x*other)

    

Pen = test("pen")
Pen.display_info()
Pen.n = 3
Pen.display_info()
Pen.x = 4
Pen.display_info()
Pen = remember("pen", 3)
Pen = myclass("pen2", 5)
Pen*5
Pen.display_info()

