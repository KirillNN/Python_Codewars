from pprint import pprint


def greet_developers(lst: list):
    for item in lst:
        firstname = item.get('firstName')
        language = item.get('language')
        item['greeting'] = f'Hi {firstname}, what do you like the most about {language}?'
    return lst


def greet_developers(lst):
    return [{**dev, 'greeting': f"Hi {dev['firstName']}, what do you like the most about {dev['language']}?"} for dev in
            lst]


# import codewars_test as test
# from solution import greet_developers
#
#
# @test.describe('Sample Test Cases')
# def example_tests():
#     @test.it('Example Test Case')
#     def example_test_case():
#         list1 = [
#             {'firstName': 'Sofia', 'lastName': 'I.', 'country': 'Argentina', 'continent': 'Americas', 'age': 35,
#              'language': 'Java'},
#             {'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia', 'continent': 'Europe', 'age': 35,
#              'language': 'Python'},
#             {'firstName': 'Madison', 'lastName': 'U.', 'country': 'United States', 'continent': 'Americas', 'age': 32,
#              'language': 'Ruby'}
#         ]
#
#         answer = [
#             {'firstName': 'Sofia', 'lastName': 'I.', 'country': 'Argentina', 'continent': 'Americas', 'age': 35,
#              'language': 'Java',
#              'greeting': 'Hi Sofia, what do you like the most about Java?'
#              },
#             {'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia', 'continent': 'Europe', 'age': 35,
#              'language': 'Python',
#              'greeting': 'Hi Lukas, what do you like the most about Python?'
#              },
#             {'firstName': 'Madison', 'lastName': 'U.', 'country': 'United States', 'continent': 'Americas', 'age': 32,
#              'language': 'Ruby',
#              'greeting': 'Hi Madison, what do you like the most about Ruby?'
#              }
#         ]
#
#         test.assert_equals(greet_developers(list1), answer)


list1 = [
    {'first_digit': 1, 'second_digit': 2},
    {'first_digit': 2, 'second_digit': 3},
    {'first_digit': 3, 'second_digit': 4},
    {'first_digit': 4, 'second_digit': 5},
    {'first_digit': 5, 'second_digit': 6}
]
# добавление пары ключ-значение в словарь с предварительной распаковкой
list1 = [{**x, 'result': x['first_digit'] + x['second_digit']} for x in list1]

pprint(list1)
