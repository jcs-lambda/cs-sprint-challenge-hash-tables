#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    ht = {}

    for ticket in tickets:
        ht[ticket.source] = ticket.destination
    
    route = []
    destination = ht['NONE']
    while destination != 'NONE':
        route.append(destination)
        destination = ht[destination]

    return route + ['NONE']
