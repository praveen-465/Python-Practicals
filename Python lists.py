# Python lists
list = ['Tomato', 'Ginger', 'Chilly', 'Sugar cane'] # A list

list.append('Pineapple') # Adding element
print(list)

list.extend(('Kivy', 'Green Apple')) # Add multiple values
print(list)

list.pop() # Remove the last element
list.pop(1) # Remove 2nd element
print(list)

list.remove('Kivy') #Remove  'Kivy' from list
print(list)

a = list.index('Tomato') # Search for Tomato in list
print(a)

c = list.append('Tomato')
h=list.count('Tomato') # Count 'Tomato'
print(h)

list.sort() # Sort values in ascending order
print(list)

copy = list.copy()
print(copy)

r = list.reverse() # Reverse the list
print(r)

list.insert(1, 'Grapes') # Add grapes at 2nd position
print(list)

list.clear() #clear the list
print(list)