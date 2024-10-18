from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
left = queue.popleft()
print(left)
left = queue.popleft()
print(left)
print(queue)
