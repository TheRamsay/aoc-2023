def part1():
    acc = 0

    limits = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    for i, line in enumerate(open("./input.txt", "r").readlines()):
        _, data = line.split(": ")

        dices_sets = data.split(";")

        correct = True

        for _set in dices_sets:
            colors = _set.split(", ")

            for pair in colors:
                pair = pair.strip()
                n, c = pair.split(" ")
                n = int(n)

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

    for i, line in enumerate(open("./input.txt", "r").readlines()):
        counts = {
            "green": -1,
            "red": -1,
            "blue": -1
        }

        line = line.strip()
        line.lstrip()
        _, data = line.split(": ")

        dices_sets = data.split(";")

        correct = True

        for _set in dices_sets:
            colors = _set.split(", ")

            for pair in colors:
                pair = pair.strip()
                n, c = pair.split(" ")
                n = int(n)

                if n > counts[c]:
                    counts[c] = n

        mult = 1
        for c in counts.values():
            mult *= c

        acc += mult

    print(acc)

part1()
part2()