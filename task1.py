import json
# TODO решите задачу
def task() -> float:
    with open("input.json", 'r') as f:
        return round(sum(d["score"] * d["weight"] for d in json.load(f)), 3)

print(task())
