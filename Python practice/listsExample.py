spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print(spam[0])
print(spam[0][1])
print(spam[1][4])

spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[0:4])
print(spam[1:3])
print(spam[0:-1])


spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[:3])
print(spam[1:])
print(spam[:])

spam[1] = 'aardvark'
spam[-1] = 12345
print(spam)


spam = [1, 2, 3]
spam = spam + ['A', 'B', 'C']
print(spam)


del spam[2]
print(spam)



catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] 
print('The cat names are:')
for name in catNames:
    print('  ' + name)

    

for i in range(4):
    print(i)

    

for i in [0, 1, 2, 3]:
    print(i)
    

supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])


print('howdy' in ['hello', 'hi', 'howdy', 'heyas'])
print('howdy' not in spam)

