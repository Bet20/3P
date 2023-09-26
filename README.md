# 3P _ Postfix Programming Pidgin

Stack based language created to learn more about programming languages and as golf-like language eventually.

Greet example:
```
"John" =john "Hello " john + print
```

### Syntax
| PFLPF  | C |
|---|---|
| `10 =n` | `int n = 10`|
| `10 10 +`  | `10 + 10` |
| `"bad" "ok" 10 10 > ?`  | `if (10 > 10) { return "ok" } else {return "bad"}` |

### Types
- Integers
- Floats
- Strings
- Booleans
- Labels
- *Some composite type eventually*

### Examples
```
# | Not implemented yet |
# macro to prefix text with '*'
# prefix("hello", 3) -> "***hello"
"hello" 3 |(dup 1 <) if { 1 - swp "*" + swp prefix }| =prefix
```
