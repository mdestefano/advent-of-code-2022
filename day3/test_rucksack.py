from rucksack import *
import pytest

def test_rucksack():
    with open('test.txt') as f:
        items = f.readlines()
    assert rucksack(items) == 157

@pytest.mark.parametrize("strings, expected", 
    [(("abcde", "efghi"),"e"), (("abcde", "fghij"), None), 
    (("vJrwpWtwJgWrhcsFMMfFFhFp","jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL","PmmdzqPrVvPwwTWBwg"),"r"),
    (("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"), "Z")])
def test_find_common_item(strings, expected):
    assert find_common_item(strings) == expected


@pytest.mark.parametrize("char, expected",
    [("a", 1), ("b", 2), ("c", 3), ("z", 26), ("L", 38), ("A", 27), ("Z", 52)])
def test_priority(char, expected):
    assert priority(char) == expected

@pytest.mark.parametrize("string, expected",
    [("abba", ("ab", "ba")), ("abcd", ("ab", "cd")), ("ab", ("a", "b")),("", ("", ""))])
def test_split_string(string, expected):
    assert split_string(string) == expected

def test_grouped_strategy():
    assert grouped_strategy([
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", 
        "ttgJtRGJQctTZtZT", 
        "CrZsJsPPZsGzwwsLwLmpwMDw"
    ], 3) == [
        ["vJrwpWtwJgWrhcsFMMfFFhFp", "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg"],
        ["wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "ttgJtRGJQctTZtZT", "CrZsJsPPZsGzwwsLwLmpwMDw"]
    ]

def test_grouped_rucksack():
    with open('test.txt') as f:
        items = f.readlines()
    assert rucksack(items, grouped_strategy) == 70