def binary_search(data, item):
    low = 0
    upper = len(data) - 1
    while upper >= low:
        mid = int((low+upper) / 2)
        if data[mid] > item:
            upper = mid - 1
        elif data[mid] < item:
            low = mid + 1
        else:
            return mid 
    return None
       
data = [1, 3, 5, 7, 9]
print(binary_search(data, 3))
print(binary_search(data, -1))





 




