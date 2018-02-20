spam = ['hello', 'hi', 'howdy', 'heyas']
print(spam.index('hello'))

spam.append('moose')
print(spam)

spam.insert(1, 'chicken')
print(spam)


spam.remove('howdy')
spam.remove(spam[0])
print(spam)



spam.sort()
print(spam)

spam.sort(reverse=True)
print(spam)

spam = ['a', 'z', 'A', 'Z']
spam.sort()
print(spam)
spam.sort(key=str.lower)
print(spam)


import random

messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

print(messages[random.randint(0, len(messages) - 1)])


name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
print(name)
print(newName)

