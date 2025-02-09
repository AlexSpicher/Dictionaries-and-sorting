"""
Sorting exercises
Alex Spicher
"""
print('sorting numbers')

ls = [5, 1, 4, 3] #create a list with integers (sorting pertains to lists)
print(ls) #displays unsorted list
print(sorted(ls)) #sorts the list using the sorted variable
print('------------------------------')

print('sorting strings')

lis = ['aa', 'BB', 'zz', 'CC'] #list of random strings
print(lis)
print(sorted(lis)) #sorts the list of strings, case sensitive
print(sorted(lis, reverse=True)) #sorts the list in reverse
print('-------------------------------')

print('sorting using key')
new = ['ccc', 'AAAA', 'd', 'BB'] #list of random strings titled new
print(new) #displays the list
print(sorted(new, key=len)) #uses the key operator to sort by the length of each variable
print(sorted(new, key=str.lower)) #uses the str.lower to sort alphabetically regardless of case
