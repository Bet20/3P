import sys
import pflfp_token
import pflfp_eval
import ppp_parser as parser
import ppp_internals as internals

def read_line():
    inp = input('>> ')
    tokens = pflfp_token.tokenize(inp)
    print(tokens)
    for x in tokens:
        print(x)
    pflfp_eval.evaluate(tokens)

def main():
    tokens = pflfp_token.tokenize("| 2 + | =add")
    nodes = parser.parse(tokens, True) 
    internals.debug_print_ast(nodes)

#    pflfp_eval.evaluate(tokens)
    
    if len(sys.argv) > 1: # is reading file
        file = open(sys.argv[1], "r")
        input = file.read()
        tokens = pflfp_token.tokenize(input)
        pflfp_eval.evaluate(tokens)
        exit(0)

    while 1:
        read_line()

main()
