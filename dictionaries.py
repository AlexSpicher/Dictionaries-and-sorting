"""
Dictionary exercises
Alex Spicher
"""
print('Dictionary basics')
mydct = {} #creates an empty dicionary, dictionaries used curly brackets
mydct[1] = 'red' #dictionaries uses keys to identify items
mydct[2] = 'orange' #this process adds an item with a key
mydct[3] = 'yellow'
print(mydct) #displays built dictionary
print(mydct[2]) #searches for the key to display the item assigned
if 2 in mydct:
    print(mydct[3]) #uses the if command to display a value if another is present
else:
    mydct[4] = 'blue' #this would add blue if there was no key value of 2
print('--------------------------------')

print('delete operator (del)')
mylist = ['red', 'orange', 'yellow', 'green'] #makes a dictionary, this time it is filled
print(mylist)
del mylist[2] #deletes the third item from the list
print(mylist)
mylist.append('yellow') #adds yellow back
print(mylist)
del mylist[-2:] #deletes the third element and everything after using slicing
print(mylist)
print('----------------------------------')

print('dictionary formatting')
h = {} #creates an empty dictionary
h['word'] = 'garfield' #adds garfield with the key 'word'
h['count'] = 42 #adds 42 with the key 'count'
print(h) # prints the dictionary
s = 'I want %(count)d copies of %(word)s' % h #converts 42 into a string by adding %s with count in between
#count is the key for the integer we want to convert
#without converting, we would have to use + and commas to separate the string from the variable
print(s)

