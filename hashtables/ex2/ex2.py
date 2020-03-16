#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """

    for ticket in tickets:
        # hash each ticket such that the starting location is the key
        key = ticket.source
        # and the destination is the value
        value = ticket.destination
        # store new key and value in hash table
        hash_table_insert(hashtable, key, value)
        # print(f'key: {ticket.source}, value: {ticket.destination}')

    # since the source of the first ticket is none we set the starting destination to place at the start of route
    route[0] = (hash_table_retrieve(hashtable, "NONE"))
    # print(route, "routr")

    # using the length of the tickets list we can find source of the next ticket in our route
    for i in range(1, length):
        # the `i`th location in the route can be found by checking the hash table for the `i-1`th location
        source_of_next_ticket = route[i-1]
        # and then set the ith location in the route as the next destination using the source retrive
        route[i] = hash_table_retrieve(hashtable, str(source_of_next_ticket))

    # we pop off the none value on the end of our list
    route.pop()

    return route
