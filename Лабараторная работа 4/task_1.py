import json


def task(JSON_FILE) -> float:
    with open(JSON_FILE, "r") as f:
        json_data = json.load(f)

    original = 0

    for dictionary in json_data:
        original += dictionary["score"] * dictionary["weight"]

    return round(original, 3)

JSON_FILE = "input.json"
answer = task(JSON_FILE)
print(answer)
