def get_max_item(array):
    max_item = 0
    for item in array:
        if item > max_item:
            max_item = item
    return max_item

def selection_sort(array):
    times = len(array) - 1
    for i in range(times):
        if i == 0:
            max_item = get_max_item(array)
            max_index = array.index(max_item)
            print(str(max_index) + " ")
            array[-i - 1], array[max_index] = array[max_index], array[-i - 1]
        else:
            max_item = get_max_item(array[:-i])          
            max_index = array.index(max_item)
            print(str(max_index) + " ")
            array[-i - 1], array[max_index] = array[max_index], array[-i - 1]

counter = int(input())

nums = [int(x) for x in input().split()]

selection_sort(nums)