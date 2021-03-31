array = []
array1 = []
n = int(input("Enter the number of elements"))

v = 1
for i in range(0, n):
    ele = int(input())
    array.append(ele)
    array1.append(v)
    v = v+1

non_i = 1
for x in array1:
    if x not in array:
        non_i = min(x, non_i)

print("\n\nNon occuring integer\n")
print(non_i)