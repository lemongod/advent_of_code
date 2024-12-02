from collections import defaultdict


def get_input_as_sorted_lists() -> tuple:
    with open("input.txt", 'r') as f:
        lines = f.read().splitlines()

    list1, list2 = [], []
    for line in lines:
        two_nums = [int(num) for num in line.split(" ") if num != ""]
        list1.append(two_nums[0])
        list2.append(two_nums[1])

    return sorted(list1), sorted(list2)


def get_total_distance() -> int:
    # Sort both lists, then sum the absolute distance
    # between the two numbers at each index
    list1, list2 = get_input_as_sorted_lists()

    assert len(list1) == len(list2)

    total_diff = sum((
        abs(list1[i] - list2[i])
        for i in range(len(list1))
    ))

    return total_diff


print(get_total_distance())


def get_similarity_score() -> int:
    # Sort both lists, then store the similarity score for each
    # number in the first list in a map to avoid recalculating
    list1, list2 = get_input_as_sorted_lists()
    similarity_map = defaultdict(int)

    total_score = 0

    for num in list1:
        if num not in similarity_map:
            similarity_map[num] = len([i for i in list2 if i == num])

        total_score += num * similarity_map[num]

    return total_score


print(get_similarity_score())
