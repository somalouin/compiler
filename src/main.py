from src.lexer.lexer import Lexer
from src.parser.parser import Parser
from src.interpreter.interpreter import Interpreter

def main():
    """Simple REPL (Read-Eval-Print Loop)"""
    while True:
        try:
            text = input('calc> ')
            
            if text.lower() in ['exit', 'quit']:
                break
            
            # Create lexer, parse input, and interpret
            lexer = Lexer(text)
            parser = Parser(lexer)
            interpreter = Interpreter()
            
            # Execute and print result
            result = interpreter.interpret(parser.parse())
            print(result)
        
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    main()