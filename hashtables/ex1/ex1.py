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
    # for i in weights:
    #     for j in weights:
    #         if ((i + j) == limit):
    #             print([max(i, j), min(i, j)])
    #             print([weights.index(max(i, j)), weights.index(min(i, j))])
    #             return [weights.index(max(i, j)), weights.index(min(i, j))]

    # second pass
    # Think about what we can store in the hash table in order to help us to solve this problem more efficiently
    for w in weights:
        # store each weight in the input list as keys
        keys = w
        # store each weight's list index as its value
        value = weights.index(keys)
        # store new key and value pair in hash table
        hash_table_insert(ht, keys, value)

        # print(f'keys: {keys}, value: {value}')

    # check to see if the hash table contains an entry for `limit - weight`
    for w in weights:
        index = weights.index(w)
        value = hash_table_retrieve(ht, limit - w)
        print(f'value: {value}, index: {index}')
        # If it does, then we've found the two items whose weights sum up to the `limit`
        if value is not None:
            return (value, index)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
