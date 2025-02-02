n = int(input("Enter the number of sub-tuples: "))
nested_list = []
largest_element=0
for i in range(n):
    print(f"Enter elements for sub-tuple {i + 1}, separated by spaces: ")
    elements = input().split() 
    elements = list(map(int, elements)) 
    sub_tuple = tuple(elements)  
    nested_list.append(sub_tuple) 
nested_tuple = tuple(nested_list)
for sub_tuple in nested_tuple:
    for element in sub_tuple:
        if largest_element is None or element > largest_element:
            largest_element = element
print(f"The nested tuple is: {nested_tuple}")
print(f"The largest element in the nested tuple is: {largest_element}")
