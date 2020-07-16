def solution(src, dest):
    """
    Scratch
    ---------------
    Some manual checks on what numbers you can add/subtract
    From 0, you can only do +10 or +17
    From 1, you can only do +10, +15, or +17
    From 2, you can only do +6, +10, +15, or +17
    From 36, you can do (-17, -15, -10, -6, 6, 10, 15, 17)

    Need to optimize the amount of adds/subtracts to go from src to dest...
    """

    # Start by making a dictionary of the starting squares as keys and possible moves as values.

    sd = {
        0: [10, 17],
        1: [10, 15, 17],
        2: [6, 10, 15, 17],
        3: [6, 10, 15, 17],
        4: [6, 10, 15, 17],
        5: [6, 10, 15, 17],
        6: [6, 15, 17],
        7: [6, 15],
        8: [-6, 10, 17],
        9: [-6, 10, 15, 17],
        10: [-10, -6, 6, 10, 15, 17],
        11: [-10, -6, 6, 10, 15, 17],
        12: [-10, -6, 6, 10, 15, 17],
        13: [-10, -6, 6, 10, 15, 17],
        14: [-10, 6, 15, 17, 15, 17],
        15: [-10, 6, 15],
        16: [-15, -6, 10, 17],
        24: [-15, -6, 10, 17],
        32: [-15, -6, 10, 17],
        40: [-15, -6, 10, 17],
        17: [-17, -15, -6, 10, 15, 17],
        25: [-17, -15, -6, 10, 15, 17],
        33: [-17, -15, -6, 10, 15, 17],
        41: [-17, -15, -6, 10, 15, 17],
        22: [-17, -15, -10, 6, 15, 17],
        30: [-17, -15, -10, 6, 15, 17],
        38: [-17, -15, -10, 6, 15, 17],
        46: [-17, -15, -10, 6, 15, 17],
        23: [-15, -10, 6, 15],
        31: [-15, -10, 6, 15],
        39: [-15, -10, 6, 15],
        47: [-15, -10, 6, 15],
        48: [-15, -6, 10],
        49: [-17, -15, -6, 10],
        50: [-17, -15, -10, -6, 6, 10],
        51: [-17, -15, -10, -6, 6, 10],
        52: [-17, -15, -10, -6, 6, 10],
        53: [-17, -15, -10, -6, 6, 10],
        54: [-17, -15, -10, 6],
        55: [-17, -10, 6],
        56: [-15, -6],
        57: [-17, -15, -6],
        58: [-17, -15, -10, -6],
        59: [-17, -15, -10, -6],
        60: [-17, -15, -10, -6],
        61: [-17, -15, -10, -6],
        62: [-17, -15, -10],
        63: [-17, -10],
        18: [-17, -15, -10, -6, 6, 10, 15, 17],
        19: [-17, -15, -10, -6, 6, 10, 15, 17],
        20: [-17, -15, -10, -6, 6, 10, 15, 17],
        21: [-17, -15, -10, -6, 6, 10, 15, 17],
        26: [-17, -15, -10, -6, 6, 10, 15, 17],
        27: [-17, -15, -10, -6, 6, 10, 15, 17],
        28: [-17, -15, -10, -6, 6, 10, 15, 17],
        29: [-17, -15, -10, -6, 6, 10, 15, 17],
        34: [-17, -15, -10, -6, 6, 10, 15, 17],
        35: [-17, -15, -10, -6, 6, 10, 15, 17],
        36: [-17, -15, -10, -6, 6, 10, 15, 17],
        37: [-17, -15, -10, -6, 6, 10, 15, 17],
        42: [-17, -15, -10, -6, 6, 10, 15, 17],
        43: [-17, -15, -10, -6, 6, 10, 15, 17],
        44: [-17, -15, -10, -6, 6, 10, 15, 17],
        45: [-17, -15, -10, -6, 6, 10, 15, 17],
    }

    # Chess fact: it takes a knight no more than 6 moves to get to any square on an 8x8 board (corner to corner).
    # The below statement will address this edge case.
    if (src == 0 and dest == 63) or (src == 63 and dest == 0) or (src == 7 and dest == 56) or (src == 56 and dest == 7):
        return 6

    # The plan now will be to create 5 lists to account for the different possible moves to get from any src to dest.
    # The first list will represent all possible dest values 1 move from src, the second list will account for 2 moves, etc.

    # First, take the src as a key and retrieve its value from the dictionary.
    # If dest < src, use dest as the key since the move count is the same from square to square either way.

    if src < dest:
        m1 = sd[src]

        # Then, add src to each list element in m1 and create a new list s1, as mentioned above, to represent the possible dest values.
        # If dest is in s1, the function will return 1 since it took 1 move to go from src to dest.

        s1 = [move + src for move in m1]
    elif dest < src:
        m1 = sd[dest]
        s1 = [move + dest for move in m1]
    else:
        # If src == dest then no moves are needed.
        return 0

    # Next, generate list m2 which will have all possible moves from each element of s1, which represent the current position of the knight.

    m2 = []
    for i in range(len(s1)):
        m2.append(sd[s1[i]])
    """
    Right now, the elements of m2 are also lists themselves. We will create s2 by adding the elements of s1
    to their corresponding lists in m2, i.e. the possible moves from that square.
    """
    s2 = []
    for i in range(len(s1)):
        for j in range(len(m2[i])):
            s2.append(s1[i] + m2[i][j])
    # Reduce some clutter by removing duplicate values from s2.
    s2 = list(dict.fromkeys(s2))

    # If dest is in s2, the function will return 2 since it took 2 moves to go from src to dest.
    # Next, generate list m3 which will have all possible moves from each element of s2.

    m3 = []
    for i in range(len(s2)):
        m3.append(sd[s2[i]])

    # Repeat the logic to create s3, m4, s4, m5, s5.

    s3 = []
    for i in range(len(s2)):
        for j in range(len(m3[i])):
            s3.append(s2[i] + m3[i][j])
    s3 = list(dict.fromkeys(s3))

    m4 = []
    for i in range(len(s3)):
        m4.append(sd[s3[i]])

    s4 = []
    for i in range(len(s3)):
        for j in range(len(m4[i])):
            s4.append(s3[i] + m4[i][j])
    s4 = list(dict.fromkeys(s4))

    m5 = []
    for i in range(len(s4)):
        m5.append(sd[s4[i]])

    s5 = []
    for i in range(len(s4)):
        for j in range(len(m5[i])):
            s5.append(s4[i] + m5[i][j])
    s5 = list(dict.fromkeys(s5))
    """
    Final step: checking which list dest exists in and returning that number which corresponds to the number of moves.

    Since these if statements are listed in increasing order, the returned value will be the minimum number of moves 
    as that is the first occurrence of the dest.
    """
    if src < dest:
        if dest in s1:
            return 1
        elif dest in s2:
            return 2
        elif dest in s3:
            return 3
        elif dest in s4:
            return 4
        elif dest in s5:
            return 5
    else:
        if src in s1:
            return 1
        elif src in s2:
            return 2
        elif src in s3:
            return 3
        elif src in s4:
            return 4
        elif src in s5:
            return 5
