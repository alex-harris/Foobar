def solution(M, F):
    # M and F are string inputs, convert them to ints.
    M = int(M)
    F = int(F)

    # If M and F are 1, no generations needed.
    if M == 1 and F == 1:
        return str(0)

    # If M or F are zero, then this is impossible.
    if M == 0 or F == 0:
        return "impossible"

    # If M is 1 and F is > 1, return F - M and vice versa.
    if (M == 1 and F > 1) or (F == 1 and M > 1):
        return str(abs(M - F))

    # Work backwards to see how many moves it took to get to M, F.
    # Keep a counter of the generations needed.
    generations = 0

    # Run the loop as long as M and F are greater than 0.
    while M > 0 and F > 0:
        if F > M:
            F -= M
        else:
            M -= F
        generations += 1
        # Once you hit M = 1 and F = 1, end the loop and return generations as a str.
        if M == 1 and F == 1:
            return str(generations)
    return str("impossible")
