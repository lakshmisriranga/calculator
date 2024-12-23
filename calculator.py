print("***It is my calculator***")
a=int(input("please enter your first number\n"))
b=int(input("please enter your second number\n"))
n=int(input("how many calculations do you want.....??"))
for l in range(0,n):
    print("please choose your option")
    print(" 1 for addition\n 2 for substraction\n 3 for multiplication\n 4 for division\n 5 for factorial\n 6 for add in between number")
    p=int(input())
    if p==1:
        print(a+b)
    elif p==2:
        print(a-b)
    elif p==3:
        print(a*b)
    elif p==4:
        if a>b:
            print(a/b)
        else:
            print(b/a)
    elif p==5:
        f=1
        f1=1
        for i in range(1,a+1):
            f=f*i
        print(f)
        for j in range(1,b+1):
            f1=f1*j
        print(f1)
    elif p==6:
        su=0
        s=0
        if a<b:
            for k in range(a,b+1):
                su=su+k
            print(su)
        else:
            for h in range(b,a+1):
                s=s+h
            print(s)
    else:
        print("please enter above option only")
print("*** Thank you ***")
