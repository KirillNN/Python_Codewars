def find_caterer(budget, people):
    if not people or budget < people * 15:
        return -1
    if budget >= people * 30 * [1, 0.8][people > 60]:
        return 3
    if budget >= people * 20:
        return 2
    return 1
