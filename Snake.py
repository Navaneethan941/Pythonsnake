from Holder import Holder

class Snake:
    __head=None
    __tail=None
    __body=None
    __food=None
    __ref=None
    __score=None

    def __init__(self,head:Holder,tail:Holder,body:list,food:Holder,ref:int,score:int):
        self.__head=head
        self.__tail=tail
        self.__body=body
        self.__food=food
        self.__ref=ref
        self.__score=score

    def set_head(self,head:Holder):
        self.__head = head

    def get_head(self):
        return(self.__head)

    def set_tail(self, tail: Holder):
        self.__tail = tail

    def get_tail(self):
        return (self.__tail)

    def set_body(self, body:list):
        self.__tail = body

    def get_body(self):
        return (self.__body)

    def set_food(self, food:Holder):
        self.__tail = food

    def get_food(self):
        return (self.__food)

    def set_ref(self, ref:int):
        self.__tail = ref

    def get_ref(self):
        return (self.__ref)

    def set_score(self, score:int):
        self.__tail = score

    def get_score(self):
        return (self.__score)

    def __str__(self):
        return f"head({self.__head.get_x()},{self.__head.get_y()}), tail({self.__tail.get_x()},{self.__tail.get_y()}),body({self.__body}),food{self.__food},ref{self.__ref},score{self.__score}"

