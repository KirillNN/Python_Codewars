def alphabet_war(fight):
    left = ('', 's', 'b', 'p', 'w')
    right = ('', 'z', 'd', 'q', 'm')
    left_power = right_power = 0
    for letter in fight:
        if letter in left:
            left_power += left.index(letter)
        elif letter in right:
            right_power += right.index(letter)
    return ['Right side wins!', "Let's fight again!", 'Left side wins!'][
        (left_power > right_power) + (left_power >= right_power)]


print(alphabet_war('zdqmwpbs'))
