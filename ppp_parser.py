from re import error
import pflfp_token as tk

class AstNode:
    def __init__(self):
        pass

class Atom(AstNode):
    def __init__(self, type: tk.Token, value):
        self.type = type
        self.value = value
        super().__init__()
    
    def __str__(self) -> str:
        return self.value

class Assignment(AstNode):
    def __init__(self, identifier: str, value: AstNode):
        self.identifier = identifier
        self.value = value
        super().__init__()

class BinOp(AstNode):
    # might need to hold left hand and right hand values eventually 
    def __init__(self, op: str):
        self.op = op
        super().__init__()
    
    def __str__(self) -> str:
        return f'{self.op}'

class Macro(AstNode):
    def __init__(self, identifier: str, body: list):
        self.identifier = identifier
        self.body = body
        super().__init__()
    
    def __str__(self) -> str:
        print(f'{self.identifier} -> {self.body}')
        return super().__str__()

class If(AstNode):
    def __init__(self, condition: Atom, consequence: AstNode):
        self.condition = condition
        self.consequence = consequence
        super().__init__()

class Identifier(AstNode):
    def __init__(self, name):
        super().__init__()

def is_type(node: Atom, type: tk.T):
    return node.type == type

def parse(tokens: list[tk.Token], debug: bool = False):
    nodes: list[AstNode] = [] 
    idx: int = 0   

    while True:
        t = tokens[idx]
        match t.type:
            case tk.T.PLUS | tk.T.STAR | tk.T.MINUS | tk.T.SLASH:
                # rh = nodes[idx - 2]
                # lh = nodes[idx - 1]
                # nodes.pop()
                # nodes.pop()
                nodes.append(BinOp(t.literal))
            case tk.T.EOF:
                return nodes
            case tk.T.BLOCK:
                idx += 1 # advance one
                initial_pos = idx

                while tokens[idx].type != tk.T.BLOCK: 
                    idx += 1
                    if len(tokens) <= idx:
                        print("error, macro was not properly defined")
                        exit(-1)

                aux_tok_list = tokens[initial_pos:idx]
                aux_tok_list.append(tk.Token(tk.T.EOF, 'eof', len(aux_tok_list)))
                sub_tok_list = parse(aux_tok_list)
                # advance to get identifier
                idx += 1 
                if not is_type(tokens[idx], tk.T.IDENTASSIGN):
                    # TODO: Error
                    print("error parsing macro, should have an identifier after the block, got " + tokens[idx].literal)
                    exit(-1)
                nodes.append(Macro(tokens[idx].literal, sub_tok_list))
            case _:
                nodes.append(Atom(t.type, t.literal))
        idx += 1
        if debug:
            print(nodes[len(nodes) - 1])
