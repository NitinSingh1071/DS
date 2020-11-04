def Linear_search(array, elements):
    for i in range (len(array)):
        if array[i] == elements:
            return i
    return -1

def Binary_search(array, elements):
    first = 0
    array.sort()
    last = len(array)-1
    done = False
    while (first <= last) and not done:
        mid = (first+last)//2
        if array[mid] == elements:
            done = True
        else:
            if elements < array[mid]:
                last = last - 1
            else:
                first = first + 1
    return done


array = [12,200,88,59,373,117]
print(array)
elements = int(input("Enter the number you want to search : "))
print("Type '1' for Linear Search and '2' for Binary Search")
yourChoice = str(input("Enter your choice : "))

if yourChoice == '1':
    
    result = Linear_search(array, elements)
    print(result)
    if result == 1:
        print("Element is present.")
    else :
        print("Element not present.")
else:
    result = Binary_search(array, elements)
    print(result)
    if result == -1:
        print("Element not present.")
    else :
        print("Element is present.")
