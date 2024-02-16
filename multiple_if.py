height=int(input("enter height in mtrs:"))
bill=0
if(height>=3):
   print("you can ride")
   age=int(input("enter your age:"))
   if(age<=12):
      bill=150
      print("ticket price is 150")
   elif(age<=15):
      bill=250
      print("ticket price is 250")
   elif(age<=20):
      bill=350
      print("ticket price is 350")
   else:
      bill=500
      print("ticket price is 500")
   want_photo=input("do you want take photo(y/n):")
   if(want_photo =='y' or want_photo=='Y'):
      bill=bill+50
   print(f"your total bill is {bill}")
else:
   print("you can't ride")
print("bye i love u")