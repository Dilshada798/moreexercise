# num=int(input("enter the number"))
# i=1
# while i<num:
#     a=num%10
#     b=(num//10)%10
#     c=(num//10)//10
#     d=a+b+c
#     i=i+1
# if num%d==0:
#     print("harshad num",i) 
# else:
#     print("not harshad number",i)       



# harshad number1-1000
i=1
while i<1000:
    a=i%10
    b=(i//10)%10
    c=(i//10)//10
    d=a+b+c
    if i%d==0:
        print(i,"harshad num")
    else:
        print(i)
    i=i+1

