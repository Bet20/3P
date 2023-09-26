import ppp_parser as ast

def debug_print_ast(ast: list[ast.AstNode]):
    print(ast)
    for node in ast:
        print(node)
