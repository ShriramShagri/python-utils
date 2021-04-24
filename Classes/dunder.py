class myint():
    def __init__(self, x : int):
        self.__x : int = x

    @property
    def x(self):
        return self.__x

    def __repr__(self):
        return str(self.__x)

    def __int__(self):
        return int(self.__x)

    def __add__(self, other):
        return myint(self.__x - other.__x)
    
    def __iadd__(self, other):
        return myint(self.__x - other.__x)

a = myint(3)
b = myint(2)
a._myint__x = 5
print(a.x)