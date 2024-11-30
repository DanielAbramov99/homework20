def has_no_duplicates(lst: sorted(list[int])):
    no_duplicates = []
    [no_duplicates.append(number) for number in lst if number not in no_duplicates]
    return no_duplicates


print(sorted(has_no_duplicates([1, 9, 8, 4, 2, 2, 4, 6, 7])))
print(has_no_duplicates([1, 1, 1, 2, 3, 4, 5, 6, 7, 7, 7, ]))
