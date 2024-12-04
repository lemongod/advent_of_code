import re

def get_input() -> str:
    with open("input.txt", 'r') as f:
        data = f.read()

    return data


def sum_matches(data):
    total = 0
    matches = re.findall("mul\(([0-9]+,[0-9]+)\)", data)
    for match in matches:
        num1, num2 = match.split(",")
        total += (int(num1) * int(num2))

    return total


def get_multiplied() -> int:
    return sum_matches(data=get_input())


print(get_multiplied())


def get_multiplied_with_conditions() -> int:
    data = get_input()

    # Split by don't
    # First time you see a do, calculate the rest of the mul

    # Prepend the do because we start immediately
    data = f"do(){data}"
    donts = data.split("don't()")
    concat = ""
    for j, string in enumerate(donts):
        parsed_string = string[string.find("do()"):]
        concat += parsed_string

    return sum_matches(data=concat)


print(get_multiplied_with_conditions())