import random
def getAnswer(answerNumber):
       if answerNumber == 1:
           return 1
       elif answerNumber == 2:
           return 2
       elif answerNumber == 3:
           return 'Yes'
       elif answerNumber == 4:
           return 4
       elif answerNumber == 5:
           return 'Ask again later'
       elif answerNumber == 6:
           return 'Concentrate and ask again'
       elif answerNumber == 7:
           return 7
       elif answerNumber == 8:
           return 'Outlook not so good'
       elif answerNumber == 9:
           return 'Very doubtful'

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)


print('cats', 'dogs', 'mice')
print('cats', 'dogs', 'mice', sep='ashok')



def spam():
   eggs = 99
   bacon()
   print(eggs)

def bacon():
      eggs = 0
      print(eggs)

spam()


def spam():
    eggs = 'spam local'
    print(eggs) 
def bacon():
        eggs = 'bacon local'
        print(eggs) 
        spam()
        print(eggs) 

eggs = 'global'
bacon()
print(eggs)





