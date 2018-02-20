eggs = ('hello', 42, 0.5)
print(eggs[0])

print(eggs[1:3])

print(type(('hello',)))
print(type(('hello')))

print(list(eggs))
print(tuple(eggs))


def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)
