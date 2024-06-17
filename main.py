# a = 5
# while True:
#     print(a)
#     a-=1


# #завдання 1
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# for i in range(a, b, 1):
#     print(i)

# #завдання 2

# c = int(input("Enter first number: "))
# d = int(input("Enter second number: "))
# for i in range(c, d, 1):
#     if i%2 == 0:
#         continue
#     print(i)

# #завдання 3

# e = int(input("Enter first number: "))
# f = int(input("Enter second number: "))
# for i in range(e, f, 1):
#     if i%2 != 0:
#         continue
#     print(i)

# #завдання 4

# g = int(input("Enter first number: "))
# h = int(input("Enter second number: "))
# for i in range(g, h, -1):
#     print(i)

#завдання 5

start = int(input("Enter start: "))
end = int(input("Enter end: "))
if end > start:
    for i in range(end, start, 1):
        if i%2 == 0:
            continue
        print(i)
else:
    for i in range(start, end, 1):
        if i%2 == 0:
            continue
        print(i)
    