# score = [1, 2, 3, 4, 5]

# with open("file.txt", "w") as f:
#     for s in score:
#         f.write(str(s) + "\n")
import random
weight = [[random.triangular(-5, 5)for _ in range(2)]for _ in range(2)]
file = open("xor_weight.txt", 'r')
content = file.read()

print(content)
