# dictionary or dict is a collection that associates immutable keys with values of any type
x = {"name": "abdi", "age": 22} # this is the syntax for creating a dictionary
# the arrangement of the dictionary is the key:value pair
print(x["name"]) # the syntax for accessing the value abdi

# to add keys and values: =>
x = {} # we can start with an empty dictionary
x["Name"] = "Abdi"
print(x) # this outputs {'Name':'Abdi'}

# to add a key and a value to an existing dictionary: =>
x ={"key1": "value1"}
x["key2"] = "value2" # this updates the dictionary by adding this to it if it does not exist in the dictionary
print(x) # this outputs : => {'key1':'value1', 'key2':'value2'}

# to delete a key and its value from a dictionary : =>
x = {"a":1, "b":2, "c":3}
del x["a"]
print(x) # this outputs : => {"b": 2, "c": 3}

# to check if a key is contained in a dictionary : =>
x = {2:1, 3:3}
contains = 1 in x
print(contains) # this outputs False

names = {
  1: "Abdi",
  2: "John"
  3: "Mohammed",
}
print("The first guy's name is", names[1]) : => # this outputs the first guy's name is Abdi

# to count the occurance of the letters of a word using dictionary:
characters = {}

string = "hello world"

for char in string:
  characters[char] = charachters.get(char, 0) + 1

print(characters) # this outputs => {'h': 1, 'e': 1, 'l': 3, 'o':2, 'w': 1,'r': 1, 'd': 1}
