def code_tracing():
    sc = [1]
    if sc.pop() == 1.0:
        print('Answer1:', sc)
    else:
        print('Answer2:', sc)
    cs = [101]
    mystery(sc, cs)
    print('Answer3:', sc, cs)


def mystery(cs, sc):
    if len(cs):
        print('Answer5:', sc)
    else:
        print('Answer6:', sc)
    cs = sc


if __name__ == '__main__':
    code_tracing()