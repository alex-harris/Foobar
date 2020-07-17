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
    # If the GCD is any number other than 1, this can't work because you eventually get to M = F or GCD = GCD.
    gcd(M, F)
    if gcd(M, F) != 1 and (abs(M - F) % gcd(M, F) == 0):
        return "impossible"

    return str(generations(M, F))


# Recursively subtract M and F until we are back at M = 1 and F = 1.
# Use integer division to create a factor for subtraction.
def generations(m, f):
    if (m == 1 and f > 1) or (f == 1 and m > 1):
        return abs(m - f)
    else:
        if m < f:
            return generations(f, m)
        else:
            return (m // f) + generations(m - m // f * f, f)


# Function found online.
def gcd(m, f):
    if f == 0:
        return m
    else:
        return gcd(f, m % f)


print(solution("1000000000000000000000000000000000000", "92342349521"))
