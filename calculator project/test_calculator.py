from calculator import calculate
assert calculate("1", 2, 3) == 5
print("Addition test passed")

assert calculate("2", 7, 2) == 5
print("Subtraction test passed")

assert calculate("3", 3, 2) == 6
print("Multiplication test passed")

assert calculate("4", 25, 5) == 5
print("Division test passed")

assert calculate("4", 5, 0) == "Answer is undefined"
print("Division by zero test passed")