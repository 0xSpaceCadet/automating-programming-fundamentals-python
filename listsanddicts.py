import random
from copy import deepcopy

c_name=[]
max_len = 3

while len(c_name)<max_len:
    istream = input("Please enter your name: (or ENTER to quit storing): ")
    if istream == '':
        break
    c_name.append(istream)

print(c_name)
a, b, c = c_name
print(a, b, c)
print()


for index, item in enumerate(c_name):
    print(index, item)

# short circuiting
spam=[]
if len(spam)>0 and len(spam)<=max_len and spam[0]=='alpha':
    print('firsttermyes')



messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

print('Ask a yes or no question:')
input('>')
print(messages[random.randint(0, len(messages) - 1)])

print(list('hello'))

#copy and deepcopy() To compartive

# in python assignments during fucntion all parameters are by reference
# which mean that they depend on MUTABILITY of the type
