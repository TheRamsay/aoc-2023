acc = 0

digits_str = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

for line in open("./input.txt").readlines():
    digits = []

    for i, char in enumerate(line):
        if char.isdigit():
            digits.append(char)
        
        for ds in digits_str.keys():
            idx = line.find(ds, i)

            if idx == i:
                digits.append(digits_str[ds])
                break


    if len(digits) == 1:
        acc += int(f"{digits[0]}{digits[0]}")
    else:
        acc += int(f"{digits[0]}{digits[-1]}")


print(acc)