# 3 "Cobblestones" and 2 "Sticks"
#  "Wood" can be converted into 4 "Sticks"

def stone_pick(arr: list):
    count_cobblestones = arr.count('Cobblestone')
    if not len(arr) or not count_cobblestones:
        return 0
    count_stick = arr.count('Sticks') + arr.count('Wood') * 4
    return min(count_stick // 2, count_cobblestones // 3)


print(stone_pick(["Sticks"] * 4 + ["Cobblestone"] * 6))
