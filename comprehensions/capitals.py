cities = [x for x in input().split(", ")]
capitals = [x for x in input().split(", ")]
combination = zip(cities, capitals)

for i, k in tuple(combination):
    print(f"{str(i)} -> {str(k)}")
