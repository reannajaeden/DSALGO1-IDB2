#[23,89, 7, 56, 44] – Implement the Bubble Sort Algorithm for the Dataset and
#sort the data into ascending order.
arr1=[23,89,7,56,44]
for i in range (len(arr1)):
    for j in range(0,len(arr1)-i-1):
        if arr1[j] > arr1[j+1]:
            arr1[j], arr1[j+1] =arr1[j+1],arr1[j]
print("1. Values [23,89,7,56,44] in Ascending Order: ")
print(arr1)

# [12, 78, 91, 34, 62] – Implement the
#Insertion Sort Algorithm for the Dataset and sort the data into ascending
#Order.
arr2=[12, 78, 91, 34, 62]
for i in range(1,len(arr2)):
    key = arr2[i]
    j=i-1
    while j>=0 and key < arr2[j]:
        arr2[j+1] = arr2[j]
        j-=1
    arr2[j+1] = key
print("2. Values [12, 78, 91, 34, 62] in Ascending Order: ")
print(arr2)

#  [5, 99, 48, 15, 67] – Implement the
#Selection Sort Algorithm for the Dataset and sort the data into descending
#Order.
arr3=[5, 99, 48, 15, 67]
for i in range(len(arr3)):
    min_idx= i
    for j in range(i+1, len(arr3)):
        if arr3[min_idx] < arr3[j]:
            min_idx = j
    arr3[i], arr3[min_idx] = arr3[min_idx], arr3[i]
print("3. Values [5, 99, 48, 15, 67] in Descending Order: ")
print(arr3)

#[38, 82, 25, 74, 13] – Implement the
#Insertion Sort Algorithm for the Dataset and sort the data into descending
#Order.
arr4=[38, 82, 25, 74, 13]
for i in range(1,len(arr4)):
    key = arr4[i]
    j=i-1
    while j>=0 and key > arr4[j]:
        arr4[j+1] = arr4[j]
        j-=1
    arr4[j+1] = key
print("4. Values [38, 82, 25, 74, 13]  in Descending Order: ")
print(arr4)

#Copy all of the values from the
#second index and third index of the previous datasets into one
#dataset. After copying, sort the data into ascending order and descending
#order each order of the dataset is inserted into a separate list/array.
arr5=[44,56,62,78,48,15,38,25]
for i in range (len(arr5)):
    for j in range(0,len(arr5)-i-1):
        if arr5[j] > arr5[j+1]:
            arr5[j], arr5[j+1] =arr5[j+1],arr5[j]
print("5. Values [44,56,62,78,48,15,38,25] in Ascending Order: ")
print(arr5)
#descending Order
arr6=[44,56,62,78,48,15,38,25]
for i in range (len(arr6)):
    for j in range(0,len(arr6)-i-1):
        if arr6[j] < arr6[j+1]:
            arr6[j], arr6[j+1] =arr6[j+1],arr6[j]
print("5. Values [44,56,62,78,48,15,38,25] in Descending Order: ")
print(arr6)

# Create a new list/array or values copying all of
#the values from item number 1 to 4. Implement the Selection
#Sort Algorithm and sort the data into ascending order.
arr7=[23,89,7,56,44,12, 78, 91, 34, 62,5, 99, 48, 15, 67,38, 82, 25, 74, 13]
for i in range(len(arr7)):
    min_idx= i
    for j in range(i+1, len(arr7)):
        if arr7[min_idx] > arr7[j]:
            min_idx = j
    arr7[i], arr7[min_idx] = arr7[min_idx], arr7[i]
print("6. Values [23,89,7,56,44,12, 78, 91, 34, 62,5, 99, 48, 15, 67,38, 82, 25, 74, 13] in Ascending Order: ")
print(arr7)

# Print the even and odd values of the
#list/array created in item number 6.
arr8=[23,89,7,56,44,12, 78, 91, 34, 62,5, 99, 48, 15, 67,38, 82, 25, 74, 13]
evenNum=[num for num in arr8 if num % 2==0]
oddNum=[num for num in arr8 if num % 2 != 0]
print("Even Numbers: ", evenNum)
print("Odd Numbers: ",oddNum)








