
def remove_duplicates(lst):
    i = 0
    while i < len(lst):
        j = i + 1
        while j < len(lst):
            if lst[i] == lst[j]:
                del lst[j]
            else:
                j += 1
        i += 1

# Example usage
numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5]
remove_duplicates(numbers)
print(numbers)                                             