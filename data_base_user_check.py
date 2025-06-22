import csv
# creating a csv file with single user details
'''with open("user_database.csv", mode="w", newline="") as f:
   writer = csv.writer(f, delimiter=",")
   writer.writerow( ["Name"] )
   writer.writerow( ["Craig Lou"] )'''
# check function to check the user_id status in the database
def check():
   with open("user_database.csv", mode="r") as f:
    reader=csv.reader(f,delimiter=",")
    c11=0
    for i in reader:
      if a1 ==i[0]:
       c11=1+c11
      else:
          c11=c11+0
    if c11>0:
      print("User present")
    else:
          print("User not present")
          s1= input("Do you want to register yes/no ").lower()
          if s1=='yes':
             register_check()
          elif s1=='no':
             quit()
# register the new user in the data_base
def register_check():
      c12=input("Enter the user id for register : ").lower()
      with open("user_database.csv", mode="a",newline="") as f1: 
         writer = csv.writer(f1)
         writer.writerow([c12])
# asking the user to share the user_id detail and check in data_base 
# and if new register the user_id in data_base                 
while True:
   a1=input("Enter the user name ").lower()
   check()
   q11=input("To exist Enter q or press other key to continue:").lower()
   if q11=="q":
      quit()