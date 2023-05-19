def like_or_dislike(lst):
    if not lst:
        return 'Nothing'
    state = lst[0]
    for value in lst[1:]:
        if state == 'Nothing':
            state = value
        elif value == 'Like' and state == 'Dislike':
            state = 'Like'
        elif value == 'Dislike' and state == 'Like':
            state = 'Dislike'
        else:
            state = 'Nothing'
    return state

print(like_or_dislike(['Like', 'Dislike']))

# like_or_dislike(["Dislike"]) ➞ "Dislike"
# like_or_dislike(["Like", "Like"]) ➞ "Nothing"
# like_or_dislike(["Dislike", "Like"]) ➞ "Like"
# like_or_dislike(["Like", "Dislike", "Dislike"]) ➞ "Nothing"
