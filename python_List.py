# List is a collection of elements, of different data types, denoted by square brackets
lst = [1, 1, 2, 3, 4.5, True, "Hello"]
lst.append("last element") # this adds an element to the list => lst = [1, 1, 2, 3, 4.5, True, "Hello", "last element"]
print(len(lst)) # this outputs the length of the list
lst.pop() # this method removes the last element from the list
lst.count() # this method counts the number of times an element occurs in the list like 1 appears twice
lst.index(1) # this method gives the indes of the first occurance of the element 1 which is 0
lst.remove(1) # this method removes the first occurance of the passed element
print(lst[-1]) # this gives us the last element which is "Hello"
lst2 = [5, 6] # creating another list
sum = lst + lst2 # this combines the two lists
print(sum) # this outputs both lists [1, 1, 2, 3, 4.5, True, "Hello"] [5, 6]
lst.extend(lst2) # this method combines the two lists and outputs => [1, 1, 2, 3, 4.5, True, "Hello", 5, 6]
lst3 = [[1,2[]][3, 4][5, 6][7, 8]] # this is a multidimentional list
print([0][2]) # this outputs the empty list [], thats how to index and access an element in a multidimentional list
