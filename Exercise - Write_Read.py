# 1. write a function countNum(num so that it returns number of occurrences of a number in that file
# e.g, countNum(9) should return 2, countNum(100) should return 0
#create a input.txt file that contains numbers separated by comma as shown below

# Pair numbers provided
pair_numbers = [
    (6, 8),
    (7, 6),
    (2, 8),
    (9, 5),
    (9, 6)
]

# Writing pair numbers to input.txt file
with open("D:\\AI Engineering\\Python\\My_Projects\\Project1\\input.txt", "w") as f:
    for pair in pair_numbers:
        f.write(f"{pair[0]}, {pair[1]}\n")

def countNum(num):
    count = 0
    with open("input.txt", "r") as f:
        for line in f:
            numbers = line.strip().split(',')
            for n in numbers:
                if int(n.strip()) == num:  # Use strip() to remove any leading/trailing spaces
                    count += 1
    return count

cnt = countNum(6)
print(cnt)

# Change input.txt so that when program ends it contains sum of all numbers
# in a line as shown below
"""
sum: 14 | 6, 8
sum: 13 | 7, 6
"""

# Open input.txt file for reading and input_sum.txt file for writing
with open("D:\\AI Engineering\\Python\\My_Projects\\Project1\\input.txt", "r") as file:
    with open("D:\\AI Engineering\\Python\\My_Projects\\Project1\\input_sum.txt", "w") as file_w:
        # Iterate through each line in the input.txt file
        for line in file:
            # Split the line into individual numbers and convert them to integers
            numbers = [int(num) for num in line.strip().split(", ")]
            # Calculate the sum of the numbers
            print(f"numbers: {numbers}")
            total = sum(numbers)

            print(f"sum: {total} | {line}")
            # Write the sum along with the original line to the input_sum.txt file
            prt = file_w.write(f"sum: {total} | {line}")

print("File has been modified successfully!")


