import numpy as np

def count_mirrored(data):
    l_i, r_i = None, None
    for i, (row1, row2) in enumerate(zip(data, data[1:])):
        if row1 == row2:
            print(f"{i=}")
            l_i = i - 1
            r_i = i + 2

            counter = 1


            while l_i >= 0 and r_i < len(data):
                print(f"{l_i=} {r_i=}")
                if data[l_i] == data[r_i]:
                    counter += 1
                    l_i -= 1
                    r_i += 1
                else:
                    return counter


for pattern in open("./test.txt").read().split("\n\n"):

    pattern_data = pattern.split("\n")

    # rows
    pattern_rows = np.array(pattern_data).tolist()
    c1 = count_mirrored(pattern_rows)

    
    # columns
    pattern_columns = np.array(pattern_data).T.tolist()
    print("r", pattern_rows)
    print("c", pattern_columns)

    c2 = count_mirrored(pattern_columns)

    print(c1, c2)

