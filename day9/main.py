from typing import List

data = open('input.txt', 'r').readlines()

def process_history(data: List[int], reverse = False):
    steps = [data]
    current = data

    while not all(True if i == 0 else False for i in current):
        new = [n - c for c, n in zip(current[:-1], current[1:])]
        steps.append(new)
        current = new


    if reverse:
        steps[-1].insert(0, 0)
    else:
        steps[-1].append(0)
    for c, p in zip(reversed(steps[:-1]), reversed(steps[1:])):
        if reverse:
            next_val = c[0] - p[0]
            c.insert(0, next_val)
        else:
            next_val = c[-1] + p[-1]
            c.append(next_val)


    if reverse:
        return steps[0][0]
    else:
        return steps[0][-1]

acc1 = 0
acc2 = 0

for history in data:
    history = [int(i) for i in history.split()]
    
    acc1 += process_history(history)
    acc2 += process_history(history, True)

print(acc1)
print(acc2)