def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        result.append([i, 'Fizz', 'Buzz', 'FizzBuzz'][(not i % 3) + (not i % 5) * 2])
    return result

# def fizzbuzz(n):
#     return ['Fizz'*(not i%3) + 'Buzz'*(not i%5) or i for i in range(1, n+1)]


print(fizzbuzz(30))
