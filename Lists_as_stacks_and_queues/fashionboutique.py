box_of_clothes = [int(x) for x in input().split()]
capacity = int(input())
total_capacity = 0
racks_used = 0

while box_of_clothes:
    clothing = box_of_clothes.pop()
    if clothing + total_capacity <= capacity:
        total_capacity += clothing
    else:
        box_of_clothes.append(clothing)
        total_capacity = 0
        racks_used += 1

if total_capacity > 0:
    racks_used += 1
print(racks_used)

