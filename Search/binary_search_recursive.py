def binary_search_recursive(data,left,right,item):
    while right >= left:
        mid=int(left+right)
        if data[mid] > item:
            return binary_search_recursive(data, left, mid - 1, item)
        elif data[mid] < item:
            return binary_search_recursive(data, mid + 1, right, item)
        else:
            return mid
    return None
data = [1, 3, 5, 7, 9]
print(binary_search_recursive(data,0,len(data)-1,3))
print(binary_search_recursive(data,0,len(data)-1,-1))