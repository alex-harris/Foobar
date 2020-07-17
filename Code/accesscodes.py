def solution(l):
    # If len(l) = 2, then there are no lucky triples.
    if len(l) == 2:
        return 0

    triples = 0
    for i in range(len(l) - 2):
        # j should always start 1 ahead of i.
        for j in range(i + 1, len(l) - 1):
            # If a lucky double is identified, then check the rest of l for a z to complete the triple.
            if l[j] % l[i] == 0:
                for k in range(j + 1, len(l)):
                    if l[k] % l[j] == 0:
                        triples += 1
    return triples
