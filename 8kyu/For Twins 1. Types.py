def type_validation(variable, _type):
    return type(variable).__name__ == _type

print(type_validation(True, 'int'))
print(type_validation(42, 'int'))