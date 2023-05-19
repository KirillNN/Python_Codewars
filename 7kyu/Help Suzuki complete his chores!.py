def chore_assignment1(c):
    r = [x + y for x, y in zip(sorted(c)[:len(c) // 2], sorted(c, reverse=True))]
    return r


chore_assignment = lambda c: sorted([x + y for x, y in zip(sorted(c)[:len(c) // 2], sorted(c, reverse=True))])

print(chore_assignment([5, 2, 1, 6, 4, 4]))  # [7, 7, 8]
