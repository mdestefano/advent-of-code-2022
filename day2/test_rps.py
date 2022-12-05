from rps import rock_paper_scissors, compute_score, encrypted_strategy
import pandas as pd

def test_rock_paper_scissor():
    
    strategies = pd.read_table("test.txt", header=None, sep=" ")
    print(strategies)
    assert rock_paper_scissors(strategies) == 15

def test_encrypted_strategy():
    strategies = pd.read_table("test.txt", header=None, sep=" ")
    print(strategies)
    assert rock_paper_scissors(strategies, encrypted_strategy) == 12

def test_draw():
    assert compute_score("AX") == 4
    assert compute_score("BY") == 5
    assert compute_score("CZ") == 6

def test_win():
    assert compute_score("AY") == 8
    assert compute_score("BZ") == 9
    assert compute_score("CX") == 7

def test_lose():
    assert compute_score("BX") == 1
    assert compute_score("CY") == 2
    assert compute_score("AZ") == 3
