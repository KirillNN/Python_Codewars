def fibonacci(seq, n):
    return seq[n - 1] + seq[n - 2]


def pisano(n):
    seq_fibonacci = [0, 1, 1]
    seg_pisano = [0, 1, 1]
    for i in range(3, 20):
        seq_fibonacci.append(fibonacci(seq_fibonacci, i))
        seg_pisano.append(seq_fibonacci[i] % n)
    return seg_pisano


print(pisano(3))
