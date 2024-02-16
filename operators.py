
"""#arithmetic operator
# +,-,/,//,*,**,%
w=input("enter weight=")
h=input("enter height=")
#i=int(h)*int(h) 
bmi=int(w)/int(h)**2
print(bmi)
#or
height=int(input("enter weight in kg="))
weight=float(input("enter height meters="))
bmi=(weight)/(height)**2
print(bmi)"""
"""# assignment operator +=,-=,*=,**=,/=,//=,%=
a=5
a +=10 #(a=a+10)
print(a)
b=10
b **= 5
print(b)
# comparison ope  >,<,>=,<=,==,!=
a=10
print(a==10)
print((a+2)==12)"""
"""# logical ope and,or,not
a=10
b=2
c=(a>9 and b<3) #all conditions are true its true otherthan false
print(c)
f=20
e=30
g=(f>10 or e<20) # any one conditon is true its true
print(g)
i=10
j=20
k=(i>6 and j<30) 
#it gives reverse its true it gives false
print(not(k))"""
"""#bitwise operator
a,b=6,7
print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(~b)
print(a << b)
print(a >> b)"""
"""#identity operators (it cmpares id of the data)
a=10
b=10
print(id(a))
print(id(b))
#print(a is b)
print(a is not b)
c=11
print(id(c))
d="11"
print(c is d)
j=12
print(id(j))
j=13
print(id(j))
print(j is j)"""
# membership operator
str='vanapalli sai'
print('v' in str)
n=[1,6,8,9,20]
print(20 in n)
print(8 not in n)

