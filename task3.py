#3.	Write a Python function to check whether a number is completely divisible by another number. Accept two integer values form the user
first_num=int(input("Enter the first number: "))
sec_num=int(input("enter the second number: "))
div=first_num/sec_num
print(div)
if first_num%sec_num==0 :
    print("Both numbers are divisible")
else:
    print("Both numbers are not divisible")