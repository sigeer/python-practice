from sympy import symbols, Eq, solve

x = symbols('x')
eq = Eq(2*x, 10)
solution = solve(eq, x)
print(solution)

a, b = symbols('a, b')
eq1 = Eq(2*a + 3 * b, 50)
eq2 = Eq(a + b, 20)
print(solve((eq1, eq2), (a , b)))
