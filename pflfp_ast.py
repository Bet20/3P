class Ast:
    def __init__(self) -> None:
        pass

class Atom(Ast):
    def __init__(self, value, type, pos):
        self.value = value
        self.type = type
        self.pos = pos

class Function(Ast):
    def __init__(self, ident: str, body, params) -> None:
        self.ident = ident 
        self.body = body
        self.params = params 
        self.env = {}

class Def(Ast):
    def __init__(self, ident: str, value: Atom):
        self.ident = ident
        self.value = value
