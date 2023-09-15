import pflfp_token as pt

# ----- ENV -----
env: dict = {}

# ---- STACK ----
stack: list = []
stack_push = lambda tok: stack.append(tok)
stack_pop = lambda: stack.pop()

# ---- EVALUATION ----
is_type = lambda x, y: x.type == y
are_type = lambda x, y: all(t == y for t in x) # checks if every element in list is of type y


def evaluate(toks: list[pt.Token]):
    for tok in toks:
        match tok.type:
            case pt.T.PLUS:
                rh = stack_pop()
                lh = stack_pop()
                if not is_type(rh, pt.T.INTEGER) or not is_type(lh, pt.T.INTEGER): 
                    print(rh.literal + " + " + lh.literal + " : are not of the same type") 
                    exit(-1)
                stack_push(pt.Token(pt.T.INTEGER, str(int(rh.literal) + int(lh.literal)), lh.pos))
            case pt.T.STAR:
                rh = stack_pop()
                lh = stack_pop()
                if not is_type(rh, pt.T.INTEGER) or not is_type(lh, pt.T.INTEGER): 
                    print(rh.literal + " * " + lh.literal + " : are not of the same type") 
                    exit(-1)
                stack_push(pt.Token(pt.T.INTEGER, str(int(rh.literal) * int(lh.literal)), lh.pos))
            case pt.T.MINUS:
                rh = stack_pop()
                lh = stack_pop()
                if not is_type(rh, pt.T.INTEGER) or not is_type(lh, pt.T.INTEGER): 
                    print(rh.literal + " - " + lh.literal + " : are not of the same type") 
                    exit(-1)
                stack_push(pt.Token(pt.T.INTEGER, str(int(rh.literal) - int(lh.literal)), lh.pos))
            case pt.T.INTEGER:
                stack_push(tok)
            case pt.T.STRING:
                stack_push(tok)
            case pt.T.BOOL:
                stack_push(tok)
            case pt.T.PRINT:
                lh = stack_pop() 
                print(lh.literal)
            case pt.T.TYPE:
                lh = stack_pop()
                print(pt.look_up.get(lh.type))
            case _:
                pass
    pass
