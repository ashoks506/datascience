import copy
spam = ['A', 'B', 'C', 'D',23,4,5,5,5,6,6,54,5,4]
cheese = copy.copy(spam)
cheese[1] = 42
print(spam)
print(cheese)
print(int('3' * 2))
print(int(int('3' * 2) // 11))
print(spam[int(int('3' * 2) // 11)])
