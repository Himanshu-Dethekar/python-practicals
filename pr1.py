"""
    Create a list and perform the following methods 
    Append, Insert, Remove, Reverse, Pop, Count, Clear

"""

list=[1,2,3,4,5]                                           # LIST
print(list)

list.append(6)                                             #adding element to existing list
print("list after append",list)

list.insert(2,10)                                          #inserting element '10' at index '2'
print("list after insert",list)

list.remove(6)                                             #removing element from list
print("list after removing element",list)

list.pop(2)                                                #popping element form list
print("list after popping element at index 2",list)

list.reverse()                                             #reversing the list
print("reverse list",list)

p = list.count(2)                                          #occurence of the element '2' in the list
print("count",p)

length = list.__len__()                                    #using dunder
print("length of list",length)

'''OR'''

print("length of list is ",len(list))                      #using length function

list.clear()
print("After performing clear method",list)                #list is empty now