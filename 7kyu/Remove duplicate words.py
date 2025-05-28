def remove_duplicate_words(s: str):
    result = []
    for word in s.split():
        if word not in result:
            result.append(word)
    return ' '.join(result)
