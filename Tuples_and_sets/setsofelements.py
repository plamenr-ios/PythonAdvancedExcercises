n, m = input().split()
n, m = int(n), int(m)

set_a, set_b = set(), set()

for _ in range(n):
    set_a.add(int(input()))

for _ in range(n):
    set_b.add(int(input()))

present_in_both = set_a.intersection(set_b)

for element in present_in_both:
    print(element)
