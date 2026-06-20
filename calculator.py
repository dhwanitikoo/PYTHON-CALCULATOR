import math as m
print("*********************************HELPS TO PERFORM SIMPLE OPERATIONS***********************************")
print("CHOOSE NUMBER ACCORDING TO THE OPERATION YOU WANT TO PERFORM")
print("TYPE 1 FOR ADDITION")
print("TYPE 2 FOR SUBTRACTION")
print("TYPE 3 FOR MULTIPLICATION")
print("TYPE 4 FOR DIVISION")
print("TYPE 5 FOR POWER OPERATION")
print("TYPE 6 FOR SQUARE ROOT")
print("TYPE 7 FOR TRIGNOMETRIC FUNCTION")
print("TYPE 8 FOR HISTORY")
choice=int(input("ENTER YOUR CHOICE : "))
if choice in [1,2,3,4,5]:
    a=int(input("ENTER  A NUMBER : "))
    b=int(input("ENTER A NUMBER : "))

if choice in [6,7]:
    a=int(input("ENTER  A NUMBER : "))
    

def add(x , y):
    return x+y

def subs(x , y):
    return x-y

def mul(x , y):
    return x*y

def div(x , y):
    return x/y

def power(x , y):
    return m.pow(x,y)

def square(x):
    return m.sqrt(x)

def trigno(x):
    return m.tan(x),m.sin(x),m.cos(x)

def history():
    f=open("history.txt","r")
    data=f.read()
    f.close()
    return data
    

def write_file():
    f=open("history.txt","w")
    if choice==1:
        f.write(str(add(a,b)))
    elif choice==2:
        f.write(str(subs(a,b)))
    elif choice==3:
        f.write(str(mul(a,b)))
    elif choice==4:
        f.write(str(div(a,b)))
    elif choice==5:
        f.write(str(power(a,b)))
    elif choice==6:
        f.write(str(square(a)))
    elif choice==7:
        f.write(str(trigno(a)))
    f.close()

if choice==1:
    print(add(a,b))
    write_file()
elif choice==2:
    print(subs(a,b))
    write_file()
elif choice==3:
    print(mul(a,b))
    write_file()
elif choice==4:
    print(div(a,b))
    write_file()
elif choice==5:
    print(power(a,b))
    write_file()
elif choice==6:
    print(square(a))
    write_file()
elif choice==7:
    print(trigno(a))
    write_file()
elif choice==8:
    print(history())
else:
    print("INVALID CHOICE")