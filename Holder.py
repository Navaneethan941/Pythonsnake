class Holder:
    __x=None
    __y=None

    def __init__(self, x,y):
        self.__x = x
        self.__y = y

    def set_x(self, x):
        self.__x = x

    def get_x(self):
        return (self.__x)

    def set_y(self, y):
        self.__y = y

    def get_y(self):
        return (self.__y)

    def __str__(self):
        return f"{self.__x},{ self.__y}"

