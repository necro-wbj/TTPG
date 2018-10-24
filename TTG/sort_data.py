import random
ans = []
with open("atrain_data.txt", "r") as file:
    for f in file:
        ans.append(f.strip())
    for i in range(len(ans)):
        ans[i] = ans[i][1:-1].split(",")
        for j in range(len(ans[i])):
            ans[i][j] = int(ans[i][j])
b = []
with open("qtrain_data.txt", "r") as file:
    for f in file:
        b.append(f.strip())
for i in range(len(b)):
    b[i] = b[i][1:-1].split(",")
    for j in range(len(b[i])):
        b[i][j] = int(b[i][j])
j = 0
r = [i for i in range(len(b))]
random.shuffle(r)

# for i in range(len(b)):
#     if ans[i].index(1) != j:
#         for k in range(len(b) - 1, i, -1):
#             if ans[k].index(1) == j:
#                 ans[i], ans[k] = ans[k], ans[i]
#                 b[i], b[k] = b[k], b[i]
#                 break
#     j += 1
#     if(j == 9):
#         j = 0
# for i in range(len(ans)):
#     print(b[i], ans[i])
# f = open("qtrain_data.txt", "w")
# for i in b:
#     f.write(str(i))
#     f.write("\n")
# b = []
# f = open("atrain_data.txt", "w")
# for i in ans:
#     f.write(str(i))
#     f.write("\n")
