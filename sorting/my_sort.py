def my_sort(lst):
    """Return the sequence `lst` sorted in-place in ascending order."""
    # Note: in-place means, that the method shouldn't create and return
    # another list, but sort the same list object it received, and
    # return it.
    # It is allowed however, to copy values to another list and use it
    # to get the given list sorted. Note that this will take extra
    # memory though.
    # The solution must be fast in order to complete the biggest sorting
    # problems in time before the time runs out and the evaluator
    # terminates the attempt.
    # Note: If you are implementing a recursive mergesort, remember to
    # divide only up until a certain sublist size, eg. 20, and then sort
    # the sublist with another method, eg. selection sort. Dividing and
    # recursing up until sublists of size 1 is not effective!

    length = len(lst)
    if length > 9:
        midpoint = length // 2
        left_half = my_sort(lst[:midpoint])
        right_half = my_sort(lst[midpoint:])
        i = 0
        j = 0
        k = 0
        left_length = len(left_half)
        right_length = len(right_half)
        while i < left_length and j < right_length:
            if left_half[i] < right_half[j]:
                lst[k] = left_half[i]
                i += 1
            else:
                lst[k] = right_half[j]
                j += 1
            k += 1

        while i < left_length:
            lst[k] = left_half[i]
            i += 1
            k += 1

        while j < right_length:
            lst[k] = right_half[j]
            j += 1
            k += 1

    insert_sort(lst)

    return lst

def insert_sort(list):
    for index in range(1, len(list)):
        while 0 < index and list[index] < list[index - 1]:
            list[index], list[index - 1] = list[index - 1], list[index]
            index -= 1
    return list