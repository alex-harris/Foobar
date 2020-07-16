def solution(l):

    # Strings, need to delimit and then convert to ints

    delim = []
    for item in l:
        delim.append(item.split("."))

    # 2. Convert the numbers.

    # NOTE: I tried this with a nested for loop, but a cleaner way seems to be nested list comprehension.
    #
    # convert = delim
    #   for item in convert:
    #       for subitem in range(len(item)):
    #           item[subitem] = int(item[subitem])

    convert = [[int(subitem) for subitem in item] for item in delim]
    # Now we can properly sort our new list
    convert_sort = sorted(convert)
    # And format the output
    output = [(".".join(str(subitem) for subitem in item)) for item in convert_sort]
    return output


print(solution(["1.0", "1.0.2", "3.1.13", "1.13.2", "2", "0.1", "1", "100.12.13", "99.100", "100.12.9"]))

