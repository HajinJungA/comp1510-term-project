from rock_paper_scissors import decide_winner


def test_decide_winner_player():
    assert decide_winner("rock", "scissors") == "player"


def test_decide_winner_computer():
    assert decide_winner("paper", "scissors") == "computer"


def test_decide_winner_tie():
    assert decide_winner("rock", "rock") == "tie"