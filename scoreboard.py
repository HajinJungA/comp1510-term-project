"""Scoreboard functions for the COMP 1510 term project.

Write load_scoreboard and save_scoreboard so the arcade keeps scores across
restarts. Their docstrings and the tests in tests/test_scoreboard.py define
the required behavior.
"""
import json


def load_scoreboard(filename):
    """Return the scoreboard read from filename, or an empty one.

    :param filename: name of a JSON scoreboard file
    :return: the scoreboard as a dictionary. The caller still checks the
             nested record shape, as the README describes
    """
    try:
        with open(filename, "r") as file:
            data = json.load(file)

        if isinstance(data, dict):
            return data
        else:
            print("Could not load the scoreboard. Starting with an empty scoreboard.")
            return {}

    except (FileNotFoundError, json.JSONDecodeError):
        print("Could not load the scoreboard. Starting with an empty scoreboard.")
        return {}


def save_scoreboard(scoreboard, filename):
    """Write the scoreboard to filename as JSON.

    :param scoreboard: the scoreboard dictionary to write
    :param filename: name of the JSON scoreboard file
    :return: None
    """
    with open(filename, "w") as file:
        json.dump(scoreboard, file)
