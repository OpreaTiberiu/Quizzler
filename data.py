import requests


def get_questions():
    resp = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
    resp.raise_for_status()
    data = resp.json()

    return data["results"]
