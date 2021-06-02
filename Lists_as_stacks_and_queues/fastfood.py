from collections import deque

total_food_quantity = int(input())
order_queue = deque()
for order in input().split():
    order_queue.append(int(order))

max_order = max(order_queue)

for i in range(len(order_queue)):
    order = order_queue.popleft()
    if order <= total_food_quantity:
        total_food_quantity = total_food_quantity - order
    else:
        order_queue.appendleft(order)
        break

print(max_order)
if len(order_queue) == 0:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(str(x) for x in order_queue)}")