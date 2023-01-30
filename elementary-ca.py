import random

ROWS = 10
COLS = 15

#Initializing random state of queue
states = [[random.randint(0, 1) for _ in range(COLS)]]

#Populating the queues with empty spaces indicating availability
for i in range(1, ROWS):
    tempArr = []

    for j in range(COLS):
        tempArr.append(0)

    states.append(tempArr)

print("Initial state")
print(*states, sep="\n")

#Simulating the progression of the queues as population increases

iteration_count = 0

for i in range(1, ROWS):

    for j in range(COLS):

        if(states[i - 1][j] == 1):
            if(j > 0 and j < COLS - 1):
                if(states[i - 1][j - 1] == 0):
                    states[i - 1][j - 1] = 1
                elif(states[i - 1][j + 1]):
                    states[i - 1][j + 1] = 1
            elif(j > 1 and j < COLS - 2):
                if(states[i - 1][j - 2] == 0):
                    states[i - 1][j - 2] = 1
                elif(states[i - 1][j + 2] == 0):
                    states[i - 1][j + 2] = 1
            else:
                states[i][j] = 1
        elif(states[i - 1][j] == 0):
            states[i - 1][j] = 1   
        else:
            states[i][j] = 1

        iteration_count += 1

        print('Iteration {0}'.format(iteration_count))
        print(*states, sep="\n")