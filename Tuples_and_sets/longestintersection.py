n = int(input())
longest_inter = set()


def set_in_range(start, end):
    line = set()
    for i in range(start, end + 1):
        line.add(i)
    return line


for _ in range(n):
    first, second = input().split("-")
    start_first, end_first = first.split(",")
    start_second, end_second = second.split(",")
    first_iter = set_in_range(int(start_first), int(end_first))
    second_iter = set_in_range(int(start_second), int(end_second))
    if len(first_iter.intersection(second_iter)) > len(longest_inter):
        longest_inter = first_iter.intersection(second_iter)

print(f"Longest intersection is {list(sorted(longest_inter))} with length {len(longest_inter)}")