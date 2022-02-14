n, m = map(int, input().split())
a_list = []
b_list = []
diff_list = []
count = 0

for i in range(n):
    a, b = map(int, input().split())
    a_list.append(a)
    b_list.append(b)

for i in range(n):
    diff_list.append(a_list[i] - b_list[i])

diff_list.sort(reverse=True)

x = sum(a_list) - m

if sum(b_list) > m:
    print(-1)
    exit()
else:
    for i in diff_list:
        if x > 0:
            x = x - i
            count += 1
print(count)
