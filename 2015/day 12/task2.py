import json

mode = 2
if mode == 1:
    file = "example.txt"
elif mode == 2:
    file = "input.txt"
input = [line.strip() for line in open(file)][0]


def has_red(obj):
    if isinstance(obj, dict):
        return "red" in obj.values()
    return False


def sum_numbers(obj):
    if isinstance(obj, int):
        return obj
    elif isinstance(obj, list):
        return sum(sum_numbers(item) for item in obj)
    elif isinstance(obj, dict):
        if has_red(obj):
            return 0
        return sum(sum_numbers(value) for value in obj.values())
    return 0


data = json.loads(input)
json_formatted_str = json.dumps(data, indent=2)
result = sum_numbers(data)
print(result)
print(json_formatted_str)
