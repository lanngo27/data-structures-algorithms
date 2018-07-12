def suitable_pieces(width, pieces):
    """
    Returns a tuple (L1, L2) where L1 and L2 are integers in `pieces` which have a sum equal to `width` such that abs(L1 - L2) is largest possible.
    If no pair in `pieces` have a sum equal to width, returns an empty tuple ().
    """

    if len(pieces)==0:
        return()

    tuple = list()
    pieces.sort()
    d = {}
    sum=width*1e7

    # build the hashmap key = val of lst, value = i
    for index, val in enumerate(pieces):
        d[val] = index

    # find the key; if a key is in the dict, and not the same index as the current key
    for i, val in enumerate(pieces):
        if (sum - val) in d and d[sum - val] != i:
            tuple.append((pieces[i], pieces[d[sum-val]]))

    if len(tuple) == 0:
        return ()
    elif len(tuple)==1:
        return tuple[0]
    else:
        diff = list()
        for i, val in enumerate(tuple):
            diff.append(val[1] - val[0])
        maxIndex = diff.index(max(diff))
        return tuple[maxIndex]
