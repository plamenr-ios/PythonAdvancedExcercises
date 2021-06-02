n = int(input())

stack = []
for i in range(n):
    command = input().split()
    if command[0] == "1":
        stack.append(command[1])
    elif command[0] == "2":
        if stack:
            stack.pop()
    elif command[0] == "3":
        print(max(stack))
    elif command[0] == "4":
        print(min(stack))

print(", ".join(str(x) for x in reversed(stack)))