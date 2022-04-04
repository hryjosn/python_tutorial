# for i in range(1,10):
#     for x in range(1, 10):
#         if x==3:
#             break
#         print("x",x)
#     print("i:",i)

# for x in range(1, 10):
#     if x == 3:
#         continue
#     print(x)

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4, ]

s = set(nums)
l = list(s)
i = len(nums) - len(s)  # 重複的數量
for x in range(i):
    l.append("_")

print(len(s), l)
