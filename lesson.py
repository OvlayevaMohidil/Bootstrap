def findMax(array):
    max = array[0]
    max_index = 0
    for n in range(1,len(array)):
        if array[n]>max:
            max = array[n]
            max_index = n
    return max_index

def selectSort(array):
    newArray = []
    for n in range(len(array)):
        max_index = findMax(array)
        newArray.append(array.pop(max_index))
        print(array)
        print("-----")
    return newArray

if name == 'lesson':
    array = [3, 4, 1, 6, 10, 20, 9, 8]
    newArray = selectSort(array)
    print(newArray)