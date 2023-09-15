from enum import Enum
from typing import List

class T(Enum):
    STRING = 0
    INTEGER = 1
    FLOAT = 2
    BOOL = 3
    LABEL = 4
    IDENT = 5

    PLUS = 20
    MINUS = 21
    STAR = 22
    SLASH = 23
    HAT = 24
    EXP = 25
    EQ = 26
    DEF = 27
    DOUBLEQUOTES = 28

    QUESTION = 60
    LCURLY = 61
    RCURLY = 62

    TYPE = 98
    PRINT = 99
    FUNCTION = 100
    ILEGAL = 998 
    EOF = 999

class Token:
    def __init__(self, type: T, literal: str, pos: int) -> None:
        self.type = type
        self.literal = literal
        self.pos = int
    
    def __str__(self) -> str:
        return "(" + self.literal + " " + look_up[self.type] + ")"

look_up  = {
    T.BOOL: "bool",
    T.STRING: "string",
    T.INTEGER: "integer",
    T.IDENT: "identifier",
    T.LABEL: "label",
    T.FUNCTION: "function",

    T.PLUS: "operator",
    T.MINUS: "operator",
    T.STAR: "operator",
    T.SLASH: "operator",
    T.DOUBLEQUOTES: "\"",
    T.EOF: "eof",
    T.ILEGAL: "ilegal",
    T.EQ: "operator",
    T.DEF: "def",
    T.PRINT: "print",
    T.TYPE: "type",
        }

# LEXING INLINE FUNCT ONS
is_label = lambda x: x[0] == ":" and x[1:].isalpha()
is_ws = lambda x: x == " " or x == "\n" or x == "\t" or x == "\r"

def read_ident(source: str, index: int):
    i = index 
    begin = i
    while len(source) > i and source[i].isalpha() and not is_ws(source[i]):
        i += 1
    end = i
    return (source[begin:end], i)

def read_string(source: str, index: int):
    i = index
    i += 1
    begin = i
    while source[i] == "\"":
        i += 1
    end = i
    return (source[begin:1-end], i)

def read_integer(source: str, index: int):
    i = index
    begin = i
    while source[i].isdigit():
        i += 1
    end = i
    return (source[begin:end], i)

def tokenize(source: str) -> List:
    size = len(source)
    i = 0
    tokens = []
    while 1:
        if i >= size-1: 
            tokens.append(Token(T.EOF, 'eof', i)) 
            break
        match source[i]:
            case ' ' | '\t' | '\n':
                pass
            case '+': tokens.append(Token(T.PLUS, '+', i))
            case '-': tokens.append(Token(T.MINUS, '-', i))
            case '*': tokens.append(Token(T.STAR, '*', i))
            case '/': tokens.append(Token(T.SLASH, '/', i))
            case '=': tokens.append(Token(T.EQ, '=', i))
            case 'T' | 'F': tokens.append(Token(T.BOOL, source[i], i)) 
            case '"': 
                string, i = read_string(source, i)
                tokens.append(Token(T.STRING, string, i))
            case ':':
                i += 1
                label_ident, i = read_ident(source, i)
                tokens.append(Token(T.LABEL, label_ident, i))
            case _:
                if source[i].isdigit():
                    aux, i = read_integer(source, i)
                    tokens.append(Token(T.INTEGER, aux, i))
                elif source[i].isalpha():
                    aux, i = read_ident(source, i)
                    if aux == "print": tokens.append(Token(T.PRINT, aux, i))
                    elif aux == "type": tokens.append(Token(T.TYPE, aux, i))
                    elif aux == "def": tokens.append(Token(T.DEF, aux, i))
                    
                    else: tokens.append(Token(T.IDENT, aux, i))
                else: 
                    tokens.append(Token(T.ILEGAL, "\0", i))
        i += 1
    return tokens
