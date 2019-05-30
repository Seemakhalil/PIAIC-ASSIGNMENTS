num=int(input("Enter number of rows: "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(i,end="")
    print()
for i in range(num,0,-1):
    for j in range(1,i):
        print(i ,end="")
    print()
