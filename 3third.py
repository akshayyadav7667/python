
#  List Methods

#  list=[1,3,4]

# list.append(4)  add one elements at the end
# list.sort()   sort in ascending order
# list.sort(reverse=True) sorts in descending order [4,3,1]
# list.reverse()  reverse list   [4,3,1]
# list.insert(index,el)  insert element at index


list=[2,4,7,1,6]

list.append(9)

print(list)
# [2, 4, 7, 1, 6, 9]

# list.sort(reverse=True)
list.sort()
# [1, 2, 4, 6, 7, 9]

list.insert(1,5)
# [1, 5, 2, 4, 6, 7, 9]

# list.remove(5)   remove the first occurence of the element
# [1, 2, 4, 6, 7, 9]

# list.pop(index)  remove the elements at index 

list.pop(1)

# [1, 2, 4, 6, 7, 9]   pop the element at the index 1 (5 is deleted )



print(list)

