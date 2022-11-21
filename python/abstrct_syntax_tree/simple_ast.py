import ast


tree = ast.parse('''
def f(x):
    print(f'{x} -> {x + 1}')
    return x + 1
''')

print(ast.dump(tree))
