def combine_sets(set1: set, set2: set) -> set:
    """
    Combines two sets into one.

    Args:
        set1 (set): First set.
        set2 (set): Second set.

    Returns:
        set: Combined set.
    """
    return set1.union(set2)

def update_set(set1: set, set2: set) -> set:
    """
    Given two Python sets, updates the first set with items that exist only in the second set and not in the first set.
    :param set1:
    :param set2:
    :return:
    """
    return set1.update(set2 - set1) or set1