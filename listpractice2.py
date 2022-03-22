#Given a sorted array arr[] of size N. Find the element that appears only once in the array. All other elements appear exactly twice.

#Example 1:

#Input:
#N = 11
#arr[] = {1, 1, 2, 2, 3, 3, 4, 50, 50, 65, 65}
#Output: 4
#Explanation: 4 is the only element that
#appears exactly once.
l1 = [1, 1, 2, 2, 3, 3, 4, 50, 50, 65, 65]
arr = l1
n = len(arr)
d2 = {}
for num in l1:
    if num in d2:
        d2[num] = d2[num]+ 1
    else:
        d2[num]=1


for key in d2.keys():
    #values = d2.values()
    if d2[key] == 1:
        print(str(key) + " " + " is the only element that appears once")

i = 0
while (i < (n - 1)):
    if arr[i] != arr[i + 1]:
        print(arr[i])
        break
    else:
        i += 2
if i == n - 1:
    print(arr[i])

    #print(key, ":", d2[key])
flag = False
for i in range(0,n-1,2):
    if arr[i] != arr[i+1]:
        flag = True
        print(arr[i])
        break
if flag == False:
    print(arr[n-1])


