# TODO решите задачу
import json


def task() -> float:
    with open(json_file, 'r') as file:
        data = json.load(file)
    product_sum = sum(item["score"] * item["weight"] for item in data)

    return round(product_sum, 3)


json_file = "input.json"
print(task())
