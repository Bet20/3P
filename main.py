import sys

stack: list = []
env: dict = {}

# builtins functions
sum = lambda x, y: x + y
min = lambda x, y: x - y
mul = lambda x, y: x * y
div = lambda x, y: x / y
exp = lambda x, y: x ^ y

env.update({
    "+": sum,
    "-": min,
    "*": mul,
    "/": div,
    "^": exp
})

def stack_push(x):
    stack.append(x)

def stack_pop():
    return stack.pop()

def read_line():
   inp = input('>> ')
   toks = inp.split(" ")
   eval(toks)

def error(message: str):
    print("error: " + message) 
    exit(1)

# evaluates a list of tokens
def eval(toks: list):
   for value in toks:
       match value:
            case "+":
                rh = stack_pop()
                lh = stack_pop()
                stack_push(lh+rh)

            case "*":
                rh = stack_pop()
                lh = stack_pop()
                stack_push(lh*rh)

            case "-":
                rh = stack_pop()
                lh = stack_pop()
                stack_push(lh-rh)

            case "?": # (condition) (what to do) ?
                consequence = stack_pop() 
                condition = stack_pop()
                if(condition):
                    stack_push(consequence)

            case ">":
                rh = stack_pop()
                lh = stack_pop()
                stack_push(rh > lh)
            case "<":
                rh = stack_pop()
                lh = stack_pop()
                stack_push(rh < lh)
            case "=":
                rh = stack_pop()
                lh = stack_pop()
                stack_push(rh == lh)

            case ")":
                stack.clear()
            
            case "print":
                lh = stack_pop()
                if lh != None:
                    print(lh)
                else:
                    error("Stack is empty, nothing to print!")
                stack_push(lh)
            
            case "«" | "def":
                value = stack_pop()
                ident = stack_pop()
                if ident.isalpha():
                    env[ident] = value

            case _:
                if value.isnumeric():
                    if value.isdecimal():
                        stack_push(int(value))
                    else:
                        stack_push(float(value))

                if value.isalpha():
                    if env.get(value) != None:
                        stack_push(env.get(value))
                    else:
                        stack_push(value)



def main():
    if len(sys.argv) > 1: # is reading file
        file = open(sys.argv[1], "r")
        input = file.read().split()
        print(input) 
        eval(input)
        exit(0)

    while 1:
        read_line()

main()
