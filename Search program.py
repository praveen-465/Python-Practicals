a = input('Enter word: ')
with open('meanings.dat', 'r+b') as f:
    for i in f:
        if a.encode() in i:
            print(i.decode())