import pflfp_token as pt

# ----- ENV -----
env: dict = {}
def register_def(id, value):
    env[id] = value

def get_def(id):
    env.get(id)

def override_def(id, value):
    if id in env:
        existing_value = env[id]
        if existing_value is not None and existing_value.type != value.type:
            print(f"error '{id}' is not of type '{value.type}'")
            # You might want to raise an exception here instead of exiting
            # raise ValueError(f"error '{id}' is not of type '{value.type}'")
        env[id] = value
        for key in env:
            print(key, env[key])
    else:
        print(f"'{id}' not found in the environment")
        exit(-1)

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
            case pt.T.IDENT:
                if get_def(tok) != None:
                    print("EXISTS")
                    stack_push(env[tok])
                    pass
                stack_push(tok)
            case pt.T.BOOL:
                stack_push(tok)
            case pt.T.LABEL:
                stack_push(tok)
            case pt.T.PRINT:
                lh = stack_pop() 
                print(lh.literal)
            case pt.T.DEF:
                rh = stack_pop()
                lh = stack_pop()
                if not is_type(lh, pt.T.IDENT):
                    print("error, def needs to map to a identifier")
                    exit(-1)

                if get_def(lh) == None:
                    register_def(lh, rh)
                    pass

                override_def(lh, rh)

            case pt.T.TYPE:
                lh = stack_pop()
                print(pt.look_up.get(lh.type))
            case _:
                pass
    pass
