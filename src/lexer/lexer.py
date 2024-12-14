class TokenType:
    """Enumeration of token types"""
    INTEGER = 'INTEGER'
    PLUS = 'PLUS'
    MINUS = 'MINUS'
    MULTIPLY = 'MULTIPLY'
    DIVIDE = 'DIVIDE'
    LPAREN = 'LPAREN'
    RPAREN = 'RPAREN'
    EOF = 'EOF'

class Token:
    """Represents a single token"""
    def __init__(self, type, value):
        self.type = type
        self.value = value
    
    def __str__(self):
        return f'Token({self.type}, {self.value})'
    
    def __repr__(self):
        return self.__str__()

class Lexer:
    """Breaks input into tokens"""
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if text else None
    
    def error(self):
        """Raise an error for invalid input"""
        raise Exception('Invalid character')
    
    def advance(self):
        """Move to the next character"""
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None
    
    def skip_whitespace(self):
        """Skip over whitespace characters"""
        while self.current_char and self.current_char.isspace():
            self.advance()
    
    def integer(self):
        """Parse an integer"""
        result = ''
        while self.current_char and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)
    
    def get_next_token(self):
        """Tokenize the input"""
        while self.current_char:
            # Skip whitespace
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            
            # Parse integers
            if self.current_char.isdigit():
                return Token(TokenType.INTEGER, self.integer())
            
            # Parse operators
            if self.current_char == '+':
                self.advance()
                return Token(TokenType.PLUS, '+')
            
            if self.current_char == '-':
                self.advance()
                return Token(TokenType.MINUS, '-')
            
            if self.current_char == '*':
                self.advance()
                return Token(TokenType.MULTIPLY, '*')
            
            if self.current_char == '/':
                self.advance()
                return Token(TokenType.DIVIDE, '/')
            
            if self.current_char == '(':
                self.advance()
                return Token(TokenType.LPAREN, '(')
            
            if self.current_char == ')':
                self.advance()
                return Token(TokenType.RPAREN, ')')
            
            # If no token is recognized, raise an error
            self.error()
        
        # Return EOF when input is exhausted
        return Token(TokenType.EOF, None)