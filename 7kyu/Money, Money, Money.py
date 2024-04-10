def calculate_years(principal, interest, tax, desired):
    count = 0
    while principal < desired:
        principal += principal * interest - principal * interest * tax
        count += 1
    return count


print(calculate_years(1000, 0.05, 0.18, 1100))
