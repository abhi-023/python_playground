import array as arr
a = arr.array('i', [1, 2, 3])
print("The new created array is : ", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")
print()
b = arr.array('d', [2.5, 3.2, 3.3])
print("The new created array is : ", end=" ")
for i in range(0, 3):
    print(b[i], end=" ")
print("\n")
# inserting array using
# insert() function
a.insert(1, 4)
print("Array after insertion : ", end=" ",)
for i in (a):
    print(i, end=" ")
print("\n")
# adding an element using append()
b.append(4.4)
print("Array after insertion : ", end=" ")
for i in (b):
    print(i, end=" ")
print()
# accessing element of array
print("Access element is: ", a[3])
print("Access element is: ", b[1])
# using pop() to remove element at 2nd position
print ("The popped element is : ", end ="")
print (a.pop(2))
# Print elements of a range
# using Slice operation
Sliced_array = b[1:3]
print("\nSlicing elements in a range 1-3: ")
print(Sliced_array)
# using index() to print index of 1st occurrence of 2
print ("The index of 1st occurrence of 3.2 is : ", end ="")
print (b.index(3.2))
# updating a element in a array
a[2] = 6
print("Array after updation : ", end="")
for i in range(0, 3):
    print(a[i], end=" ")
print()

