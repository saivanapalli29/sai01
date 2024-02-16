"""height=int(input("enter a height:"))
if(height>3):
    print("token is required")
    print("buy token")
    print("now you can board the metro")
else:
    print("token is not required")"""
#  if else and nested if
height=int(input("enter a  height in feats:"))
if(height>=4):
    print("you can ride")
    age=int(input("enter age:"))
    if(age<=10):
        print("pay 100 rs")
    elif(age<=12):
        print("pay 150 rs")
    elif(age<=15):
        print("pay 200 rs")
    elif(age<=20):
        print("pay 300 rs")
    else:
        print("pay 500 rs")
else:
    print("you are not eligible")
print("bye")