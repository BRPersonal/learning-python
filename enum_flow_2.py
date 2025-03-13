from enum import Enum

class TaskStatus(Enum):
    TODO = 0
    IN_PROGRESS = 1
    DONE = 2
    ABANDONED = -1

print(f"isEnum: {isinstance(TaskStatus.TODO,Enum)}")

print(f"Enum list:{list(TaskStatus)}")

num_statuses = len(TaskStatus)
print(f"no.of states: {num_statuses}")

print("-----printing states and their values-------")
for status in TaskStatus:
    print(status.name, status.value)
