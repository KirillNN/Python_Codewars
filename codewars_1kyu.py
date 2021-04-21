MOD = 998244353
mods = [0, 1]
for x in range(2, 10001):
    mods.append((MOD - MOD // x) * mods[MOD % x] % MOD)


def height(n, m):
    x, y = 0, 1
    m %= MOD

    for i in range(1, n + 1):
        y = y * (m - i + 1) * mods[i] % MOD
        x = (x + y) % MOD
    return x % MOD


# print(height(1, 51))


x = 0
for i in range(1, 100000000):
    x+=1/i**2
    # print(x)
print((x*6)**0.5)
# print(x)
