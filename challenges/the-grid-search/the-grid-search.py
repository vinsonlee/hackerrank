#!/usr/bin/env python

t = int(raw_input().strip())
for a0 in xrange(t):
    R, C = raw_input().strip().split(' ')
    R, C = [int(R), int(C)]
    G = []
    G_i = 0
    for G_i in xrange(R):
        G_t = str(raw_input().strip())
        G.append(G_t)
    r, c = raw_input().strip().split(' ')
    r, c = [int(r), int(c)]
    P = []
    P_i = 0
    for P_i in xrange(r):
        P_t = str(raw_input().strip())
        P.append(P_t)

    assert R == len(G)
    found = False

    for i in range(R - r + 1):
        for j in range(C - c + 1):
            # check for a match in the first row
            if G[i][j:j+c] == P[0]:
                match = True
                # check the rest for a possible full match
                for k in range(1, r):
                    if G[i+k][j:j+c] != P[k]:
                        match = False
                        break

                if match:
                    found = True
                    break

    if found:
        print 'YES'
    else:
        print 'NO'
