def solution(l):
    # If len(l) = 2, then there are no lucky triples.
    if len(l) == 2:
        return 0

    # Create a list to use as a counter while maintaining the same index as input l.
    ly = [0] * len(l)
    triples = 0
    for i in range(len(l) - 1):
        # j should always start 1 ahead of i.
        # This loop will check for a lucky double and record if it exists by adding 1 to the ly counter list.
        for j in range(i + 1, len(l)):
            if l[j] % l[i] == 0:
                ly[j] += 1
                # When the if statement is true, the below checks if the pairing was already identified.
                # If so, then that means we now have a lucky triple.
                triples += ly[i]
    return triples
