
races1 = [
    (60, 601),
    (80, 1163),
    (86, 1559),
    (76, 1300)
]

races2 = [
    (60808676, 601116315591300)
]


def run(races):
    ans = 1

    for duration, record in races:
        acc = 0
        speed = 0

        for seconds in range(duration + 1):
            distance_traveled = speed * (duration - seconds)

            if distance_traveled > record:
                acc += 1

            speed += 1

        ans *= acc

    return ans

print(run(races1))
print(run(races2))