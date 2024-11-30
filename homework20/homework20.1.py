def comma(str1: str):
    brackets_list: list[str] = []
    brackets: dict[str, str] = {"}": "{", "]": "[", ")": "(", }
    for char in str1:
        if char in brackets.values():
            brackets_list.append(char)
        elif char in brackets.keys():
            if not brackets_list or brackets_list[-1] != brackets[char]:
                return False
            brackets_list.pop()

    return not brackets_list


def has_no_duplicates(lst: sorted(list[int])):
    no_duplicates = []
    [no_duplicates.append(number) for number in lst if number not in no_duplicates]
    return no_duplicates


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


print(comma("(),[],{}"))
print(comma("(),[],(}"))
print(sorted(has_no_duplicates([1, 9, 8, 4, 2, 2, 4, 6, 7])))
print(has_no_duplicates([1, 1, 1, 2, 3, 4, 5, 6, 7, 7, 7, ]))
print(merge_list([1, 2, 4], [1, 3, 4]))
