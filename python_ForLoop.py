for i in range(10):
    print(i) # this syntax outputs => 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    
for i in range(2):
    print("Hello")  # this outputs => Hello, Hello

for i in range(2, 10, 3): # this syntax is for i range(start, stop, step):
    print(i) # this outputs 3, 6, 9
    
    
# to iterate through a list
lst = [1, 2, 3, True, 4.5]
for i range(len(lst)):
  print(lst[i]) # this outputs => 1, 2, 3, True, 4.5
  
 # or
lst = [1, 2, 3, True, 4.5]
for idx range(len(lst)):
  print(lst[idx]) # this outputs => 1, 2, 3, True, 4.5
  
 # iteration by item
lst = [1, 2, 3, True, 4.5]
for element in lst:
  print(element) # this outputs => 1, 2, 3, True, 4.5
  
lst = [1, 2, 3, True, 4.5]
for i, element in enumerate(lst):
  print(i, element)
  # the output is : =>
  # 0 1
  # 1 2
  # 2 3
  # 3 True
  # 4 4.5
  
  #looping through tuples
tup = (1, 2, 3, True, 4.5)
for i, element in enumerate(tup):
  print(i, element)
  # the output is : =>
  # 0 1
  # 1 2
  # 2 3
  # 3 True
  # 4 4.5
  
  # control statements => :
  # break => this terminates the loop statement and transfers the execution to the statement immediately following the loop.
  # continue => Causes the loop to skip the remainder of its body and immediately retest its condition prior to reiterating.
  # pass => The pass statement in Python is used when a statement is required syntactically but you do not want any command or code to execute.
  
  # nested for loop =>:
  i = 2
while(i < 19):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print i, " is prime"
   i = i + 1

print "Good bye!"
# the output would be => : 
# 2 is prime 
# 3 is prime 
# 5 is prime 
# 7 is prime 
# 11 is prime 
# 13 is prime 
# 17 is prime
Good bye!

# to find an index of a value/string:
st = "Hello World!"
for i, char in enumerate(st):
  if char == "w":
    print(i)
# this outputs => : 6

numbers = []

for i in range(3):
  num = input("Enter a number: ")
  numbers.append(int(num))
  
print(numbers) # if we enter 1, 2, 3 this outputs => : [1, 2, 3]
