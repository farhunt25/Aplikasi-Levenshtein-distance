\import numpy


def levDist(token1, token2):
    dist = numpy.zeros((len(token1) + 1, len(token2) + 1))

    for t1 in range(len(token1) + 1):
        dist[t1][0] = t1

    for t2 in range(len(token2) + 1):
        dist[0][t2] = t2

    a = 0
    b = 0
    c = 0

    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            if (token1[t1 - 1] == token2[t2 - 1]):
                dist[t1][t2] = dist[t1 - 1][t2 - 1]
            else:
                a = dist[t1][t2 - 1]
                b = dist[t1 - 1][t2]
                c = dist[t1 - 1][t2 - 1]

                if (a <= b and a <= c):
                    dist[t1][t2] = a + 1
                elif (b <= a and b <= c):
                    dist[t1][t2] = b + 1
                else:
                    dist[t1][t2] = c + 1
                printDist(dist, len(token1), len(token2))
                print()
        print()

    printDist(dist, len(token1), len(token2))
    return dist[len(token1)][len(token2)]


def printDist(dist, token1Length, token2Length):
    for t1 in range(token1Length + 1):
        for t2 in range(token2Length + 1):
            print(int(dist[t1][t2]), end=" ")
        print()

string1=input("Masukan Kata 1 = ")
string2=input("Masukan Kata 2 = ")
levDist(string1, string2)
