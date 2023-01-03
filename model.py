import sympy

def execute_example(example: str) -> str:
    try:
        ans = sympy.simplify(example)
        return ans
    except ValueError:
        print('Incorrect input')

def execute_equasion(equasion):
    x = sympy.Symbol('x')
    try:
        ans = sympy.solve(equasion, x)
        return ans
    except ValueError:
        print('Incorrect input')

def simplification(equasion):
    try:
        ans = sympy.simplify(equasion)
        return ans
    except ValueError:
        print('Incorrect input')