from hangman import WORDS, choose_word, display_word, is_word_guessed


def test_choose_word():
    assert choose_word() in WORDS


def test_display_word():
    assert display_word("apple", ["p"]) == "_ p p _ _"


def test_is_word_guessed():
    assert is_word_guessed("apple", ["a", "p", "l", "e"]) is True


def test_is_word_not_guessed():
    assert is_word_guessed("apple", ["p", "l", "e"]) is False