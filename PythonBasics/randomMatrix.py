import random


# Check Symmetrical
def is_symmetrical(list):
    n = len(list)
    for i in range(n // 2):
        if list[i] != list[n - i - 1]:
            return False
        return True


# Create a random lists
list_random = random.sample(range(100), 10)

# Calc Sum of random lists
sum_list = sum(list_random)

print(f"Random List: {list_random}")
print(f"Sum of List: {sum_list}")


# Create a random matrix
matrix_random = [[random.randint(1, 10) for i in range(3)] for j in range(3)]

# Calc Sum of random numbers
sum_matrix = sum(sum(row) for row in matrix_random)

print(f"Random matrix: {matrix_random}")
print(f"Sum of the elements of the matrix: {sum_matrix}")

# Create 3 random elements
random_elements = random.sample(list_random, 3)
print(f"3 random elements {random_elements}")

# Check random lists is Symmetrical or not
print(f"List: {list_random} is symmetrical: {is_symmetrical(list_random)}")

list1 = [1, 3, 5, 7, 5, 3, 1]
print(f"List : {list1} is symmetrical: {is_symmetrical(list1)}")
