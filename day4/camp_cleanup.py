import pandas as pd

def split_range(range):
    return [int(x) for x in range.split('-')]


def fully_contains(row):    
    range1 = split_range(row[0])
    range2 = split_range(row[1])

    range1_is_in_range2 = range1[0] >= range2[0] and range1[1] <= range2[1]
    range2_is_in_range1 = range2[0] >= range1[0] and range2[1] <= range1[1]
    return range1_is_in_range2 or range2_is_in_range1

def overlaps(row):
    range1 = split_range(row[0])
    range2 = split_range(row[1])

    range1_overlaps_range2 = range1[0] <= range2[1] and range1[1] >= range2[0]
    range2_overlaps_range1 = range2[0] <= range1[1] and range2[1] >= range1[0]
    return range1_overlaps_range2 or range2_overlaps_range1

def compute_fully_contained_ranges(ranges):
    ranges['fully_contain'] = ranges.apply(fully_contains, axis=1)
    return ranges['fully_contain'].sum()

def compute_overlapping_ranges(ranges):
    ranges['overlaps'] = ranges.apply(overlaps, axis=1)
    return ranges['overlaps'].sum()

if __name__ == '__main__':
    ranges = pd.read_table('input.txt', header=None, sep=',')
    result = compute_fully_contained_ranges(ranges)
    print(f"Puzzle 1 : {result}")
    result2 = compute_overlapping_ranges(ranges)
    print(f"Puzzle 2 : {result2}")
    
