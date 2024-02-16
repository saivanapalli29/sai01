set1={1,2,"sai",True,0.99}
# set not allowed duplicate values
#sets are unorder, no sequence  like listand tuple
#print(set1[0])#we can't access the index number because sets are unorder
set2={11,22,33,44,55}
#set={} #dict
#set=set()
#print(type(set))
#set1.add(98) add single value
#print(len(set1))
#set1.remove(1) it remove  selected item (if that value not in set it gives key error)
#set1.discard(1) it  also remove but if that value not in set it not gives error
#set1.clear() it clear all set
#print(set1.pop()) it remove random item and print the value
set1.add((78,67,45)) #add tuple in set
print(set1)
