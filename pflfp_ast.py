class Ast

class Atom(Ast):
    def __init__(self, value):
        self.value = value

class Call(Ast):
    def __init__(self, ident: str, args: int) -> None:
        self.ident = ident
        self.args = args

class Function(Ast):
    def __init__(self, ident: str, body: Token[], params: str[]) -> None:
        self.body = body
        self.params = params 
        self.env = {}

class Def(Ast):
    def __init__(self, ident: str, value: Atom)