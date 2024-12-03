def equalizeArray(arr):
    duplicates = []
    seen = set()
    for x in arr:
        if x in seen and x not in duplicates:
            duplicates.append(x)
        seen.add(x)

    len_arr = len(arr)
    count = 0
    for x in duplicates:
        count = len_arr - arr.count(x)

    return count

if __name__ == '__main__':
    str = "36 12 60 99 78 33 4 21 22 9 12 21 34 76 21 3 3 37 65 27 21 42 11 14 21 88 46 63 79 6 37 94 99 68 76 6 21 86 49 56 22 90 74 83 20 21 94 60 76 75 96 99 92 65 77 26 51 21 77 22 97 34 56"
    arr = list(map(int, str.split()))
    # 55
    result = equalizeArray(arr)
    print(result)