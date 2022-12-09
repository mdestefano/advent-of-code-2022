import numpy as np


def viewing_distance(height, direction):
    for i,h in enumerate(direction):
        if h >= height:
            return i+1
    return len(direction)
        
def scenic_score(x,y,wood_map):
    tree_height = wood_map[x, y]
    
    left_trees = np.flip(wood_map[x, :y].copy())
    right_trees = wood_map[x, y+1:]
    top_trees = np.flip(wood_map[:x, y].copy())
    bottom_trees = wood_map[x+1:, y]
    #print(f"left_trees: {left_trees}, right_trees: {right_trees}, top_trees: {top_trees}, bottom_trees: {bottom_trees}")
    
    left_distance = viewing_distance(tree_height, left_trees)
    right_distance = viewing_distance(tree_height, right_trees)
    top_distance = viewing_distance(tree_height, top_trees)
    bottom_distance = viewing_distance(tree_height, bottom_trees)
    
    #print(f"left_distance: {left_distance}, right_distance: {right_distance}, top_distance: {top_distance}, bottom_distance: {bottom_distance}")
    return left_distance * right_distance * top_distance * bottom_distance

def is_visible(x, y, wood_map):
    tree_height = wood_map[x, y]
    
    left_trees = wood_map[x, :y]
    right_trees = wood_map[x, y+1:]
    top_trees = wood_map[:x, y]
    bottom_trees = wood_map[x+1:, y]

    return (left_trees.max() < tree_height or right_trees.max() < tree_height or top_trees.max() < tree_height or bottom_trees.max() < tree_height)
    
def read_input(filename):
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    matrix = []
    for line in lines:
        l = [w for w in line]
        matrix.append([int(x) for x in l])
    return np.array(matrix)

visible_trees = 0
wood_map = read_input('input.txt')
interesting_trees = wood_map[1:-1, 1:-1]
scenic_scores = np.zeros(interesting_trees.shape)
for x in range(1, interesting_trees.shape[0] + 1):
    for y in range(1, interesting_trees.shape[1] + 1):
        scenic_scores[x-1, y-1] = scenic_score(x, y, wood_map)
        if is_visible(x, y, wood_map):
            visible_trees += 1
visible_trees += 2 * (wood_map.shape[0] + wood_map.shape[1] - 2)
print(f"Visible trees: {visible_trees}")
print(f"Max scenic score: {scenic_scores.max()}")




