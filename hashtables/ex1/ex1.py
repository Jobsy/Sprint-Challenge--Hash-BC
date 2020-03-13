#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # first pass
    for i in weights:
        for j in weights:
            if ((i + j) == limit):
                print([max(i, j), min(i, j)])
                print([weights.index(max(i, j)), weights.index(min(i, j))])
                return [weights.index(max(i, j)), weights.index(min(i, j))]

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
