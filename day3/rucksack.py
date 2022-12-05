from functools import reduce

def split_string(string):
    return (string[:len(string)//2], string[len(string)//2:])

def split_strategy(items):
    return list(map(split_string, items))

def grouped_strategy(items, groups=3):
    return [items[i:i+groups] for i in range(0, len(items), groups)]

def rucksack(items, refine_strategy=split_strategy):
    clean_items = [item.strip() for item in items]
    refined_items = refine_strategy(clean_items)
    common_items = map(lambda x: find_common_item(x), refined_items)
    return sum(map(priority, common_items))

def find_common_item(*strings):
    alist = list(*strings)
    sets = list(map(set, alist))
    common_elements = ''.join(sets[0].intersection(*sets[1:]))
    return common_elements[0] if common_elements else None

def priority(char):
    return ord(char) - 96 if char.islower() else ord(char) - 38

if __name__ == '__main__':
    with open('input.txt') as f:
        items = f.readlines()
    print(f"Puzzle 1: {rucksack(items)}")
    print(f"Puzzle 2: {rucksack(items, grouped_strategy)}")
