num = int(input())
h = num % (60 * 24) // 60
m = num % 60
print(h, m)
