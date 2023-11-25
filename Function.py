from setuptools import sic

from Holder import Holder
from Snake import Snake
import random

class Function:

    def foodGenerator(snack:Snake):

        head = snack.get_head()
        tail = snack.get_tail()
        body = snack.get_body()
        food = snack.get_food()
        ref = snack.get_ref()
        score = snack.get_score()
        touch = 1

        while(touch==1):
            touch = 0
            food.set_x(random.randint(0,9))
            food.set_y(random.randint(0,9))

            if(head.get_x()==food.get_x() and head.get_y()==food.get_y()):
                touch=1
            if (tail.get_x() == food.get_x() and tail.get_y() == food.get_y()):
                touch=1
            for i in range(0,len(body),2):
                if(body[i]==food.get_x() and body[i+1]==food.get_y()):
                    touch=1

        new_snack=Snake(head,tail,body,food,ref,score)

        return(new_snack)


    def desplay(snack:Snake):
        print(snack)
        matrix = [["*" for x in range(10)] for y in range(10)]
        body=snack.get_body()
        for i in range(10):
            for j in range(10):
                for k in range(0,len(body),2):
                    if(i==body[k] and j==body[k+1]):
                        matrix[i][j]='-'


                if(i==snack.get_head().get_x() and j==snack.get_head().get_y()):
                    matrix[i][j] = 'H'

                if (i == snack.get_tail().get_x() and j == snack.get_tail().get_y()):
                    matrix[i][j] = 'T'

                if (i == snack.get_food().get_x() and j == snack.get_food().get_y()):
                    matrix[i][j] = '$'

        print("# # # SCORE : "+str(snack.get_score())+" # # #")

        for i in range(10):
            for j in range(10):
                print(matrix[i][j], end =" ")
            print()

        print()
        print(("@ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @"))
        print()


    def changeBodyTail(snack:Snake,new_head:Holder):

        print(snack)
        head = snack.get_head()
        tail = snack.get_tail()
        body = snack.get_body()
        food = snack.get_food()
        ref = snack.get_ref()
        score = snack.get_score()


        tail.set_x(body[-2])
        tail.set_y(body[-1])

        body.pop(-1)
        body.pop(-1)

        body.insert(0,head.get_y())
        body.insert(0,head.get_x())

        new_snack=Snake(head,tail,body,food,ref,score)


        Function.desplay(new_snack)

        return(new_snack)



    def changeBodyTailFood(snack:Snake,new_head:Holder):

        print(snack)
        head = snack.get_head()
        tail = snack.get_tail()
        body = snack.get_body()
        food = snack.get_food()
        ref = snack.get_ref()
        score = snack.get_score()

        body.insert(0,head.get_y())
        body.insert(0,head.get_x())

        snack=Snake(new_head,tail,body,food,ref,score)

        snack=Function.foodGenerator(snack)


        Function.desplay(snack)

        return(snack)




    def clickUp(snack:Snake):
        head=snack.get_head()
        tail=snack.get_tail()
        body=snack.get_body()
        food = snack.get_food()

        new_head=Holder(head.get_x()-1,head.get_y())

        if(new_head.get_x()==-1):
            new_head.set_x(9)

        new_snack=Function.decisionMaking(snack,new_head)
        return (new_snack)

    def clickdown(snack:Snake):
        head=snack.get_head()
        tail=snack.get_tail()
        body=snack.get_body()
        food = snack.get_food()

        new_head=Holder(head.get_x()+1,head.get_y())

        if(new_head.get_x()==10):
            new_head.set_x(0)

        new_snack=Function.decisionMaking(snack,new_head)
        return (new_snack)

    def clickRight(snack:Snake):
        head=snack.get_head()
        tail=snack.get_tail()
        body=snack.get_body()
        food = snack.get_food()

        new_head=Holder(head.get_x(),head.get_y()+1)

        if(new_head.get_y()==10):
            new_head.set_y(0)

        new_snack=Function.decisionMaking(snack,new_head)
        return (new_snack)

    def clickLeft(snack:Snake):
        head=snack.get_head()
        tail=snack.get_tail()
        body=snack.get_body()
        food = snack.get_food()

        new_head=Holder(head.get_x(),head.get_y()-1)

        if(new_head.get_y()==-1):
            new_head.set_y(9)

        new_snack=Function.decisionMaking(snack,new_head)
        return (new_snack)

    def  checkBodytouch(snack:Snake,new_head:Holder):
        print(snack,"checkBodytouch S")
        head = snack.get_head()
        tail = snack.get_tail()
        body = snack.get_body()
        food = snack.get_food()
        ref = 0
        score = snack.get_score()

        if (tail.get_x() == new_head.get_x() and tail.get_y() == new_head.get_y()):
            ref=1
        for i in range(0, len(body), 2):
            if (body[i] == new_head.get_x() and body[i + 1] == new_head.get_y()):
                ref=1
        new_snack=Snake(head,tail,body,food,ref,score)
        return (new_snack)


    def  checkfoodtouch(snack:Snake,new_head:Holder):
        print(snack,"checkBodytouch S")
        head = snack.get_head()
        tail = snack.get_tail()
        body = snack.get_body()
        food = snack.get_food()
        ref = 0
        score = snack.get_score()

        if (food.get_x() == new_head.get_x() and food.get_y() == new_head.get_y()):
            print("food touch")
            score+=1
            ref=1
        new_snack=Snake(head,tail,body,food,ref,score)

        return(new_snack)

    def decisionMaking(snack:Snake,new_head:Holder):

        head = snack.get_head()
        tail = snack.get_tail()
        body = snack.get_body()
        food = snack.get_food()
        ref = snack.get_ref()
        score = snack.get_score()

        temp_snack = Function.checkfoodtouch(snack,new_head)

        if(temp_snack.get_ref()==1):
            snack=Function.changeBodyTailFood(temp_snack,new_head)
            snack = Snake(new_head,snack.get_tail(),snack.get_body(),snack.get_food(),0,snack.get_score())
            return(snack)


        else:
            snack = Function.changeBodyTail(temp_snack, new_head)
            snack = Function.checkBodytouch(snack, new_head)
            if(snack.get_ref()==0):
                snack = Snake(new_head,snack.get_tail(),snack.get_body(),snack.get_food(),snack.get_ref(),snack.get_score())
                Function.desplay(snack)
                return(snack)
            else:
                snack = Snake(new_head,snack.get_tail(),snack.get_body(),snack.get_food(),snack.get_ref(),snack.get_score())
                return (snack)











