import sys, time, random
WIDTH = 50
c_dim = [0]*WIDTH
try:
    columns = [0] * WIDTH
    while True:
        for i in range(WIDTH):
            if random.random() < 0.02:
                columns[i] = random.randint(4, 14)

            if columns[i] == 0:
                print('.', end='')
            else:
                print(random.choice([0, 1]), end='')
                columns[i] -= 1  # Decrement the counter for this column.
        print()  # Print a newline at the end of the row of columns.
        time.sleep(0.1)  # Each row pauses for one tenth of a second.
except KeyboardInterrupt:
    sys.exit()  # When Ctrl-C is pressed, end the program.