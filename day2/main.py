def parse():
    output = [] 
    for line in open("./input.txt", "r").readlines():
        line_output = []
        _, data = line.split(": ")

        dices_sets = data.split(";")

        for _set in dices_sets:
            colors = _set.split(", ")

            for pair in colors:
                pair = pair.strip()
                n, c = pair.split(" ")
                n = int(n)
                line_output.append((n, c))

        output.append(line_output)

    return output

def part1():
    acc = 0

    limits = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    for i, line in enumerate(parse()):
        correct = True

        for n, c in line:
            for color, limit_n in limits.items():
                if c == color and n > limit_n:
                    correct = False

            if not correct:
                break
        
        if correct:
            acc += i + 1

    print(acc)

def part2():
    acc = 0


    for line in parse():

        counts = {
            "green": -1,
            "red": -1,
            "blue": -1
        }

        for n, c in line:
            if n > counts[c]:
                counts[c] = n

        mult = 1
        for c in counts.values():
            mult *= c

        acc += mult

    print(acc)

part1()
part2()