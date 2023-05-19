def solution(frank, sam, tom):
    if 0 in frank:
        return 1
    return 2


print(solution([0, 4, 10, 11], [3, 6, 8, 9], [1, 2, 5, 7]))
print(solution([1, 2, 4, 5], [3, 6, 8, 10], [0, 7, 9, 11]))
