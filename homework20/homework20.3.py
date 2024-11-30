def merge_list(list1, list2):
    combined_list = []
    l1: int = 0
    l2: int = 0

    while l1 < len(list1) and l2 < len(list2):
        if list1[l1] < list2[l2]:
            combined_list.append(list1[l1])
            l1 += 1
        else:
            combined_list.append(list2[l2])
            l2 += 1
    while l1 < len(list1):
        combined_list.append(list1[l1])
        l1 += 1
    while l2 < len(list2):
        combined_list.append(list2[l2])
        l2 += 1

    return combined_list


print(merge_list([1, 2, 4], [1, 3, 4]))
