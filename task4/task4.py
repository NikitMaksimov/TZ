arr = []

n = int(input("Введите кол-во элементов: "))

for i in range(0, n):
    elem = int(input())
    arr.append(elem) 

sorted_arr = sorted(arr)
m = sorted_arr[len(arr) // 2]

s = 0
for i in arr:
    s += abs(i - m)

print(s)