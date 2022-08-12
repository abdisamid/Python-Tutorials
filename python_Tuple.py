# tuple is similar to list, the only difference is that it cant be modified
t1 = (1, 2) # tuple creation
t2 = (3, 4, 5, 3)

print(len(t1), len(t2)) # determining the length of a tuple

print(t1.count(3))
print(t2.count(3))

print(t1.index(2)) # getting the index

print(t1[0])
