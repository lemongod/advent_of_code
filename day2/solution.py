def get_input_as_list_of_nums() -> list:
    with open("input.txt", 'r') as f:
        lines = f.read().splitlines()

    levels = []
    for line in lines:
        levels.append([int(num) for num in line.split(' ')])

    return levels


def check_level(level: list) -> bool:
    increasing = None
    for i, num in enumerate(level):
        if i + 1 >= len(level):
            return True

        # Set direction, if it's opposite of previous direction
        # it's not safe
        if -3 <= num - level[i + 1] < 0:
            # We are increasing

            # Means we switched directions
            if increasing is False:
                return False

            increasing = True
        elif 0 < num - level[i + 1] <= 3:
            # We are decreasing

            # Means we switched directions
            if increasing is True:
                return False

            increasing = False
        else:
            # Either 0 or out of bounds, we are unsafe
            return False


def get_safe_reports() -> int:
    levels = get_input_as_list_of_nums()
    total_safe_reports = 0
    for level in levels:
        if check_level(level):
            total_safe_reports += 1

    return total_safe_reports


print(get_safe_reports())


def get_safe_reports_with_dampener() -> int:
    levels = get_input_as_list_of_nums()
    total_safe_reports = 0

    for level in levels:
        is_safe = check_level(level)
        if is_safe:
            total_safe_reports += 1
            continue

        for i in range(len(level)):
            new_level = [ele for idx, ele in enumerate(level) if idx != i]
            new_is_safe = check_level(new_level)
            if new_is_safe:
                total_safe_reports += 1
                break

    return total_safe_reports


print(get_safe_reports_with_dampener())
