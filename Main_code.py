from Holder import Holder
from Snake import Snake
from Function import Function

while(True):
    entry=input("Are you willing to play snake game(y/n) -> \n")
    if(entry.lower()=='n'):
        entry = input("Thank you for trying")
        break
    else:
        while(True):
            entry1=int(input("Press 1 to start New game\nPress 2 to start Quit game\n"))
            if(entry1==1):
                head=Holder(4,7)
                tail=Holder(4,2)
                body=[4,6,4,5,4,4,4,3]
                food=Holder(None,None)
                ref=0
                Score=0
                snack=Snake(head,tail,body,food,ref,Score)
                snack=Function.foodGenerator(snack)
                Function.desplay(snack)

                while(True):
                    entry2=input("Press W to click Uparrow \nPress A to click Leftarrow \nPress D to click Rightarrow \nPress S to click Downtarrow \nPress Q to go for menu\n")
                    if(entry2.lower()=='w'):
                        print("click up")
                        print(snack)
                        snack=Function.clickUp(snack)
                    if (entry2.lower() == 'a'):
                        print("click left")
                        snack = Function.clickLeft(snack)
                    if (entry2.lower() == 'd'):
                        print("click right")
                        snack = Function.clickRight(snack)
                    if (entry2.lower() == 's'):
                        print("click down")
                        snack = Function.clickdown(snack)
                    if (entry2.lower() == 'q'):
                        break
                    if (snack.get_ref()==1):
                        print("!!!!GAME OVER!!!!")
                        break

            else:
                print("Thank you for playing")
                break

