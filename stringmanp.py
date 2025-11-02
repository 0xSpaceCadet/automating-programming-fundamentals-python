l_s_name = 10

def abcdr(s_name):
    for i in range(len(s_name)):
        global l_s_name
        l_s_name= len(s_name)//2
        printable=s_name[0:len(s_name)-(i+1)]
        #print(printable.rjust(len(s_name)//2, "-"))
        print(printable.center(len(s_name), " "))

print(abcdr('abracadabra'))
print(l_s_name)


import sys, time
indent =0

indent_increasing=True

story =  """Once upon a time there was a very long string that was \
over 100 characters long and could not all fit on the """

print(story)

# try:
#     while True:
#         print(' ' * indent, end='')
#         print('@@@@@@@@@@')
#         time.sleep(0.001)
#
#         if indent_increasing:
#             indent = indent + 1
#             if indent == 20:
#                 indent_increasing = False
#         else:
#             indent = indent - 1
#             if indent == 0:
#                 indent_increasing = True
# except KeyboardInterrupt:
#     sys.exit()