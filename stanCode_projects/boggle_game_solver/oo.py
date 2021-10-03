def main():
    lst = [1, 4, 2, 3, 7]
    print(rank_sort(lst))
    print(mystery(lst))


def rank_sort(lst):
    n = len(lst)
    for i in range(1, n):
        temp = lst[i]
        j = i-1
        while j >= 0 and temp < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = temp
    return lst


def mystery(lst):
    lst = [1, 4, 2, 7, 3]

    n = len(lst)
    for i in range(n-1):
        m = i
        for j in range(i+1, n):
            if lst[j] < lst[m]:
                m = j
        if m != i:
            lst[i], lst[m] = lst[m], lst[i]
    return lst


if __name__ == '__main__':
    main()