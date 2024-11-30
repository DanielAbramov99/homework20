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


print(comma("(),[],{}"))
print(comma("(),[],(}"))
