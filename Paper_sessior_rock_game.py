import random as rd 
input1 = input("do you want to play rock/paper/sessior game? Answer in yes/no only:").lower()
l1=['rock','sessior','paper']
us1=0
cus1=0
if input1=='yes':
    while True:
        user_input =input("enter the rock/paper/sessior or q to quit")
        if user_input =='q':
            break
        elif  user_input not in l1:
            continue
        r1 = rd.randrange(0,2)
        print("computer input",l1[r1])
        # rock is 1, paper is 2, sessior is 3
        computer_pick=l1[r1]
        print("Computer pick is",computer_pick)

        if user_input=="paper":
            if computer_pick =="paper":
                print("Tie")
            elif computer_pick =="sessior":
                print("computer wins")
                cus1=cus1+1
            else:
                print("user wins")
                us1=1+us1

        elif user_input=="sessior":
            if computer_pick =="paper":
                print("user wins")
                us1=1+us1
            elif computer_pick =="sessior":
                print("tie")
            else:
                print("computer wins")
                cus1=cus1+1
        elif user_input=="rock":
            if computer_pick =="paper":
                print("computer wins")
                cus1=cus1+1
            elif computer_pick =="sessior":
                print("user wins")
                us1=1+us1
            else:print("Tie")
            continue
    print('User_score',us1)
    print("computer_score",cus1)

