import random as rd
main_cc=['R','G','B','Y','W']
com_col=[]
user_col=[]
# function for user input
def input_game():
    x1=input("Are you ready for colour guess work game:- Y or N ").lower()
    if x1=="y":
       user_col.clear()
       for i1 in range(4):
        print("Enter the digital code for the game from R,G,B,Y,W at",i1+1,"position:- ")
        col_input= input().upper()
        user_col.append(col_input)
    elif x1=="n":
         print("Thanks for showing up")
         quit()
    else:print("Enter the game status correctly")


inpos=0
copos=0
# function to check correct position
def pos_status():
    in_copos=0
    for i in range(4):
        if com_col[i]==user_col[i]:
            in_copos=1+in_copos
    return in_copos
# function to check character placed at worong position
# (for character present in random as base for comparsion)
def incor_char_status():
    in_inpos=0
    for z1 in range(4):
        if com_col[z1]!=user_col[z1]:
                for y1 in range(4):
                    if com_col[z1]==user_col[y1]:
                        in_inpos=1+in_inpos
                        break
                    
    return in_inpos
# function to check wrong character to 1:1 position comparision       
def incor_pos():
    z_inpos=0
    for j in range(4):
        if com_col[j]!=user_col[j]:
            z_inpos=1+z_inpos
    return z_inpos
#4 digit code generation           
for i in range(4):
    y1=rd.randint(0,4)
    com_col.append(main_cc[y1])
# Giving user 05 option guess it correctly
for i in range(5):
    print("Enter the input for try no",i+1)
    print(com_col)    
    input_game()
    print("computer code as ")
    print(com_col)
    print(user_col)
    pp1=pos_status()
    pp2=incor_char_status()   
    pp3=incor_pos()
    print("Correct position is ",pp1)
    print("Incorrect character position wrt to character present in baselist is",pp2)
    print("Incorrect postions ",pp3 )
    if pp1==4:
        print("You won")
        break
    else:print("Need attempt")
                



