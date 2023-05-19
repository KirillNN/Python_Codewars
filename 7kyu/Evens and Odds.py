# def evens_and_odds(n):
#     return [f'{n:b}', f'{n:x}'][n % 2]

evens_and_odds = lambda n: [f'{n:b}', f'{n:x}'][n % 2]

print(evens_and_odds(19))
