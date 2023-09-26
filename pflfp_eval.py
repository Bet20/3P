import pflfp_token as pt

# ----- ENV -----
env: dict = {}
def register_def(id, value):
    env[id.literal] = value
    print(env)

def get_def(id):
    print(env.get(id.literal))
    return env.get(id.literal)

def override_def(id, value):
    if id in env:
        existing_value = env[id]["value"]
        if existing_value is not None and existing_value.type != value.type:
            print(f"error '{id}' is not of type '{value.type}'")
            # You might want to raise an exception here instead of exiting
            # raise ValueError(f"error '{id}' is not of type '{value.type}'")
        env[id]["value"] = value
        for key in env:
            print(key, env[key])
    else:
        print(f"'{id}' not found in the environment")
        exit(-1)

# ---- STACK ----
stack: list = []
stack_push = lambda tok: stack.append(tok)
stack_pop = lambda: stack.pop()

def stack_peek(index, x = 1):
    if len(stack) <= index + x: 
        return stack[index+x]
    return None

# ---- EVALUATION ----
is_type = lambda x, y: x.type == y
are_type = lambda x, y: all(t == y for t in x) # checks if every element in list is of type y

def evaluate(toks: list[pt.Token]):
    capturing_macro = False
    for tok in toks:
        match tok.type:
            case pt.T.PLUS:
                rh = stack_pop()
                lh = stack_pop()
                if is_type(rh, pt.T.INTEGER) and is_type(lh, pt.T.INTEGER):
                    stack_push(pt.Token(pt.T.INTEGER, str(int(lh.literal) + int(rh.literal)), lh.pos))
                elif is_type(rh, pt.T.STRING) and is_type(lh, pt.T.STRING):
                    stack_push(pt.Token(pt.T.STRING, lh.literal + rh.literal, lh.pos))
                else: 
                    print(rh.literal + " + " + lh.literal + " : are not of the same type") 
                    exit(-1)
                
            case pt.T.STAR:
                rh = stack_pop()
                lh = stack_pop()
                if not is_type(rh, pt.T.INTEGER) or not is_type(lh, pt.T.INTEGER): 
                    print(rh.literal + " * " + lh.literal + " : are not of the same type") 
                    exit(-1)
                stack_push(pt.Token(pt.T.INTEGER, str(int(lh.literal) * int(rh.literal)), lh.pos))
            case pt.T.MINUS:
                rh = stack_pop()
                lh = stack_pop()
                if not is_type(rh, pt.T.INTEGER) or not is_type(lh, pt.T.INTEGER): 
                    print(rh.literal + " - " + lh.literal + " : are not of the same type") 
                    exit(-1)
                stack_push(pt.Token(pt.T.INTEGER, str(int(lh.literal) - int(rh.literal)), lh.pos))
            case pt.T.INTEGER:
                stack_push(tok)
            case pt.T.STRING:
                stack_push(tok)
            case pt.T.IDENT:
                stack_push(get_def(tok)) 
            case pt.T.BOOL:
                stack_push(tok)
            case pt.T.GREATER:
                rh = stack_pop()
                lh = stack_pop()
                if is_type(rh, pt.T.INTEGER) or is_type(lh, pt.T.INTEGER): 
                    b = int(rh.literal) > int(lh.literal)
                    t: pt.Token
                    if b:
                        t = pt.Token(pt.T.BOOL, 'T', lh.pos)
                    else:
                        t = pt.Token(pt.T.BOOL, 'F', lh.pos)
                    stack_push(t)
                    pass
                else: 
                    print(rh.literal + " - " + lh.literal + " : are not of the same type") 
                    exit(-1)

            case pt.T.LESSER:
                rh = stack_pop()
                lh = stack_pop()
                if is_type(rh, pt.T.INTEGER) or is_type(lh, pt.T.INTEGER): 
                    b = int(rh.literal) < int(lh.literal)
                    t: pt.Token
                    if b:
                        t = pt.Token(pt.T.BOOL, 'T', lh.pos)
                    else:
                        t = pt.Token(pt.T.BOOL, 'F', lh.pos)
                    stack_push(t)
                    pass
                else: 
                    print(rh.literal + " - " + lh.literal + " : are not of the same type") 
                    exit(-1)

            case pt.T.LABEL:
                stack_push(tok)
            case pt.T.PRINT:
                lh = stack_pop() 
                if lh.type == pt.T.IDENT:
                    item = env.get(lh.literal)
                    if item != None:
                        print(item.literal)
                    else:
                        print("Nil")
                else: 
                    print(lh.literal)
            
            case pt.T.IDENTASSIGN:
                lh = stack_pop()
                env[tok.literal] = lh

            case pt.T.DEF:
                rh = stack_pop()
                lh = stack_pop()
                if not is_type(lh, pt.T.IDENT):
                    print("error, def needs to map to a identifier")
                    exit(-1)

                if get_def(lh) == None:
                    register_def(lh, rh)
                else: 
                    override_def(lh, rh)

            case pt.T.TYPE:
                lh = stack_pop()
                print(lh.literal)
            case _:
                pass
    pass
