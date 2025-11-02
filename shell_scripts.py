import sys
import turtle

george=turtle.Turtle()
george.color('red')


print ('shell script' * 5) # repeat string manipulation
username = 'Mary'
password = 'swordfish'
if username == 'Mary':
    print('Hello, Mary')
    if password == 'swordfish': print('Access granted.')
    else: print('Wrong password.')

spam=0
while spam < 2:
    print('Cuda Stream Shell')
    spam = spam + 1

m_name = input('iostream > ')  # iostream input
print(type(m_name))


# while True:
#     i_name = input('input pipeline > ')
#     if i_name == 'logout':
#         sys.exit()
#     print('non terminating respoonse, spawn back')


def spiral():
    t=turtle.Pen()
    t.color('red')
    for n in range(100):
        t.forward(n//2)
        t.left(90)

spiral()
turtle.done()