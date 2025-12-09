def merge_sort(contacts):
    if len(contacts) <= 1:
        return contacts

    mid = len(contacts) // 2
    left = merge_sort(contacts[:mid])
    right = merge_sort(contacts[mid:])

    return merge(left, right)
