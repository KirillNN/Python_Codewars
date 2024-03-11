def fibonacci(seq, n):
    return seq[n - 1] + seq[n - 2]


def pisano(n):
    seq_fibonacci = [0, 1]
    seg_pisano = [0, 1]

    for i in range(2, n * 6 + 2):  # Период Пизано обязательно меньше n * 6
        seq_fibonacci.append(seq_fibonacci[i - 1] + seq_fibonacci[i - 2])
        seq_fibonacci[i] %= n

        if seq_fibonacci[-2:] == [0, 1]:  # Находим период Пизано
            return len(seg_pisano) - 1

        seg_pisano.append(seq_fibonacci[i])

    return None


print(pisano(5))
