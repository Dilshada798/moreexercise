# 1 se 1000 tak saare numbers print karne ka loop likho. Lekin * Agar number 3 se divisible hai toh "nav" print karvao.

# Agar number 7 se divisible hai toh "gurukul" print karvao.
# Agar number 21 se divisible hai toh "navgurukul" print karvao.

i=0
while i <=100:
    num=int(input("enter the no."))
    if num%3==0:
        print("nav")
    elif num%7==0:
        print("gurukul")
    elif num%21==0:
        print("navgurukul")

i=i+1