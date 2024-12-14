# Simple Compiler Project

## Overview

This is a basic compiler project demonstrating lexical analysis, parsing, and interpretation of simple arithmetic expressions.

## Project Structure

- `src/lexer/`: Tokenization of input
- `src/parser/`: Converting tokens to Abstract Syntax Tree (AST)
- `src/ast/`: Define AST node types
- `src/interpreter/`: Evaluate the AST
- `src/main.py`: Entry point and REPL

## Features

- Basic arithmetic operations (+, -, \*, /)
- Parenthesized expressions
- Integer support
- Interactive command-line interface

## How to Use

Run `python src/main.py` and enter arithmetic expressions:

```
calc> 5 + 3
8
calc> (2 + 3) * 4
20
calc> 10 / 2
5
```

## Future Expansion

Potential areas to extend:

- Variable support
- More complex data types
- Control flow statements
- Function definitions
