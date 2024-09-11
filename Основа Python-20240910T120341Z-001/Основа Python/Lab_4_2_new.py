class TextStyle:
    BOLD = '\033[1m'
    END = '\033[0m'

class TextColor:
    RED = '\033[91m'
    END = '\033[0m'

class remembers_decorator:
    def __init__(self, name, n=1):
        self.__name = name
        self.__n = n
        self.members = {}

    def __call__(self, *args, **kwargs):
        obj = (args)
        try:
            if obj in self.members:
                raise ValueError(f"Обьект по имени {TextStyle.BOLD}{args[0]}{TextStyle.END}{TextColor.RED} уже существует!")
            members = self.__name(*args, **kwargs)
            self.members[obj] = members
            return members
        except ValueError as e:
            print(f"Был вызван исключения: {TextColor.RED}{e}{TextColor.END}")


@remembers_decorator
class obj_new:
    def __init__(self, name, n=1):
        self.__name = name
        self.__n = n

    @property
    def name(self):
        return self.__name

    @property
    def n(self):
        return self.__n

    @n.setter
    def n(self,n):
        if (n > 0):
            self.__n = n
        else:
            print("Введите число больше 0")

    def __mul__(self, other):
        self.__n = self.__n*other

    def display_info(self):
        print(self.__name,"Существует", self.__n, "штук")








Pen = obj_new("Pen")
print(Pen.name)
Pen.display_info()
Pen.n = 7
Pen.display_info()
Pen*5
Pen.display_info()
Book = obj_new("Pen")
Pen.display_info()




