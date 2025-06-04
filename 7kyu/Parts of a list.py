def partlist(arr):
    result = []
    for i in range(len(arr) - 1):
        part = (
            "{}".format(*[' '.join(arr[:i + 1])]),
            "{}".format(*[' '.join(arr[i + 1:])])
        )
        result.append(part)
    return result


print(partlist(["cdIw", "tzIy", "xDu", "rThG"]))

# testing(partlist(["cdIw", "tzIy", "xDu", "rThG"]),
#         [("cdIw", "tzIy xDu rThG"), ("cdIw tzIy", "xDu rThG"), ("cdIw tzIy xDu", "rThG")])
