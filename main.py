import sys
import pflfp_token
import pflfp_eval

def read_line():
    inp = input('>> ')
    tokens = pflfp_token.tokenize(inp)
    pflfp_eval.evaluate(tokens)

def main():
    tokens = pflfp_token.tokenize("3913 3231 + type")
    pflfp_eval.evaluate(tokens)

    if len(sys.argv) > 1: # is reading file
        file = open(sys.argv[1], "r")
        input = file.read()
        tokens = pflfp_token.tokenize(input)
        pflfp_eval.evaluate(tokens)
        exit(0)

    while 1:
        read_line()

main()
