#Dudu KABAKÇI 

#TASK-1

age = int(input("Enter your age: "))

print(age>18 and age<65)
print(age<18 or age>65)
print(not(age==25))


#TASK-2

num = int(input("Enter the num: "))
if num%2==0:
    if num>0:
       print("Number is even and positive: True")
    else:
       print("Number is even and negative: False ")
else:
    print("Number is odd: False")
    
    
#TASK-3

age = int(input("Enter your age: "))
drivingLicence = input("If you have a driver's licence, enter True otherwise enter False ")

if age>=18 and drivingLicence:
    print("You can drive")
else:
    print("You can't drive")
