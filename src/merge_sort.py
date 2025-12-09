def merge_sort(contacts):
    if len(contacts) <= 1:
        return contacts

    mid = len(contacts) // 2
    left = merge_sort(contacts[:mid])
    right = merge_sort(contacts[mid:])

    return merge(left, right)


def merge(left, right):
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i].name.lower() <= right[j].name.lower():
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

while i < len(left):
        sorted_list.append(left[i])
        i += 1

    while j < len(right):
        sorted_list.append(right[j])
        j += 1

    return sorted_list
