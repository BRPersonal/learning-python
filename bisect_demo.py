# https://www.kdnuggets.com/lesser-known-python-functions-that-are-super-useful
from bisect import bisect_left, bisect_right, insort

# Let's create a grade tracking system
grades = [60, 70, 75, 85, 90, 95]

# Find where to insert a new grade while keeping the list sorted
new_grade = 82
position = bisect_left(grades, new_grade)
print(f"Insert 82 at position: {position}")

# Insert while maintaining sort order
insort(grades, new_grade)
print(f"Grades after insertion: {grades}")

# Find grade ranges
def grade_to_letter(score):
    breakpoints = [60, 70, 80, 90]  #below 60 is F; >=90 is A
    grades = "FDCBA" # F, D, C, B, A
    position = bisect_right(breakpoints, score)
    print(f"position={position}")
    return grades[position]

print(f"Score 59 gets grade: {grade_to_letter(59)}\n--------")
print(f"Score 60 gets grade: {grade_to_letter(60)}\n--------")
print(f"Score 90 gets grade: {grade_to_letter(90)}\n--------")
print(f"Score 82 gets grade: {grade_to_letter(82)}\n--------")
print(f"Score 75 gets grade: {grade_to_letter(75)}\n--------")