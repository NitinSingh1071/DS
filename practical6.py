def Insertion(array):

    for i in range(1, len(array)):
        item = array[i]
        j = i - 1

        while j >= 0 and array[j] > item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = item

    return array


def Bubblesort(array):
    n = len(array)

    for i in range(n):
        already_sorted = True

        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

                already_sorted = False
        if already_sorted:
            break

    return array

def Selection(array):
    for i in range(len(array)):
        minimum = i
        
        for j in range(i + 1, len(array)):
            if array[j] < array[minimum]:
                minimum = j

        array[minimum], array[i] = array[i], array[minimum]
            
    return array

array = [45,89,23,98,5,78,32]
print("The list is : ",array)
print("Type 'I' for Insertion sort, 'B' for Bubble sort, 'S' for selection sort")
yourChoice = str(input("Your choice : "))

if yourChoice == "I":
    print("Insertion sort : ",Insertion(array))
elif yourChoice == "B":
    print("Bubble sort : ",Bubblesort(array))
elif yourChoice == "S":
    print("Selection sort : ",Selection(array))
else :
    print("Invalid Input")
