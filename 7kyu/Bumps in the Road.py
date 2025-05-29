def bumps(road):
    return ["Woohoo!", "Car Dead"][road.count('n') > 15]


print(bumps("__nn_nnnn__n_n___n____nn__nnn"), "Woohoo!")
print(bumps("_nnnnnnn_n__n______nn__nn_nnn"), "Car Dead")
