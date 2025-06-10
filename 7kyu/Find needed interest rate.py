from decimal import Decimal


def required_interest_rate(initial: Decimal, target: Decimal, years: int, period: int) -> Decimal:
    """
    initial: starting amount (decimal)
    target: desired amount (decimal, >= initial)
    years: number of years (positive integer)
    period: number of times interest is compounded per year (positive integer)
    Returns: required annual interest rate as percentage (decimal)
    """
    n: Decimal = Decimal(years * period)
    result: Decimal = (target / initial) ** (1 / n) - 1
    return result * 100 * period


print(required_interest_rate(Decimal('1000'), Decimal('1210'), 2, 1))
print(required_interest_rate(Decimal('1000'), Decimal('1210'), 2, 2))
print(required_interest_rate(Decimal('1000'), Decimal('1210'), 2, 100))

print(required_interest_rate(Decimal('10000'), Decimal('20000'), 100, 1))
