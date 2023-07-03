def rgb_to_grayscale(color):
    R, G, B = (int(color[i:i + 2], 16) for i in range(1, len(color), 2))
    Y = round(0.299 * R + 0.587 * G + 0.114 * B)
    return "#" + f"{Y:02X}" * 3


print(rgb_to_grayscale("#FFFFFF"))
print(rgb_to_grayscale("#000000"))


# def rgb_to_grayscale(color):
#     R, G, B = (int(color[i:i + 2], 16) for i in range(1, len(color), 2))
#     Y = round(0.299 * R + 0.587 * G + 0.114 * B)
#     return "#" + f"{hex(Y)[2:].zfill(2)}" * 3
#
#
# print(rgb_to_grayscale("#FFFFFF"))
# print(rgb_to_grayscale("#000000"))
