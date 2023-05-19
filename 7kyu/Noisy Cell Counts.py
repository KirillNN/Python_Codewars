def cleaned_counts(data):
    result = [data[0]]
    max = data[0]
    for i in range(1, len(data)):
        if max > data[i]:
            result.append(max)
        else:
            result.append(data[i])
            max = data[i]
    return result

from itertools import accumulate

def cleaned_counts(data):
    return [*accumulate(data, max)]