# even or odd number in array
a = [1,2,3,4,5,6,7,8,9]

even = []
odd = []
for i in a:

    if (i%2==0):
        even.append(i)
    else:
        odd.append(i)

print(even)
print(odd)
