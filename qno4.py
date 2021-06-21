# input ka use kar ke 3 alag variables mein 3 integers ka input lein. Input lene ke baad inn 3 mein se sabse bade number ko print karo Note: Isme aap loops ka use nahi kar sakte.
a=int(input("enter a number fist"))
b=int(input("enter a number second"))
c=int(input("enter a number third"))
if a>=b and a>=c:
    print("greter",a)
elif b>=c and b>=a:
    print("greter",b)
elif c>=a and c>=b:
    print("greter",c)
else:
    print("invited")