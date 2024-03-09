def hit(l):
    if l % 10 == 9:
        return 3
    elif l % 10 == 8:
        return 3
    elif l % 10 == 7:
        return 2
    elif l % 10 == 6:
        return 1
    # elif l % 10 == 4:
    #     return 3
    elif l % 10 == 3:
        return 3
    elif l % 10 == 2:
        return 2
    elif l % 10 == 1:
        return 1

    return 1


system_hit, l = 4, 63
while l > 0:
    player_hit = hit(l)
    if player_hit not in (1, 2, 3):
        print('Strength can be only 1, 2 or 3 units')
        break
    print(f'До моего удара было {l}')
    l -= player_hit
    print(f'После моего удара стало {l}')
    if l <= 0:
        print('ok')
        break
    print(f'До удара ПК было {l}')
    l -= system_hit
    print(f'После удара ПК стало {l}')
    print()
    if l <= 0:
        print(
            f"Player {l + system_hit + player_hit} -> {l + system_hit}\nOpponent {l + system_hit} -> {l}\n")
        break
