"""#sai=[2,"sai",True,3.8]
#print(sai)
#print(sai[1])
num=[2,4,-6,65,89,7,9,5,56,9]
print(len(num))
print(num[-1])
# slicing
num=[2,4,-6,65,89,7,9,5,56,9]
print(num[0:10])
print(num[0:])
print(num[:])
print(num[1:6])
print(num[3:])
print(num[:7])
print(num[0:9:2]) #stepping
print(num[0:9:3])"""
# sort (ascending)
# we can't apply sort in mixed data type list
num=[2,4,-6,65,89,7,9,5,56,9]
#print(num.sort()) it gives none
num.sort()
print(num)
# reverse
num.reverse()
print(num)
#minimum
print(min(num))
# maximum
print(max(num))
# append (add the value end of list) add only one value
num.append(90)
print(num)
# insert (add values middle of the list) add one value at a time
num.insert(2,78)
print(num)
# extend (add more values at a time at end of the list)
num.extend([45,98,70,60,54])
print(num)
 #change values of list
num[2]=10
print(num)
# add values in list
num[1:4]=[2,3,6]
print(num)
#remove
num.remove(98)
print(num)
#pop (it will remove last element and print it)
print(num.pop())
print(num)
print(num.pop(2))
print(num)
#count (it counts how many times repeated)
print(num.count(9))
#descending order
num.sort(reverse=True)
print(num)
# copy the list
l=num.copy()
print(l)

# add two lists
l1=[2,5,7,9,9,6,4]
num.extend(l1)  #num+l1
print(num)
sai1=[1,2,3,4,5]


