from dataclasses import dataclass
from collections import OrderedDict, defaultdict
from typing import List, Tuple

@dataclass
class Filter:
    start: int 
    end: int
    shift: int

    @staticmethod
    def parse(line: str):
        destination, source, length = [int(x) for x in line.split()]
        start = source
        end = source + length
        shift = destination - source
        return Filter(start, end, shift)

    def __hash__(self) -> int:
        return hash(self.start)

def parse():
    filters = OrderedDict()

    lines = open('test.txt').readlines()

    other_data = lines[0].split(": ")[1].strip().split()
    seeds1 = [int(x) for x in other_data]
    seeds2 = []

    for i, x in enumerate(other_data[::2]):
        seeds2.append((int(x), int(x) + int(other_data[i * 2 + 1])))

    lines = lines[1:]

    current_type = None

    for line in lines:
        if line[0].isalpha():
            current_type = line.strip()[:-1]
        elif line[0].isnumeric():

            if current_type not in filters:
                filters[current_type] = []
            filters[current_type].append(Filter.parse(line))

    return seeds1, seeds2, filters


def map_seed(seed: int, filters: OrderedDict[str, List]):
    print(f"Mapping seed {seed}")

    for filter_type, filter_list in filters.items():
        for filter in filter_list:
            if filter.start <= seed < filter.end:
                print(f"Applying filter {filter_type}: {seed} -> {seed + filter.shift}")
                seed += filter.shift
                break

    return seed

def map_seed_opt(seed_range: Tuple[int, int], filters: OrderedDict[str, List]):
    mapped_seeds = []

    intervals = []

    prev = None
    for _, filter_list in filters.items():
        for filter in sorted(filter_list, key=lambda x: x.start):
            if prev is None:
                interval = (seed_range[0], filter.start)
                if interval[0] < interval[1]:
                    intervals.append(interval)
            else:
                intervals.append((prev[1], filter.start))

            curr = (filter.start, filter.end)
            intervals.append(curr)
            prev = curr


    interval = (filter.end, seed_range[1])
    if interval[0] < interval[1]:
        intervals.append(interval)



    print(f"{intervals=}")

    for i_start, i_end in intervals:
        for filter_type, filter_list in filters.items():
            for filter in filter_list:
                #            filter
                # ---|-----<------->---|--
                if filter.start > i_start and filter.end < i_end:
                    mapped_seeds.append(map_seed(filter.start, filters))
                    mapped_seeds.append(map_seed(filter.end, filters))

                #       filter
                # ---<----|--->---|--
                elif filter.start < i_start and filter.end < i_end:
                    mapped_seeds.append(map_seed(i_start, filters))
                    mapped_seeds.append(map_seed(filter.end, filters))

                #           filter
                # --|----<------|->--
                elif filter.start > i_start and filter.end < i_end:
                    mapped_seeds.append(map_seed(filter.start, filters))
                    mapped_seeds.append(map_seed(i_end, filters))


    return mapped_seeds


def part1():
    seeds, _, filters = parse()

    for k, v in filters.items():
        if len(v) != 0:
            print(k)
            print(v)
    mapped_seeds = [map_seed(seed, filters) for seed in seeds]

    return min(mapped_seeds)


def part2():
    _, seeds, filters = parse()

    mapped_seeds = []

    print(f"{seeds=}")

    for k, v in filters.items():
        if len(v) != 0:
            print(v)

    for seed in seeds:
        print(f"Mapping seed {seed}")
        mapped_seeds.extend(map_seed_opt(seed, filters))


    return min(mapped_seeds)

# print(part1())
print(part2())