import pandas as pd


def compute_score(row):
    
    base_scores = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }

    mapping = {
        "A": "X",
        "B": "Y",
        "C": "Z"
    }
    
    opponent = row[0]
    player = row[1]

    if mapping[opponent] == player:
        return 3 + base_scores[player]

    if opponent == "A":
        s = 6 if player == "Y" else 0
        return s + base_scores[player]

    if opponent == "B":
        s = 6 if player == "Z" else 0
        return s + base_scores[player]

    if opponent == "C":
        s = 6 if player == "X" else 0
        return s + base_scores[player]

def encrypted_strategy(row):
    
    opponent = row[0]
    game = row[1]

    
    base_scores = {
        "A": 1,
        "B": 2,
        "C": 3
    }

    esit = {
        "X": 0,
        "Y": 3,
        "Z": 6
    }

    mapping = {
        "A": {
            "X": "C",
            "Y": "A",
            "Z": "B"
        },
        "B": {
            "X": "A",
            "Y": "B",
            "Z": "C"
        },
        "C": {
            "X": "B",
            "Y": "C",
            "Z": "A"
        }
    }
    result = esit[game] + base_scores[mapping[opponent][game]]
    return result
    
def rock_paper_scissors(strategies, strategy=compute_score):
    strategies["scores"] = strategies.apply(strategy, axis=1)
    return strategies["scores"].sum()    

if __name__ == "__main__":
    strategies = pd.read_table("input.txt", header=None, sep=" ")
    print(f"Puzzle 1: {rock_paper_scissors(strategies)}")
    print(f"Puzzle 2: {rock_paper_scissors(strategies, encrypted_strategy)}")