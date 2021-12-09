n, vol = map(int, input().split()) ## number of things, whole space
res = [] ## things[weight, value, value/weight]
electN = [0] * n ## if elected
for i in range(n):
    hpd, hpr = map(int, input().split())
    res.append([hpd, hpr, hpr / hpd])
res.sort(key=lambda x: x[2], reverse=True)
mPretium = 0 ## max value
pondus, pretium = 0, 0 ## current weight, value

def elegere(r):
    global n, vol, res, mPretium, pondus, pretium
    if r == n:
        return
    if pondus + res[r][0] < vol:
        electN[r] = 1
        pondus += res[r][0]
        pretium += res[r][1]
        if pretium > mPretium:
            mPretium = pretium
        if limitare(r + 1) >= mPretium:
            elegere(r + 1)
        electN[r] = 0
        pondus -= res[r][0]
        pretium -= res[r][1]
    elegere(r + 1)
    return

def limitare(r):
    global n, vol, pretium, pondus
    finisPretii = pretium
    spatium = vol - pondus
    k = r
    while k < n and spatium >= res[k][0]:
        spatium -= res[k][0]
        finisPretii += res[k][1]
        k += 1
    if k < n:
        finisPretii += (res[k][1] * spatium / res[k][0])
    return finisPretii

elegere(0)
print(mPretium)
