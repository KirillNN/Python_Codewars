def is_ruby_coming(lst):
    result = list(filter(lambda x: x.get('language') == 'Ruby', lst))
    return len(result) > 0


def is_ruby_coming(lst):
    return any(x["language"] == "Ruby" for x in lst)