def len_longest_chain(tuples_list):
    # Сортировка по второму элементу кортежа
    sorted_tuples = sorted(tuples_list, key=lambda tpl: tpl[1])

    # Инициализация dp
    dp = [1] * len(sorted_tuples)

    for i in range(1, len(sorted_tuples)):
        for j in range(i):
            if sorted_tuples[j][1] < sorted_tuples[i][0]:
                dp[i] = max(dp[i], dp[j] + 1)

    # Возвращаем максимальное значение из dp
    return max(dp)
